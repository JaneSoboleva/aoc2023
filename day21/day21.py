with open("day21_input.txt", 'r') as day21_file:
    day21_map = day21_file.read().splitlines()

for i in range(len(day21_map)):
    day21_map[i] = list(day21_map[i])

for steps in range(64):
    day21_map_copy = []
    possible_coords = []
    possible_deltas = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for r in range(len(day21_map)):
        l = []
        for c in range(len(day21_map[0])):
            if day21_map[r][c] == 'S':
                possible_coords.append([r, c])
                l.append('.')
            else:
                l.append(day21_map[r][c])
        day21_map_copy.append(l)
    for coord in possible_coords:
        r, c = coord[0], coord[1]
        for possible_delta in possible_deltas:
            nr = r + possible_delta[0]
            nc = c + possible_delta[1]
            if 0 <= nr < len(day21_map_copy) and 0 <= nc < len(day21_map_copy[0]):
                if day21_map_copy[nr][nc] == '.':
                    day21_map_copy[nr][nc] = 'S'
    day21_map = [x[:] for x in day21_map_copy]

phase01_sum = 0
for i in range(len(day21_map)):
    for j in range(len(day21_map[0])):
        if day21_map[i][j] == 'S':
            phase01_sum += 1
print("Phase 01 result:", phase01_sum)
