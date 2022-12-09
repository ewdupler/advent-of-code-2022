"""
advent of code 2022 - Day 8 (parts 1) [python3]

Author: Eugene Dupler
"""


def main():
    global data
    total_size = 0

    # Open our data file
    input_file = "Day8/input_data.txt"
    # input_file = "Day8/practice_data.txt"

    try:
        with open(input_file, 'r') as file:
            data = file.read().splitlines()
    except Exception as e:
        print(e)

    interior_tree_count = 0
    exterior_tree_count = (len(data) * 2) + (len(data[0] * 2) - 4)  # -4 to subtract corners; don't count twice

    linecount = 1
    for line in data[1:-1]:  # Evaluate interior trees only
        for index in range(len(line)):
            if (index == len(line)-1) or (index == 0):
                continue
            if side_check(line, index):
                interior_tree_count += 1
            else:
                if (updown_check(data, linecount, index)):
                    interior_tree_count += 1

        linecount += 1


    max_view = 0
    for line_index in range(len(data)):
        for tree_index in range(len(data[0])):
            this_tree_height = int(data[line_index][tree_index])

            # Left View
            left_view = 0
            for left_tree_index in range(tree_index-1,-1,-1):
                if int(data[line_index][left_tree_index]) < int(data[line_index][tree_index]):
                    left_view += 1
                elif int(data[line_index][left_tree_index]) == int(data[line_index][tree_index]):
                    left_view += 1
                    break


            # Right View
            right_view = 0
            for right_tree_index in range(tree_index+1,len(data[line_index])):
                if int(data[line_index][right_tree_index]) < int(data[line_index][tree_index]):
                    right_view += 1
                elif int(data[line_index][right_tree_index]) == int(data[line_index][tree_index]):
                    right_view += 1
                    break


            # Up View
            up_view = 0
            for up_tree_index in range(line_index-1,-1,-1):
                if int(data[up_tree_index][tree_index]) < int(data[line_index][tree_index]):
                    up_view += 1
                elif int(data[up_tree_index][tree_index]) == int(data[line_index][tree_index]):
                    up_view += 1
                    break

            
            # Down View
            down_view = 0
            for down_tree_index in range(line_index+1,len(data)):
                if int(data[down_tree_index][tree_index]) < int(data[line_index][tree_index]):
                    down_view += 1
                elif int(data[down_tree_index][tree_index]) == int(data[line_index][tree_index]):
                    down_view += 1
                    break
            
            
            this_view = up_view * down_view * left_view * right_view

            if this_view > max_view:
                max_view = this_view

    print("Visible Trees: ", exterior_tree_count + interior_tree_count)
    print("max view: ", max_view)

def updown_check(all_lines, current_line, line_index):
    visible = up_visible = down_visible = True

    this_tree_height = int(all_lines[current_line][line_index])

    for tree_above in all_lines[:current_line]:
        if int(tree_above[line_index]) >= this_tree_height:
            up_visible = False
            break

    for tree_below in all_lines[current_line+1:]:
        if int(tree_below[line_index]) >= this_tree_height:
            down_visible = False
            break

    visible = up_visible or down_visible
    
    return visible


def side_check(line, tree_index):

    visible = left_visible = right_visible = True

    this_tree_height = int(line[tree_index])

    row = [int(x) for x in line]

    for tree_right in row[tree_index+1:]:
        if this_tree_height <= tree_right:
            right_visible = False
            break

    for tree_left in row[0:tree_index]:
        if this_tree_height <= tree_left:
            left_visible = False
            break

    visible = left_visible or right_visible
    
    return visible


if __name__ == "__main__":
    main()
