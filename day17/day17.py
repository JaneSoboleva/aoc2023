with open("day17_input.txt", 'r') as day17_file:
    heatloss = [[int(ch) for ch in line] for line in day17_file.read().splitlines()]

maximum_steps_in_one_direction = 10
minimums = [[{"up": {i: 10**9 for i in range(maximum_steps_in_one_direction + 1)},
              "down": {i: 10**9 for i in range(maximum_steps_in_one_direction + 1)},
              "left": {i: 10**9 for i in range(maximum_steps_in_one_direction + 1)},
              "right": {i: 10**9 for i in range(maximum_steps_in_one_direction + 1)}} for i in range(len(heatloss[0]))] for j in range(len(heatloss))]
# basically, minimums[row][column][direction, after taking which we ended up here][steps so far in this direction] = minimum heat loss found so far
clockwise_change = {"up": "right", "right": "down", "down": "left", "left": "up"}
counterclockwise_change = {"up": "left", "left": "down", "down": "right", "right": "up"}
direction_movements = {"right": [0, 1], "left": [0, -1], "up": [-1, 0], "down": [1, 0]}


def get_minimum(value):
    return minimums[value[0]][value[1]][value[2]][value[3]]
def update_minimum(value, new_min):
    minimums[value[0]][value[1]][value[2]][value[3]] = new_min
def inbounds(value):
    return 0 <= value[0] < len(heatloss) and 0 <= value[1] < len(heatloss[0])
def get_heatloss(value):
    return heatloss[value[0]][value[1]]
def get_moving(value):
    value[0] += direction_movements[value[2]][0]
    value[1] += direction_movements[value[2]][1]
    value[3] += 1
def turn_right(value):
    value[2] = clockwise_change[value[2]]
    value[3] = 0
def turn_left(value):
    value[2] = counterclockwise_change[value[2]]
    value[3] = 0
def attempt_movement(item, direction, phase):
    new_item = item.copy()
    # special restrictions for phases 1 and 2 ---
    if direction == "straight":
        if phase == 1:
            if new_item[3] >= 3:
                return  # phase 1, can't go straight for more than 3 blocks
        if phase == 2:
            if new_item[3] >= 10:
                return  # phase 2, can't go straight for more than 10 blocks
    if direction == "right":
        if phase == 2:
            if new_item[3] < 4:
                return  # phase 2, can't turn right if went straight for less than 4 blocks
        turn_right(new_item)
    if direction == "left":
        if phase == 2:
            if new_item[3] < 4:
                return  # phase 2, can't turn left if went straight for less than 4 blocks
        turn_left(new_item)
    # --- end of specifying restrictions
    get_moving(new_item)
    if inbounds(new_item):
        new_minimum = get_minimum(item) + get_heatloss(new_item)
        if get_minimum(new_item) > new_minimum:
            update_minimum(new_item, new_minimum)
            newly_updated.append(new_item)
def get_minimum_by_coordinates(row, col):
    rslt = 10 ** 9
    for direction in direction_movements:
        for xI in range(maximum_steps_in_one_direction + 1):
            rslt = min(rslt, minimums[row][col][direction][xI])
    return rslt


minimums[0][0]["right"][0] = 0
recently_updated = [[0, 0, "right", 0]]  # row, column, direction, steps so far
while len(recently_updated) > 0:
    newly_updated = []
    for r_item in recently_updated:
        attempt_movement(r_item, "straight", phase=1)
        attempt_movement(r_item, "right", phase=1)
        attempt_movement(r_item, "left", phase=1)
    recently_updated = [x[:] for x in newly_updated]
print("Phase 01 result:", get_minimum_by_coordinates(-1, -1))

# copypasting, too lazy to do this more efficiently
minimums = [[{"up": {i: 10**9 for i in range(11)},
              "down": {i: 10**9 for i in range(11)},
              "left": {i: 10**9 for i in range(11)},
              "right": {i: 10**9 for i in range(11)}} for i in range(len(heatloss[0]))] for j in range(len(heatloss))]
minimums[0][0]["right"][0] = 0
recently_updated = [[0, 0, "right", 0]]  # row, column, direction, steps so far
while len(recently_updated) > 0:
    newly_updated = []
    for r_item in recently_updated:
        attempt_movement(r_item, "straight", phase=2)
        attempt_movement(r_item, "right", phase=2)
        attempt_movement(r_item, "left", phase=2)
    recently_updated = [x[:] for x in newly_updated]
# tamper with the minimums so that we only account for those that had >= 4 movements in the same direction prior to arriving to the destination
# to comply with this: "...before it can turn (or even before it can stop at the end)..."
for d in direction_movements:
    for i in range(4):
        minimums[-1][-1][d][i] = 10 ** 9
# ---
print("Phase 02 result:", get_minimum_by_coordinates(-1, -1))
