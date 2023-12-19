with open("day19_input.txt", 'r') as day19_file:
    day19_lines = day19_file.read().splitlines()

phase01_sum = 0
workflows = {}
workflow_processing = True
for day19_line in day19_lines:
    if day19_line == "":
        workflow_processing = False
        continue
    if workflow_processing:
        splt1 = day19_line.split("{")
        splt2 = splt1[1][:-1].split(",")
        lst = []
        for splt in splt2:
            if ":" in splt:
                splt3 = splt.split(":")
                if ">" in splt3[0]:
                    splt4 = splt3[0].split(">")
                    lst.append([splt4[0], ">", int(splt4[1]), splt3[1]])
                elif "<" in splt3[0]:
                    splt4 = splt3[0].split("<")
                    lst.append([splt4[0], "<", int(splt4[1]), splt3[1]])
            else:
                lst.append([splt])
        workflows[splt1[0]] = lst
    else:
        splt1 = day19_line[1:-1].split(",")
        part = {}
        for splt0 in splt1:
            splt = splt0.split("=")
            part[splt[0]] = int(splt[1])
        current_workflow = 'in'
        escape_cycle = False
        while True:
            for workflow_item in workflows[current_workflow]:
                if len(workflow_item) == 1:
                    if workflow_item[0] == 'A':
                        for part_item in part:
                            phase01_sum += part[part_item]
                        escape_cycle = True
                        break
                    elif workflow_item[0] == 'R':
                        escape_cycle = True
                        break
                    else:
                        current_workflow = workflow_item[0]
                        break
                elif len(workflow_item) == 4:
                    condition_fulfilled = False
                    if workflow_item[1] == ">":
                        if part[workflow_item[0]] > workflow_item[2]:
                            condition_fulfilled = True
                    elif workflow_item[1] == "<":
                        if part[workflow_item[0]] < workflow_item[2]:
                            condition_fulfilled = True
                    if condition_fulfilled:
                        if workflow_item[3] == 'A':
                            for part_item in part:
                                phase01_sum += part[part_item]
                            escape_cycle = True
                            break
                        elif workflow_item[3] == 'R':
                            escape_cycle = True
                            break
                        else:
                            current_workflow = workflow_item[3]
                            break
            if escape_cycle:
                break
print("Phase 01 result:", phase01_sum)


def calc_part(pa):
    rslt = 1
    for p in pa:
        mlt = pa[p][1] - pa[p][0] + 1
        if mlt < 0:
            mlt = 0
        rslt *= mlt
    # print("calc_part", pa, rslt)  # debug
    return rslt


def dict_copy(d):  # because apparently when you make a dict.copy and modify it, it still influences the original... I swear, copying is so stupid in Python
    rslt = d.copy()
    for r in rslt:
        rslt[r] = rslt[r].copy()  # ...so I have to additionally make a copy of each element to avoid the issue (or use a deepcopy module). Gosh...
    return rslt


def calculate_variations(pa, w, pst):
    if pst >= len(workflows[w]):
        return 0
    p = dict_copy(pa)
    # print("init calculate_variations", p, w, pst)  # debug
    func_res = 0
    w_item = workflows[w][pst]
    if len(w_item) == 1:
        if w_item[0] == "A":
            func_res += calc_part(p)
        elif w_item[0] != "R":
            func_res += calculate_variations(p, w_item[0], 0)
    elif len(w_item) == 4:
        if w_item[1] == ">":
            p = dict_copy(pa)
            p[w_item[0]][0] = w_item[2] + 1
            if w_item[3] == "A":
                func_res += calc_part(p)
            elif w_item[3] != "R":
                func_res += calculate_variations(p, w_item[3], 0)
            p = dict_copy(pa)
            p[w_item[0]][1] = w_item[2]
            func_res += calculate_variations(p, w, pst + 1)
        elif w_item[1] == "<":
            p = dict_copy(pa)
            p[w_item[0]][1] = w_item[2] - 1
            if w_item[3] == "A":
                func_res += calc_part(p)
            elif w_item[3] != "R":
                func_res += calculate_variations(p, w_item[3], 0)
            p = dict_copy(pa)
            p[w_item[0]][0] = w_item[2]
            func_res += calculate_variations(p, w, pst + 1)
    return func_res


print("Phase 02 result:", calculate_variations({"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]}, "in", 0))
