with open("day16_input.txt", 'r') as day16_file:
    day16_lines_copy = day16_file.read().splitlines()


def calculate_energized_tiles(lights):
    day16_lines = day16_lines_copy.copy()
    visited = [[{"right": 0, "left": 0, "up": 0, "down": 0} for i in range(len(day16_lines[0]))] for j in range(len(day16_lines))]
    # visited[i][j]["down"] = 1 assignment would mean that light was passing down through [i, j]th cell.

    direction_movements = {"right": [0, 1], "left": [0, -1], "up": [-1, 0], "down": [1, 0]}
    direction_conversion = {"\\": {"right": ["down"], "left": ["up"], "down": ["right"], "up": ["left"]},
                            "/":  {"right": ["up"], "left": ["down"], "down": ["left"], "up": ["right"]},
                            "-":  {"right": ["right"], "left": ["left"], "up": ["left", "right"], "down": ["left", "right"]},
                            "|":  {"up": ["up"], "down": ["down"], "left": ["up", "down"], "right": ["up", "down"]},
                            ".":  {"up": ["up"], "down": ["down"], "right": ["right"], "left": ["left"]}}
    # lights = [[0, -1, "right"]]  # phase 01 initial configuration; moved to a parameter
    new_visits = 1
    while new_visits > 0:
        new_visits = 0
        newborn_lights = []
        for i in range(len(lights)):
            lights[i][0] += direction_movements[lights[i][2]][0]
            lights[i][1] += direction_movements[lights[i][2]][1]
            if 0 <= lights[i][0] < len(day16_lines) and 0 <= lights[i][1] < len(day16_lines[0]):
                if visited[lights[i][0]][lights[i][1]][lights[i][2]] == 0:
                    visited[lights[i][0]][lights[i][1]][lights[i][2]] = 1
                    new_visits += 1
                    for new_direction in direction_conversion[day16_lines[lights[i][0]][lights[i][1]]][lights[i][2]]:
                        new_light = [lights[i][0], lights[i][1], new_direction]
                        newborn_lights.append(new_light)
        lights = [x[:] for x in newborn_lights]

    count_energized_tiles = 0
    for i in range(len(day16_lines)):
        for j in range(len(day16_lines[0])):
            for d in direction_movements:
                if visited[i][j][d] > 0:
                    count_energized_tiles += 1
                    break
    return count_energized_tiles


phase02_max = calculate_energized_tiles([[0, -1, "right"]])
print("Phase 01 result:", phase02_max)

for i in range(len(day16_lines_copy)):
    phase02_max = max(phase02_max, calculate_energized_tiles([[i, -1, "right"]]))
    phase02_max = max(phase02_max, calculate_energized_tiles([[i, len(day16_lines_copy[0]), "left"]]))
for i in range(len(day16_lines_copy[0])):
    phase02_max = max(phase02_max, calculate_energized_tiles([[-1, i, "down"]]))
    phase02_max = max(phase02_max, calculate_energized_tiles([[len(day16_lines_copy), i, "up"]]))
print("Phase 02 result:", phase02_max)
