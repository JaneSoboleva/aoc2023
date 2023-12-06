with open("day05_input_example.txt", 'r') as day05_file:
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

print(seed_list)
for i in range(len(remap_lists)):
    print(remap_lists[i])

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

# Phase 02. Tried to make a lazy solution, but apparently it'll take hours of computing...
# I could maybe parallelize it, but just found out that despite knowing about threading,
# it all still runs on the same core... What a headache, I guess I'll look into proper parallelizing later.
# I'll try to make a "proper" algo for now.


# input: the segment [10, 20], seed range... and 3 numbers of remap rule, according to which we modify
# return: list of 1-3 segments/lists
def modify_one_segment_against_one_remap(the_segment, remap_item):
    seg1_left = the_segment[0]
    seg1_right = the_segment[1]
    seg2_left = remap_item[1]
    seg2_right = remap_item[1] + remap_item[2] - 1
    seg_modifier = remap_item[0] - remap_item[1]

    # case 01: no intersections
    if seg1_right < seg2_left or seg2_right < seg1_left:
        return [[seg1_left, seg1_right]]  # no changes
    # case 02: seg1 completely inside seg2
    if seg1_left >= seg2_left and seg1_right <= seg2_right:
        return [[seg1_left + seg_modifier, seg1_right + seg_modifier]]
    # case 03: seg2 completely inside seg1
    if seg2_left >= seg1_left and seg2_right <= seg1_right:
        rslt = []
        if seg1_left < seg2_left:
            rslt.append([seg1_left, seg2_left - 1])
        rslt.append([seg2_left + seg_modifier, seg2_right + seg_modifier])
        if seg1_right > seg2_right:
            rslt.append([seg2_right + 1, seg1_right])
        return rslt
    # case 04: seg1 intersects with seg2 from the left
    if seg1_left < seg2_left <= seg1_right:
        return [[seg1_left, seg2_left - 1], [seg2_left + seg_modifier, seg1_right + seg_modifier]]
    # case 05: seg1 intersects with seg2 from the right
    if seg2_left < seg1_left <= seg2_right:
        return [[seg1_left + seg_modifier, seg2_right + seg_modifier], [seg2_right + 1, seg1_right]]


def modify_one_segment_against_multiple_remaps(the_segment, remap_items):
    rslt = []
    for xJ in range(1, len(remap_items)):
        modified_segments = modify_one_segment_against_one_remap(the_segment, remap_items[xJ])
        
    return rslt


segment_list = []
for i in range(0, len(seed_list), 2):
    segment_item = [seed_list[i], seed_list[i] + seed_list[i + 1] - 1]
    segment_list.append(segment_item)
print(segment_list)
for i in range(len(remap_lists)):
    segment_list = modify_multiple_segments(segment_list, remap_lists[i])
    # print(segment_list)
