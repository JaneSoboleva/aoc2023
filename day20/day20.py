with open("day20_input.txt", 'r') as day20_file:
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
for inpt in inputs:
    if module_types[inpt] == "conjunction":
        conjunction_memory[inpt] = {}
        for lst in inputs:
            if inpt in inputs[lst]:
                conjunction_memory[inpt][lst] = 0
        conjunction_memory[inpt]["~sum"] = 0

# print(module_types, "\n", flip_flop_values, "\n", inputs, "\n", conjunction_memory)  # debug


def signal_info(sg):
    sg_value = {0: "low", 1: "high"}
    print(sg["sender"], '-' + sg_value[sg["value"]] + "->", sg["recipient"])


def push_button():
    signals_received = [{"sender": "button", "recipient": "broadcaster", "value": 0}]
    pulse_count = [0, 0]
    phase02_monitor_rx = False
    while len(signals_received) > 0:
        new_signals = []
        for signal in signals_received:
            # signal_info(signal)  # debug
            pulse_count[signal["value"]] += 1
            if module_types.get(signal["recipient"], -1) == -1:
                module_types[signal["recipient"]] = "ordinary"
                inputs[signal["recipient"]] = []
            if signal["recipient"] == "rx" and signal["value"] == 0:
                phase02_monitor_rx = True
            if module_types[signal["recipient"]] == "flip-flop" and signal["value"] == 0:
                flip_flop_values[signal["recipient"]] = 1 - flip_flop_values[signal["recipient"]]
                for inp in inputs[signal["recipient"]]:
                    new_signals.append({"sender": signal["recipient"], "recipient": inp, "value": flip_flop_values[signal["recipient"]]})
            elif module_types[signal["recipient"]] == "conjunction":
                current_memory = conjunction_memory[signal["recipient"]][signal["sender"]]
                if current_memory == 0 and signal["value"] == 1:
                    conjunction_memory[signal["recipient"]]["~sum"] += 1
                elif current_memory == 1 and signal["value"] == 0:
                    conjunction_memory[signal["recipient"]]["~sum"] -= 1
                conjunction_memory[signal["recipient"]][signal["sender"]] = signal["value"]
                if conjunction_memory[signal["recipient"]]["~sum"] == len(conjunction_memory[signal["recipient"]]) - 1:
                    for inp in inputs[signal["recipient"]]:
                        new_signals.append({"sender": signal["recipient"], "recipient": inp, "value": 0})
                else:
                    for inp in inputs[signal["recipient"]]:
                        new_signals.append({"sender": signal["recipient"], "recipient": inp, "value": 1})
            elif module_types[signal["recipient"]] == "ordinary":
                for inp in inputs[signal["recipient"]]:
                    new_signals.append({"sender": signal["recipient"], "recipient": inp, "value": signal["value"]})
        signals_received = new_signals.copy()
    # print("---")
    return pulse_count, phase02_monitor_rx


low_pulse_count, high_pulse_count, rx_id_found, i = 0, 0, -1, 0
while True:
    p_count, is_rx_found = push_button()
    if is_rx_found and rx_id_found == -1:
        rx_id_found = i + 1
        print("Phase 02 result:", rx_id_found)
        break
    low_pulse_count += p_count[0]
    high_pulse_count += p_count[1]
    if i == 999:
        print("Phase 01 result:", low_pulse_count * high_pulse_count)
    i += 1
