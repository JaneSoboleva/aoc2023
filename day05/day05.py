import time


with open("day05_input.txt", 'r') as day05_file:
    day05_lines = day05_file.read().splitlines()

seed_list = day05_lines[0].split()
seed_list.pop(0)
seed_list = [int(x) for x in seed_list]

remap_lists = []
new_remap_list = []
expect_a_new_list = False
for i in range(1, len(day05_lines)):
    if day05_lines[i] == "":
        expect_a_new_list = True
        if len(new_remap_list) > 0:
            remap_lists.append(new_remap_list)
        new_remap_list = []
        continue
    if expect_a_new_list:
        new_remap_list.append(day05_lines[i].split()[0])
        expect_a_new_list = False
        continue
    new_remap_element = []
    new_remap_split = day05_lines[i].split()
    for j in range(0, 3):
        new_remap_element.append(int(new_remap_split[j]))
    new_remap_list.append(new_remap_element)
if len(new_remap_list) > 0:
    remap_lists.append(new_remap_list)

# print(seed_list)
# for i in range(len(remap_lists)):
#     print(remap_lists[i])

# done collecting data, now for the actual solution...

def remap_number(initial_number, remap_element):
    for xI in range(1, len(remap_element)):
        if remap_element[xI][1] <= initial_number <= remap_element[xI][1] + remap_element[xI][2] - 1:
            return initial_number - (remap_element[xI][1] - remap_element[xI][0])
    return initial_number


phase01_minimum = ""
for i in range(len(seed_list)):
    seed_item = seed_list[i]
    # print(seed_item, end = " => ")
    for j in range(len(remap_lists)):
        seed_item = remap_number(seed_item, remap_lists[j])
        # print(seed_item, end=" => ")
    # print(" end ")
    if phase01_minimum == "":
        phase01_minimum = seed_item
    else:
        if phase01_minimum > seed_item:
            phase01_minimum = seed_item
print("Phase 01 result:", phase01_minimum)

# Phase 02. Tried to make a lazy solution, it worked too slowly... tried to make a smart solution, messed it up
# rolling back to the lazy solution since I'm past 24h+ mark already anyway

phase02_minimum = 10 ** 10
start_time = time.time()
counter = 0
for i in range(0, len(seed_list), 2):
    range_left = seed_list[i]
    range_right = seed_list[i] + seed_list[i + 1]
    for x in range(range_left, range_right):
        counter += 1
        if counter >= 1000000:
            new_time = time.time()
            print(new_time - start_time, "seconds passed. Processing", x, "in range", range_left, "-", range_right)
            counter = 0
        # print(seed_item, end = " => ")
        seed_item = x
        for j in range(len(remap_lists)):
            seed_item = remap_number(seed_item, remap_lists[j])
            # print(seed_item, end=" => ")
        # print(" end ")
        if phase02_minimum > seed_item:
            phase02_minimum = seed_item
print("Phase 02 result:", phase02_minimum)
f = open("output.txt", "w")
f.write("Phase 02 result: " + str(phase02_minimum))
f.close()
