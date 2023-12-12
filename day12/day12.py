def pattern_corresponds_to_length_values(pattern_value, length_values):
    pattern = '.' + pattern_value + '.'
    invalid_counter = 0
    current_index = 0
    for xI in range(1, len(pattern)):
        if pattern[xI] == '.' and pattern[xI - 1] == '#':
            if current_index >= len(length_values):
                return False
            if length_values[current_index] != invalid_counter:
                return False
            current_index += 1
            invalid_counter = 0
        elif pattern[xI] == '#':
            invalid_counter += 1
    return current_index == len(length_values)


def bruteforce_number_of_variations(pattern_value, length_values, current_index):
    if current_index >= len(pattern_value):
        if pattern_corresponds_to_length_values(pattern_value, length_values):
            return 1
        else:
            return 0
    if pattern_value[current_index] == '?':
        func_result = 0
        func_result += bruteforce_number_of_variations(pattern_value[:current_index] + "." + pattern_value[current_index + 1:], length_values, current_index + 1)
        func_result += bruteforce_number_of_variations(pattern_value[:current_index] + "#" + pattern_value[current_index + 1:], length_values, current_index + 1)
        return func_result
    else:
        return bruteforce_number_of_variations(pattern_value, length_values, current_index + 1)


with open("day12_input.txt", 'r') as day12_file:
    day12_lines = day12_file.read().splitlines()

patterns = []
lengths = []
for day12_line in day12_lines:
    splt = day12_line.split()
    patterns.append(splt[0])
    lengths.append([int(x) for x in splt[1].split(",")])

phase01_sum = 0
q_count_max = 0
for i in range(len(patterns)):
    q_count_cur = 0
    for j in range(len(patterns[i])):
        if patterns[i][j] == '?':
            q_count_cur += 1
    q_count_max = max(q_count_cur, q_count_max)
    bruteforce_options = bruteforce_number_of_variations(patterns[i], lengths[i], 0)
    phase01_sum += bruteforce_options
    print(patterns[i], lengths[i], bruteforce_options)
print("Phase 01 result:", phase01_sum)
print("q_count:", q_count_max)

# Phase 02. Unfolding...
