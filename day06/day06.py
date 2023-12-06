with open("day06_input.txt", 'r') as day06_file:
    day06_lines = day06_file.read().splitlines()

time_list = day06_lines[0].split()
time_list.pop(0)
mega_time = ''
for time_item in time_list:
    mega_time += time_item
mega_time = int(mega_time)
time_list = [int(x) for x in time_list]
distance_list = day06_lines[1].split()
distance_list.pop(0)
mega_distance = ''
for distance_item in distance_list:
    mega_distance += distance_item
mega_distance = int(mega_distance)
distance_list = [int(x) for x in distance_list]

variations = []
variation_multiple = 1
for i in range(len(time_list)):
    variation = 0
    for j in range(time_list[i]):
        k = j * (time_list[i] - j)
        # print(j, '*', time_list[i] - j, '=', k, end = " | ")
        if k > distance_list[i]:
            variation += 1
            # print("(pass) | ", end="")
    variations.append(variation)
    variation_multiple *= variation
print("Phase 01 result:", variation_multiple)
# print(variations)

time_list = [mega_time]
distance_list = [mega_distance]
# copypasting... (and yeah, I know about sqrt. Don't feel like it, the solution is found within seconds anyway)
variations = []
variation_multiple = 1
for i in range(len(time_list)):
    variation = 0
    for j in range(time_list[i]):
        k = j * (time_list[i] - j)
        # print(j, '*', time_list[i] - j, '=', k, end = " | ")
        if k > distance_list[i]:
            variation += 1
            # print("(pass) | ", end="")
    variations.append(variation)
    variation_multiple *= variation
print("Phase 02 result:", variation_multiple)
