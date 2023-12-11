with open("day11_input.txt", 'r') as day11_file:
    space_map = day11_file.read().splitlines()

# expanding rows
empty_row = ''
for i in range(len(space_map[0])):
    empty_row += 'M'
for i in range(len(space_map) - 1, -1, -1):
    if not '#' in space_map[i]:
        space_map[i] = empty_row

# expanding columns
for i in range(len(space_map[0]) - 1, -1, -1):
    c = 0
    for j in range(len(space_map)):
        if space_map[j][i] == '#':
            c = 1
            break
    if c == 0:
        for j in range(len(space_map)):
            space_map[j] = space_map[j][:i] + 'M' + space_map[j][i + 1:]

# for i in range(len(space_map)):
#     print(space_map[i])

coords = []
for i in range(len(space_map)):
    for j in range(len(space_map[0])):
        if space_map[i][j] == '#':
            new_coord = [i, j]
            coords.append(new_coord)
diff_sum_phase1 = 0
diff_sum_phase2 = 0
exp_phase1 = 2
exp_phase2 = 1000000
for i in range(len(coords) - 1):
    for j in range(i + 1, len(coords)):
        current_coord = [min(coords[i][0], coords[j][0]), min(coords[i][1], coords[j][1])]
        target_coord = [max(coords[i][0], coords[j][0]), max(coords[i][1], coords[j][1])]
        while current_coord[0] < target_coord[0]:
            current_coord[0] += 1
            if space_map[current_coord[0]][current_coord[1]] == 'M':
                diff_sum_phase1 += exp_phase1
                diff_sum_phase2 += exp_phase2
            else:
                diff_sum_phase1 += 1
                diff_sum_phase2 += 1
        while current_coord[1] < target_coord[1]:
            current_coord[1] += 1
            if space_map[current_coord[0]][current_coord[1]] == 'M':
                diff_sum_phase1 += exp_phase1
                diff_sum_phase2 += exp_phase2
            else:
                diff_sum_phase1 += 1
                diff_sum_phase2 += 1
print("Phase 01 result:", diff_sum_phase1)
print("Phase 02 result:", diff_sum_phase2)
