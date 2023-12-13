def find_result_01(a):
    def equal_rows(row1, row2):
        if 0 <= row1 < len(a) and 0 <= row2 < len(a):
            return a[row1] == a[row2]
        else:
            return "out_of_range"
    def equal_columns(col1, col2):
        if 0 <= col1 < len(a[0]) and 0 <= col2 < len(a[0]):
            s_col1 = ""
            s_col2 = ""
            for xI in range(len(a)):
                s_col1 += a[xI][col1]
                s_col2 += a[xI][col2]
            return s_col1 == s_col2
        else:
            return "out_of_range"
    for xJ in range(len(a) - 1):
        for xDelta in range(len(a)):
            x_row1 = xJ - xDelta
            x_row2 = xJ + xDelta + 1
            x_equal_rows = equal_rows(x_row1, x_row2)
            if not x_equal_rows:
                break
            if x_equal_rows == "out_of_range":
                return (xJ + 1) * 100
    for xJ in range(len(a[0]) - 1):
        for xDelta in range(len(a[0])):
            x_column1 = xJ - xDelta
            x_column2 = xJ + xDelta + 1
            x_equal_columns = equal_columns(x_column1, x_column2)
            if not x_equal_columns:
                break
            if x_equal_columns == "out_of_range":
                return xJ + 1


def find_result_02(a):  # copypasting because i'm lazy...
    def row_differences(row1, row2):
        if 0 <= row1 < len(a) and 0 <= row2 < len(a):
            row_difference_count = 0
            for xI in range(len(a[row1])):
                if a[row1][xI] != a[row2][xI]:
                    row_difference_count += 1
            return row_difference_count
        else:
            return "out_of_range"
    def column_differences(col1, col2):
        if 0 <= col1 < len(a[0]) and 0 <= col2 < len(a[0]):
            s_col1 = ""
            s_col2 = ""
            column_difference_count = 0
            for xI in range(len(a)):
                s_col1 += a[xI][col1]
                s_col2 += a[xI][col2]
            for xI in range(len(s_col1)):
                if s_col1[xI] != s_col2[xI]:
                    column_difference_count += 1
            return column_difference_count
        else:
            return "out_of_range"
    for xJ in range(len(a) - 1):
        diff_count = 0
        for xDelta in range(len(a)):
            x_row1 = xJ - xDelta
            x_row2 = xJ + xDelta + 1
            x_equal_rows = row_differences(x_row1, x_row2)
            if x_equal_rows == "out_of_range":
                if diff_count == 1:
                    return (xJ + 1) * 100
                else:
                    break
            else:
                diff_count += x_equal_rows
    for xJ in range(len(a[0]) - 1):
        diff_count = 0
        for xDelta in range(len(a[0])):
            x_column1 = xJ - xDelta
            x_column2 = xJ + xDelta + 1
            x_equal_columns = column_differences(x_column1, x_column2)
            if x_equal_columns == "out_of_range":
                if diff_count == 1:
                    return xJ + 1
                else:
                    break
            else:
                diff_count += x_equal_columns

with open("day13_input.txt", 'r') as day13_file:
    day13_lines = day13_file.read().splitlines()

phase01_sum = 0
phase02_sum = 0
data = []
for day13_line in day13_lines:
    if day13_line == "":
        if len(data) == 0:
            continue
        else:
            phase01_sum += find_result_01(data)
            phase02_sum += find_result_02(data)
            data = []
            pass
    else:
        data.append(day13_line)
print("Phase 01 result:", phase01_sum)
print("Phase 02 result:", phase02_sum)
