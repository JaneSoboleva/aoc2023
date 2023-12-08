with open("day08_input.txt", 'r') as day08_file:
    day08_lines = day08_file.read().splitlines()

navigation_path = day08_lines[0]
crossroad = []
turn_left = []
turn_right = []
for i in range(2, len(day08_lines)):
    splt = day08_lines[i].split()
    crossroad.append(splt[0])
    turn_left.append(splt[2][1:-1])
    turn_right.append(splt[3][:-1])
# print(crossroad)
# print(turn_left)
# print(turn_right)
# ---
steps_taken = 0
current_navigation_position = 0
current_node = 'AAA'
final_node = 'ZZZ'
try:
    ind = crossroad.index(current_node)
except Exception as e:
    print(e)
    print("Phase 01 result: none")
else:
    while current_node != final_node:
        ind = crossroad.index(current_node)
        if navigation_path[current_navigation_position] == 'L':
            current_node = turn_left[ind]
        else:
            current_node = turn_right[ind]
        current_navigation_position += 1
        if current_navigation_position >= len(navigation_path):
            current_navigation_position = 0
        steps_taken += 1
    print("Phase 01 result:", steps_taken)
# ---
'''
current_nodes = []
for i in range(len(crossroad)):
    if crossroad[i].endswith("A"):
        current_nodes.append(crossroad[i])
ends_with_z_counter = 0
steps_taken = 0
current_navigation_position = 0
while ends_with_z_counter < len(current_nodes):
    ends_with_z_counter = 0
    steps_taken += 1
    if navigation_path[current_navigation_position] == 'L':
        for i in range(len(current_nodes)):
            current_nodes[i] = turn_left[crossroad.index(current_nodes[i])]
            if current_nodes[i].endswith("Z"):
                ends_with_z_counter += 1
                print("Route", i, "and position", current_navigation_position, "ended up on", current_nodes[i], "after", steps_taken, "steps.", end="")
                input()
    else:
        for i in range(len(current_nodes)):
            current_nodes[i] = turn_right[crossroad.index(current_nodes[i])]
            if current_nodes[i].endswith("Z"):
                ends_with_z_counter += 1
                print("Route", i, "and position", current_navigation_position, "ended up on", current_nodes[i], "after", steps_taken, "steps.", end="")
                input()
    current_navigation_position += 1
    if current_navigation_position >= len(navigation_path):
        current_navigation_position = 0
'''
# I was wondering if there are some tricky smaller loops after bigger non-loops, but the code above lets us know
# that we have perfect loops from the start with the following lengths: [11309, 13939, 16043, 17621, 18673, 20777]
# so basically we need to find the least common multiple of those... which is 13740108158591
# I felt lazy, so I ended up calculating those via an online service of finding LCM instead of coding it, but oh well.
