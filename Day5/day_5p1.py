"""
advent of code 2022 - Day 5 (parts 1) [python3]

Author: Eugene Dupler
"""
columns = list()
stacks = list()

def main():
    # Open our data file
    input_file = "Day5/input_data.txt"
    # input_file = "Day5/practice_data.txt"

    global columns
    global stacks



    for type in ["9000", "9001"]:
        stacks = list()
        columns = list()
        try:
            with open(input_file, 'r') as file:
                data = file.read().splitlines()
        except Exception as e:
            print(e)
        
        counter = 0
        
        for line in data:
            if line == "":
                stacks = build_stacks(counter, data)
                break
            else:
                counter += 1
        counter += 1
        
        for line in data[counter:]:
            instructions = line.split(" ")
            qty = int(instructions[1])
            frm = int(instructions[3])
            dst = int(instructions[5])
            move_boxes(type, qty, frm, dst)

        print("Type: ",type, "Code: ", top_boxes(stacks))



def top_boxes(stack_p):
    code = ""
    for stack in stack_p:
        code += stack.pop()
    return code


def move_boxes(type, quantity, start, end):
    global stacks
    
    if type == "9001":
        group = stacks[start-1][-1 * quantity:]
        # print(group, quantity, start, end)
        for index in range(quantity):
            stacks[start-1].pop()
        for box in group:
            stacks[end-1].append(box)
    else:
        for index in range(quantity):
            box = stacks[start-1].pop()
            stacks[end-1].append(box)

def build_stacks(counter, data):
    counter -= 1
    header = data[counter]
    index=0
    global columns
    for char in header:
        if char != " ":
            # print(index, char)
            columns.append(index)
        index += 1
    # print(columns)

    stacks = list()
    for index in range(len(columns)):
        stacks.append([])
    while counter > 0:
        counter -= 1
        stack = 0
        for index in columns:
            if data[counter][index] != " ":
                stacks[stack].append(data[counter][index])
            stack += 1
    return stacks


if __name__ == "__main__":
    main()

