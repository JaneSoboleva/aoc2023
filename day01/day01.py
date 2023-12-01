def detect_digit(inp, pst):
    word_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    if ord('0') <= ord(inp[pst]) <= ord('9'):
        return ord(inp[pst]) - 48
    for j in range(len(word_digits)):
        if inp[pst:].startswith(word_digits[j]):
            return j + 1
    return -1


with open("day01_input.txt", 'r') as day01_file:
    day01_lines = day01_file.read().splitlines()
digit_sum = 0
for day01_line in day01_lines:
    digit_left = 0
    digit_right = 0
    for i in range(len(day01_line)):
        current_digit = detect_digit(day01_line, i)
        if current_digit >= 0:
            digit_left = current_digit
            break
    for i in range(len(day01_line) - 1, -1, -1):
        current_digit = detect_digit(day01_line, i)
        if current_digit >= 0:
            digit_right = current_digit
            break
    number_to_add = digit_left * 10 + digit_right
    # print(day01_line, number_to_add)
    digit_sum += number_to_add
print("Result:", digit_sum)
