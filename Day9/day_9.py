"""
advent of code 2022 - Day 9 (parts 1 & 2) [python3]

Author: Eugene Dupler
"""
events = [2, 10]
chain = list()

# Open our data file
input_file = "Day9/input_data.txt"
# input_file = "Day9/practice_data.txt"


class rope():
    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)
        self.move = {"U":self.U, "D":self.D, "L":self.L, "R":self.R}
        self.tail_trail = {f"{self.x} {self.y}":True}

    def R(self, val):
        self.x += int(val)

    def L(self, val):
        self.x -= int(val)

    def U(self, val):
        self.y += int(val)

    def D(self, val):
        self.y -= int(val)

    def mark_trail(self):
        self.tail_trail[f"{self.x} {self.y}"] = True
        return

    def tail_count(self):
        return len(self.tail_trail)


def main():
    global tails
    counter = 0
    for tails in events:
        counter += 1
        print(f"Event {counter} tail positions: {rope_count(tails)}")
        

def rope_count(tails):
    global data
    total_size = 0

    try:
        with open(input_file, 'r') as file:
            data = file.read().splitlines()
    except Exception as e:
        print(e)

    h_rope = rope()

    # Build the chain
    for index in range(tails):
        chain.append(rope())

    for line in data:
        [h_move_direction, h_move_distance] = line.split()[0:2]

        for step in range(int(h_move_distance)):
            move(h_move_direction)

    return chain[tails - 1].tail_count()


def move(direction, depth=0):
    global chain

    chain[depth].mark_trail()

    if depth == 0:
        chain[depth].move[direction](1)
    else:
        headx = chain[depth-1].x
        heady = chain[depth-1].y
        thisx = chain[depth].x
        thisy = chain[depth].y
        if (abs(thisx - headx) > 1) or (abs(thisy - heady) > 1):
            if thisy < heady:
                chain[depth].y += 1
            elif thisy > heady:
                chain[depth].y -= 1
            if thisx < headx:
                chain[depth].x += 1
            elif thisx > headx:
                chain[depth].x -= 1

    chain[depth].mark_trail()

    # Go to the next rope in the chain
    depth += 1
    if depth < len(chain):
        move(direction, depth)
    return


if __name__ == "__main__":
    main()
