with open("day20_input_example1.txt", 'r') as day20_file:
    day20_lines = day20_file.read().splitlines()
day20_lines.append("button -> broadcaster")

module_types = {}
flip_flop_values = {}
inputs = {}
for day20_line in day20_lines:
    module_type = "ordinary"
    if day20_line[0] == "%":
        module_type = "flip-flop"
        day20_line = day20_line[1:]
    if day20_line[0] == "&":
        module_type = "conjunction"
        day20_line = day20_line[1:]
    splt = day20_line.split(" -> ")
    module_name = splt[0]
    module_types[module_name] = module_type
    if module_type == "flip-flop":
        flip_flop_values[module_name] = 0
    inputs[module_name] = splt[1].split(", ")

conjunction_memory = {}
for inp in inputs:
    if module_types[inp] == "conjunction":
        conjunction_memory[inp] = {}
        for lst in inputs:
            if inp in inputs[lst]:
                conjunction_memory[inp][lst] = 0

print(module_types, "\n", flip_flop_values, "\n", inputs, "\n", conjunction_memory)  # debug

signals = [{"sender": "button", "recipient": "broadcaster", "value": 0}]
while len(signals) > 0:
    new_signals = []
    for signal in signals:
        if module_types[signal["recipient"]] == "flip-flop" and signal["value"] == 0:
            flip_flop_values[sender] = 1 - flip_flop_values[sender]
            for inp in inputs[sender]:
                recipients