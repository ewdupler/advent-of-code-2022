"""
advent of code 2022 - Day 12 (parts 1 & 2) [python3]

Author: Eugene Dupler
"""
import string
DAY=12

# Our files
output_file = f"Day{DAY}/output.txt"
input_file = f"Day{DAY}/input_data.txt"
input_file = f"Day{DAY}/practice_data.txt"  # Uncomment for practice data

class Path:
    def __init__(self, location, content="", visited=False):
        self.x = location[0]
        self.y = location[1]
        self.location = location
        self.path    = [self.location]
        self.length  = 0
        self.level   = 1
        self.content = content
        self.visited = visited


def main():
    output()

    input_data = get_data()

    # Map grid as a list of lists
    cell = []
    grid = input_data
    for y in range(len(grid)):
        cell.append([])
        for x in range(len(grid[y])):
            cell[int(y)].append(x)
            cell[int(y)][int(x)] = Path([int(x), int(y)], content=grid[y][x])

    print_grid(grid)

    start = find_square(grid, 'S')
    goal = find_square(grid, 'E')


    start_cell = cell[start[0]][start[1]]

    navigate(start_cell, cell)

    for y in range(len(grid)):
        cell.append([])
        for x in range(len(grid[y])):
            print(cell[int(y)][int(x)].level)


def navigate(this, grid):
    x = this.location[0]
    y = this.location[1]

    this.level += 1
    this_cell_value = letter_val(this.content)
    if this_cell_value == -1 and not this.content == 'S':
        return

    # check left
    if x > 0:
        newx = x-1
        newy = y
        if not grid[newy][newx].visited and (abs(letter_val(grid[newy][newx].content) - this_cell_value) <= 1):
            print(newx, newy)
            grid[newy][newx].visited = True
            grid[newy][newx].path.append([newx, newy])
            navigate(grid[newy][newx], grid)
        elif grid[newy][newx].content == 'E':
            print("FOUND")
            return

    # check right
    if x < (len(grid[0]) - 1):
        newx = x+1
        newy = y
        if not grid[newy][newx].visited and (abs(letter_val(grid[newy][newx].content) - this_cell_value) <= 1):
            print(newx, newy)
            grid[newy][newx].visited = True
            grid[newy][newx].path.append([newx, newy])
            navigate(grid[newy][newx], grid)
        elif grid[newy][newx].content == 'E':
            print("FOUND")
            return    # check top
    if y > 0:
        newx = x
        newy = y-1
        if not grid[newy][newx].visited and (abs(letter_val(grid[newy][newx].content) - this_cell_value) <= 1):
            print(newx, newy)
            grid[newy][newx].visited = True
            grid[newy][newx].path.append([newx, newy])
            navigate(grid[newy][newx], grid)
        elif grid[newy][newx].content == 'E':
            print("FOUND")
            return   # check bottom
    if y < (len(grid) - 1):
        newx = x
        newy = y+1
        if not grid[newy][newx].visited and (abs(letter_val(grid[newy][newx].content) - this_cell_value) <= 1):
            print(newx, newy)
            grid[newy][newx].visited = True
            grid[newy][newx].path.append([newx, newy])
            navigate(grid[newy][newx], grid)
        elif grid[newy][newx].content == 'E':
            print("FOUND")
            return

def letter_val(letter):
    return int(string.ascii_lowercase.find(letter))
    # return letter

def print_grid(grid):
    for line in grid: print(line)

def find_square(grid, letter):
    retval = [-1, -1]
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if letter in grid[y][x]:
                retval = [x, y]
    return retval


def output(output_line=None):
    """ Send output to both the output.txt file and to stdout"""
    
    if output_line == None:
        with open(output_file, "w") as fh:
            pass
    else:
        print(output_line)

        with open(output_file, "a") as fh:
            fh.write(output_line + "\n")


def get_data():
    try:
        with open(input_file, 'r') as file:
            data = file.read().splitlines()
    except Exception as e:
        print(e)

    return data


if __name__ == "__main__":
    main()
