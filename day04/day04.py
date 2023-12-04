with open("day04_input.txt", 'r') as day04_file:
    day04_lines = day04_file.read().splitlines()

phase01_sum = 0
matching_numbers = []
for day04_line in day04_lines:
    multiplier = 1
    matching = 0
    max_num = 100
    card_numbers = [0] * max_num
    my_numbers = [0] * max_num
    split01 = day04_line.split(": ")
    split02 = split01[1].split(" | ")
    split_card_numbers = split02[0].split()
    split_my_numbers = split02[1].split()
    for card_number in split_card_numbers:
        card_numbers[int(card_number)] += 1
    for my_number in split_my_numbers:
        my_numbers[int(my_number)] += 1
    for i in range(max_num):
        if card_numbers[i] > 0 and my_numbers[i] > 0:
            multiplier *= 2
            matching += 1
    phase01_sum += int(multiplier / 2)
    matching_numbers.append(matching)
print("Phase 01 result:", phase01_sum)
# print(matching_numbers)
# ---
phase02_sum = 0
copies = [1] * len(matching_numbers)
for i in range(len(copies)):
    phase02_sum += copies[i]
    k = matching_numbers[i]
    for j in range(i + 1, i + 1 + k):
        copies[j] += copies[i]
    # print(copies)
print("Phase 02 result:", phase02_sum)
