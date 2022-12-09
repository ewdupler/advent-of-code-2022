"""
advent of code 2022 - Day 9 (parts 1 & 2) [python3]

Author: Eugene Dupler
"""
DAY=9
rope_lengths = [2, 10]  # lengths of "rope" for each round of the puzzle
rope_chain = list()  # Global variable used to track the individual "ropes"

# Open our data file
input_file = f"Day{DAY}/input_data.txt"
# input_file = f"Day{DAY}/practice_data.txt"  # Uncomment for practice data


class rope():
    """ Rope object

    Attributes:
    x (int), current coordinate on the horizontal plane
    y (int), current coordinate on the vertical plane
    tail_trail (dict), dictionary of unique x/y coordinates occupied by this object at any time
    move (dict), list of move functions that can be invoked through this object

    Methods:
    U: # increment y by one
    D: # decrement y by one
    L: # decrement x by one
    R: # increment x by one
    mark_trail: # Record current position in tail_trail attribute
    tail_count: # Return current count of entries in tail_trail 
    """
    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)
        self.tail_trail = {f"{self.x} {self.y}":True}
        self.move = {"U":self.U, "D":self.D, "L":self.L, "R":self.R}


    # Movement functions (Right, Left, Up, Down)
    def R(self, val): self.x += int(val)
    def L(self, val): self.x -= int(val)
    def U(self, val): self.y += int(val)
    def D(self, val): self.y -= int(val)

    # Marking the trail
    def mark_trail(self):
        self.tail_trail[f"{self.x} {self.y}"] = True
        return

    # Counting marks on the trail
    def tail_count(self):
        return len(self.tail_trail)


def main():
    """ Return a count of visited paths for each rope chain of objects specified in rope_lengths """

    with open(f"Day{DAY}/output.txt", "w") as outfile:
        counter = 0
        for tails in rope_lengths:
            counter += 1
            output(f"Event {counter} tail positions: {rope_count(tails)}", outfile)
        

def output(output_line, fh):
    """ Send output to both the output.txt file and to stdout"""
    print(output_line)
    fh.write(output_line + "\n")


def rope_count(tails):
    """ Manipulate rope object movement and return a count of visited coordinates
    
    Keyword arguments:
    1. tails (int)  # represents length of linked chain of objects to create and manipulate

    Returns: (int)  # count of visited coordinates of the last element in the rope chain
    """
    try:
        with open(input_file, 'r') as file:
            data = file.read().splitlines()
    except Exception as e:
        print(e)

    # Build the rope_chain
    for index in range(tails):
        rope_chain.append(rope())

    for line in data:
        [h_move_direction, h_move_distance] = line.split()[0:2]

        for step in range(int(h_move_distance)):
            move(h_move_direction)

    return rope_chain[tails - 1].tail_count()


def move(direction, depth=0):
    """ Move a rope object in a direction by one unit

    Keyword arguments:
    1. direction (required), one of: L, R, U, D  # left, right, up or down
    2. depth (optional), (int)  # default = 0; represents depth in a recursively linked chain of objects

    Returns: None
    """
    global rope_chain

    rope_chain[depth].mark_trail()

    if depth == 0:
        rope_chain[depth].move[direction](1)
    else:
        headx = rope_chain[depth-1].x
        heady = rope_chain[depth-1].y
        thisx = rope_chain[depth].x
        thisy = rope_chain[depth].y
        if (abs(thisx - headx) > 1) or (abs(thisy - heady) > 1):
            if thisy < heady:
                thisy += 1
            elif thisy > heady:
                thisy -= 1
            if thisx < headx:
                thisx += 1
            elif thisx > headx:
                thisx -= 1

            # Set object values
            rope_chain[depth].x = thisx
            rope_chain[depth].y = thisy

    rope_chain[depth].mark_trail()  # Mark the path of this rope

    ## RECURSION ##
    # Go to the next rope in the chain
    depth += 1
    if depth < len(rope_chain):
        move(direction, depth)

    return


if __name__ == "__main__":
    main()
