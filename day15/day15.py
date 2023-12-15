def hash_algo(s):
    rslt = 0
    for c in s:
        rslt += ord(c)
        rslt = (rslt * 17) % 256
    return rslt


with open("day15_input.txt", 'r') as day15_file:
    day15_line = day15_file.read().splitlines()[0].split(",")

phase01_sum = 0
for day15_item in day15_line:
    phase01_sum += hash_algo(day15_item)
    # print(day15_item, hash_algo(day15_item))
print("Phase 01 result:", phase01_sum)

number_of_boxes = 256
box_lens_ids = [[] for i in range(number_of_boxes)]
box_focal_ls = [[] for i in range(number_of_boxes)]


def debug_info():
    for xI in range(len(box_lens_ids)):
        if len(box_lens_ids[xI]) > 0:
            print("Box " + str(xI) + ": ", end="")
            for xJ in range(len(box_lens_ids[xI])):
                print("[" + str(box_lens_ids[xI][xJ]) + " " + str(box_focal_ls[xI][xJ]) + "] ", end="")
            print("")
    print("---")


for day15_item in day15_line:
    operation, lens_id, focal_ls = 'none', 'none', 'none'
    if '-' in day15_item:
        operation = 'remove'
        lens_id = day15_item[:-1]
    if '=' in day15_item:
        operation = 'assign'
        splt = day15_item.split("=")
        lens_id = splt[0]
        focal_ls = int(splt[1])
    box_id = hash_algo(lens_id)
    if operation == 'remove':
        if lens_id in box_lens_ids[box_id]:
            id_to_remove = box_lens_ids[box_id].index(lens_id)
            box_lens_ids[box_id].pop(id_to_remove)
            box_focal_ls[box_id].pop(id_to_remove)
    if operation == 'assign':
        if lens_id in box_lens_ids[box_id]:
            id_to_modify = box_lens_ids[box_id].index(lens_id)
            box_focal_ls[box_id][id_to_modify] = focal_ls
        else:
            box_lens_ids[box_id].append(lens_id)
            box_focal_ls[box_id].append(focal_ls)
    # debug_info()

phase02_sum = 0
for i in range(len(box_lens_ids)):
    for j in range(len(box_lens_ids[i])):
        phase02_sum += ((i + 1) * (j + 1) * box_focal_ls[i][j])
print("Phase 02 result:", phase02_sum)
