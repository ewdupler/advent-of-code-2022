"""
advent of code 2022 - Day 4 (parts 1 & 2) [python3]

Author: Eugene Dupler
"""

def main():
    # Open our data file
    input_file = "Day4/input_data.txt"
    # input_file = "Day4/practice_data.txt"

    try:
        with open(input_file, 'r') as file:
            data = file.read().splitlines()
    except Exception as e:
        print(e)

    counter = {
        "full_subsets" : 0,
        "overlapped_sets": 0
    }
    
    for line in data:
        sets = list()
        # First split line on comma
        for data in line.split(","):
            # Now split on dash and form ranges that are turned into sets
            nums = data.split('-')
            sets.append(
                set(range(
                    int(nums[0]),
                    int(nums[1])+1
                ))
            )

        if sets[0].issubset(sets[1]) or sets[1].issubset(sets[0]):
            counter["full_subsets"] += 1
        if not sets[0].isdisjoint(sets[1]):
            counter["overlapped_sets"] += 1

    print(counter)


if __name__ == "__main__":
    main()

