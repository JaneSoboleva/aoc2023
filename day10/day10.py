with open("day10_input.txt", 'r') as day10_file:
    day10_lines = day10_file.read().splitlines()
for i in range(len(day10_lines)):
    day10_lines[i] = '.' + day10_lines[i] + '.'
day10_new_row = '.' * len(day10_lines[0])
day10_lines.insert(0, day10_new_row)
day10_lines.append(day10_new_row)
visited = [[0 for i in range(len(day10_lines[0]))] for j in range(len(day10_lines))]
# for i in range(len(day10_lines)):
#     print(day10_lines[i])

init_row = 0
init_column = 0
for row in range(0, len(day10_lines)):
    if 'S' in day10_lines[row]:
        init_row = row
        init_column = day10_lines[row].index('S')
# print(init_row, init_column)

list_of_connections = {"|": "UD", "-": "RL", "L": "UR", "F": "RD", "J": "UL", "7": "DL", ".": ""}
list_of_backwards_connections = {"UD": "|", "RL": "-", "UR": "L", "RD": "F", "UL": "J", "DL": "7"}
meaning_of_connections = {"U": [-1, 0], "R": [0, 1], "D": [1, 0], "L": [0, -1]}

p_up = list_of_connections[day10_lines[init_row - 1][init_column]]
p_right = list_of_connections[day10_lines[init_row][init_column + 1]]
p_down = list_of_connections[day10_lines[init_row + 1][init_column]]
p_left = list_of_connections[day10_lines[init_row][init_column - 1]]
s_c = ''
if 'D' in p_up:
    s_c += 'U'
if 'L' in p_right:
    s_c += 'R'
if 'U' in p_down:
    s_c += 'D'
if 'R' in p_left:
    s_c += 'L'
day10_lines[init_row] = day10_lines[init_row].replace("S", list_of_backwards_connections[s_c])
# assigned the correct symbol instead of S, just in case...
# for i in range(len(day10_lines)):
#     print(day10_lines[i])

# navigating...
current_row = init_row
current_column = init_column
steps_taken = 0
visited[init_row][init_column] = 1
while True:
    connections = list_of_connections[day10_lines[current_row][current_column]]
    direction1 = meaning_of_connections[connections[0]]
    direction2 = meaning_of_connections[connections[1]]
    visited1 = visited[current_row + direction1[0]][current_column + direction1[1]]
    visited2 = visited[current_row + direction2[0]][current_column + direction2[1]]
    if visited1 > 0 and visited2 > 0:
        break
    if visited2 > 0:
        current_row += direction1[0]
        current_column += direction1[1]
    else:
        current_row += direction2[0]
        current_column += direction2[1]
    visited[current_row][current_column] = 1
    steps_taken += 1
print("Phase 01 result:", int((steps_taken + 1) / 2))
