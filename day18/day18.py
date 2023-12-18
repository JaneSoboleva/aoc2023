with open("day18_input.txt", 'r') as day18_file:
    day18_lines = day18_file.read().splitlines()

instructions, coordinates, view_from_above = [], [[0, 0]], []
min_row, max_row, min_column, max_column, current_row, current_column = 0, 0, 0, 0, 0, 0
direction_movement = {"R": [0, 1], "L": [0, -1], "U": [-1, 0], "D": [1, 0]}
for day18_line in day18_lines:
    splt = day18_line.split()
    instructions.append(day18_line.split())
    for i in range(int(splt[1])):
        current_row += direction_movement[splt[0]][0]
        current_column += direction_movement[splt[0]][1]
        coordinates.append([current_row, current_column])
    if min_row > current_row:
        min_row = current_row
    if max_row < current_row:
        max_row = current_row
    if min_column > current_column:
        min_column = current_column
    if max_column < current_column:
        max_column = current_column
for i in range(max_row - min_row + 1):
    s = ''
    for j in range(max_column - min_column + 1):
        if [min_row + i, min_column + j] in coordinates:
            s += '#'
        else:
            s += '.'
    view_from_above.append(s)
empty_row = '.' * len(view_from_above[0])
view_from_above.insert(0, empty_row)
view_from_above.append(empty_row)
for i in range(len(view_from_above)):
    view_from_above[i] = '.' + view_from_above[i] + '.'
# here's how the view from above looks:
# for s in view_from_above:
#     print(s)
# doing DFS from outside
last_updated = [[0, 0]]
outside_coords = [[0, 0]]
while len(last_updated) > 0:
    newly_updated = []
    for coord in last_updated:
        for d in direction_movement:
            new_coord = coord.copy()
            new_coord[0] += direction_movement[d][0]
            new_coord[1] += direction_movement[d][1]
            if 0 <= new_coord[0] < len(view_from_above) and 0 <= new_coord[1] < len(view_from_above[0]):
                if view_from_above[new_coord[0]][new_coord[1]] != '#':
                    if not new_coord in outside_coords:
                        newly_updated.append(new_coord)
                        outside_coords.append(new_coord)
    last_updated = newly_updated.copy()
updated_view_from_above = []
for i in range(len(view_from_above)):
    s = ''
    for j in range(len(view_from_above[i])):
        if [i, j] in outside_coords:
            s = s + '.'
        else:
            s = s + '#'
    updated_view_from_above.append(s)
    # print(s)  # to see the updated view from above
print("Phase 01 result:", len(view_from_above) * len(view_from_above[0]) - len(outside_coords))
