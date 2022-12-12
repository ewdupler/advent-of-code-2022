"""
advent of code 2022 - Day 11 (parts 1 & 2) [python3]

Author: Eugene Dupler
"""
DAY=11

# Our files
output_file = f"Day{DAY}/output.txt"
input_file = f"Day{DAY}/input_data.txt"
# input_file = f"Day{DAY}/practice_data.txt"  # Uncomment for practice data

class monkey_class():
    def __init__(self, id):
        self.items = []
        self.id = id
        self.operator = "*"
        self.opvalue = 0
        self.test = 0
        self.true_monkey = 0
        self.false_monkey = 0
        self.inspection_count = 0
        self.operate = {"+":self.add, "*":self.mult}

    def add(self, thisitem):
        return thisitem + int(self.opvalue)

    def mult(self, thisitem):
        if self.opvalue == "old":
            retval = thisitem * thisitem
        else:
            retval = thisitem * int(self.opvalue)

        return retval


def main():
    output()

    input_data = get_data()
    last = 1

    line_number = list([])  # each element is a row on the screen
    counter = 0

    monkey = list()
    maxtest = 1
    for line in input_data:
        if "Monkey" in line:
            monkey_num = int(line.split(" ")[-1].split(":")[0])
            monkey.append([])
            monkey[monkey_num] = monkey_class(monkey_num)
            # monkey[monkey_num].id = monkey_num
        if "Starting " in line:
            for number in (line.split(":")[-1]).split(','):
                monkey[monkey_num].items.append(int(number))
        if "Test:" in line:
            monkey[monkey_num].test = line.split(" ")[-1]
            maxtest *= int(monkey[monkey_num].test)
        if "Operation: " in line:
            monkey[monkey_num].operator = line.split(" ")[-2]
            monkey[monkey_num].opvalue  = (line.split(" ")[-1])
        if "If true:" in line:
            monkey[monkey_num].true_monkey = line.split(" ")[-1]
        if "If false:" in line:
            monkey[monkey_num].false_monkey = line.split(" ")[-1]


    # Part 1 and part 2
    solutions = {20:3, 10000:1}

    this_round = 0
    for rounds in solutions:
        this_round += 1
        divisor = solutions[rounds]
        for round in range(rounds):
            for monkey_num in range(len(monkey)):
                this = monkey[monkey_num]
                # print(f"Monkey {this.id}")

                for item in this.items:

                    monkey[this.id].inspection_count += 1

                    worry_level = this.operate[this.operator](item)
                    
                    # Modulo trick for manageable integers
                    divided_by_three = (worry_level % maxtest) // divisor

                    if (divided_by_three % int(this.test)) == 0:
                        send_to = this.true_monkey
                        divisible = "divisible"
                    else:
                        send_to = this.false_monkey
                        divisible = "not divisible"

                    # Throw the item
                    monkey[int(send_to)].items.append(divided_by_three)

                # Reset monkey list
                monkey[this.id].items = []

        active_monkeys = list()
        for counter in range(len(monkey)):
            active_monkeys.append(monkey[counter].inspection_count)

        active_monkeys = sorted(active_monkeys)

        output(f"Part {this_round} monkey business is {active_monkeys[-2] * active_monkeys[-1]}")


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
