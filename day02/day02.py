with open("day02_input.txt", 'r') as day02_file:
    day02_lines = day02_file.read().splitlines()

phase01_sum = 0
phase02_sum = 0
for day02_line in day02_lines:
    split01 = day02_line.split(": ")
    game_id = int(split01[0].split()[1])
    condition01_possible = True
    colors = ["red", "green", "blue"]
    max_amount = [12, 13, 14]
    limit_amount = [0, 0, 0]
    split02 = split01[1].split("; ")
    for token02 in split02:
        current_amount = [0, 0, 0]
        split03 = token02.split(", ")
        for token03 in split03:
            cube_number = int(token03.split()[0])
            cube_color = colors.index(token03.split()[1])
            current_amount[cube_color] += cube_number
        for i in range(len(max_amount)):
            if current_amount[i] > max_amount[i]:
                condition01_possible = False
            if limit_amount[i] < current_amount[i]:
                limit_amount[i] = current_amount[i]
    if condition01_possible:
        phase01_sum += game_id
    phase02_sum += (limit_amount[0] * limit_amount[1] * limit_amount[2])
print("Phase 01 result:", phase01_sum)
print("Phase 02 result:", phase02_sum)
