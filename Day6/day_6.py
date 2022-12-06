"""
advent of code 2022 - Day 5 (parts 1) [python3]

Author: Eugene Dupler
"""
columns = list()
stacks = list()

def main():
    # Open our data file
    input_file = "Day6/input_data.txt"
    # input_file = "Day6/practice_data.txt"

    try:
        with open(input_file, 'r') as file:
            data = file.read().splitlines()
    except Exception as e:
        print(e)

    for line in data:
        print("Code start: ", scan_line(line))
        print("Message start: ", scan_line(line, 14))

def scan_line(line, marker_length=4):
    for index in range(marker_length-1, len(line)):
        unique_line = set(line[index-marker_length:index])
        if len(unique_line) == marker_length:
            break
    return index


if __name__ == "__main__":
    main()
