"""
advent of code 2022 - Day 9 (parts 1 & 2) [python3]

Author: Eugene Dupler
"""
DAY=10
cycle_register = []
INTERESTING_CYCLES = [20, 60, 100, 140, 180, 220]
pixel_grid = [[]]

# Our files
output_file = f"Day{DAY}/output.txt"
input_file = f"Day{DAY}/input_data.txt"
# input_file = f"Day{DAY}/practice_data.txt"  # Uncomment for practice data


def main():
    output()

    input_data = get_data()
    last = 1

    line_number = list([])  # each element is a row on the screen
    counter = 0

    for line in input_data:
        if "addx" in line:
            addx = int(line.split(" ")[-1])
            cycle_register.append(last)
            set_pixel(counter, cycle_register[-1])
            counter += 1

            cycle_register.append(last)
            last += addx
            set_pixel(counter, cycle_register[-1])
            counter += 1
        elif "noop" in line:
            cycle_register.append(last)
            set_pixel(counter, cycle_register[-1])
            counter += 1

    total_strength = 0

    for cycle_number in INTERESTING_CYCLES:
        strength = cycle_number * cycle_register[cycle_number -1]
        total_strength += strength


    output(f"The sum of these signal strengths is {total_strength}.")
    output("")

    for line in pixel_grid:
        output(''.join(line))


def output(output_line=None):
    """ Send output to both the output.txt file and to stdout"""
    
    if output_line == None:
        with open(output_file, "w") as fh:
            pass
    else:
        print(output_line)

        with open(output_file, "a") as fh:
            fh.write(output_line + "\n")


def set_pixel(counter, last):
        global pixel_grid
        
        row = (counter) // 40
        column = (counter) % 40

        if ((column == last-1) or
            (column == last) or
            (column == last+1)):
            pixel_grid[row].append("#")
        else:
            pixel_grid[row].append(".")
        if column == 39:
            pixel_grid.append([])

def get_data():
    try:
        with open(input_file, 'r') as file:
            data = file.read().splitlines()
    except Exception as e:
        print(e)

    return data


if __name__ == "__main__":
    main()
