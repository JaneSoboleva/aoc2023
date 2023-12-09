def extrapolate(number_line):
    last_number_line = number_line.copy()
    final_result_01 = last_number_line[-1]
    first_values = [last_number_line[0]]
    new_number_sum = 1
    while new_number_sum > 0:
        new_number_line = []
        new_number_sum = 0
        new_element = 0
        first_values.append(last_number_line[1] - last_number_line[0])
        for xI in range(1, len(last_number_line)):
            new_element = last_number_line[xI] - last_number_line[xI - 1]
            new_number_sum += abs(new_element)
            new_number_line.append(new_element)
        final_result_01 += new_element
        last_number_line = new_number_line.copy()
    last_number_02 = 0
    for xI in range(len(first_values) - 2, -1, -1):
        last_number_02 = first_values[xI] - last_number_02
    return final_result_01, last_number_02


with open("day09_input.txt", 'r') as day09_file:
    day09_lines = day09_file.read().splitlines()

number_lines = []
for day09_line in day09_lines:
    number_lines.append([int(x) for x in day09_line.split()])

phase01_sum = 0
phase02_sum = 0
for c_number_line in number_lines:
    phase01_delta, phase02_delta = extrapolate(c_number_line)
    phase01_sum += phase01_delta
    phase02_sum += phase02_delta
print("Phase 01 result:", phase01_sum)
print("Phase 02 result:", phase02_sum)
