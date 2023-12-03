def is_digit(char_value):
    if ord('0') <= ord(char_value) <= ord('9'):
        return ord(char_value) - 48
    else:
        return -1


with open("day03_input.txt", 'r') as day03_file:
    day03_lines = day03_file.read().splitlines()

# expanding the map by 1
empty_row = '.' * len(day03_lines[0])
day03_lines.insert(0, empty_row)
day03_lines.append(empty_row)
day03_lines.append(empty_row)
for i in range(len(day03_lines)):
    day03_lines[i] = '.' + day03_lines[i] + '..'
# for day03_line in day03_lines:
#     print(day03_line)

# creating an array for gears, [x][y][0] is amount of numbers nearby, [x][y][1] is a result of their multiplication
gear_list = [[[0, 1] for i in range(len(day03_lines[0]))] for j in range(len(day03_lines))]

phase01_sum = 0
for i in range(1, len(day03_lines) - 1):
    # print('(debug) line:', day03_lines[i])
    current_number = 0
    is_adjacent = False
    last_symbol_was_a_digit = False
    nearby_gears = set()
    for j in range(1, len(day03_lines[0]) - 1):
        # --- checking whether the current char is adjacent to a symbol (not dot and not digit)
        is_symbol_adjacent = False
        for x in range(-1, 2):
            for y in range(-1, 2):
                if not (x == 0 and y == 0):
                    c = day03_lines[i + x][j + y]
                    d = is_digit(c)
                    if c != '.' and d == -1:
                        is_symbol_adjacent = True
                    if c == '*' and is_digit(day03_lines[i][j]) >= 0:
                        nearby_gears.add((i + x) * 10000 + (j + y))
        # --- end of checking
        d = is_digit(day03_lines[i][j])
        if d == -1 and last_symbol_was_a_digit:  # encountered not a digit, while last symbol was a digit
            if is_adjacent:
                phase01_sum += current_number
                for gear_item in nearby_gears:
                    gear_item_x = int(gear_item / 10000)
                    gear_item_y = gear_item % 10000
                    gear_list[gear_item_x][gear_item_y][0] += 1
                    gear_list[gear_item_x][gear_item_y][1] *= current_number
            # print(current_number, is_adjacent, "| ", end="")
            current_number = 0
            is_adjacent = False
            last_symbol_was_a_digit = False
            nearby_gears = set()
        if d >= 0:  # encountered a digit
            current_number = current_number * 10 + d
            if is_symbol_adjacent:
                is_adjacent = True
            last_symbol_was_a_digit = True
    # print("")
print("Phase 01 result:", phase01_sum)

phase02_sum = 0
for i in range(len(gear_list)):
    for j in range(len(gear_list[0])):
        if gear_list[i][j][0] == 2:
            phase02_sum += gear_list[i][j][1]
print("Phase 02 result:", phase02_sum)
