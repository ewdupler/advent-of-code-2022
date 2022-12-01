"""
advent of code 2022 - Day 1 (parts 1 & 2)

Author: Eugene Dupler
"""


# Open our data file
input_file = "Day1/day_1.txt"

try:
    with open(input_file, 'r') as file:
        data = file.read().splitlines()
except Exception as e:
    print(e)


# Initialize elf results and calories
elf_sum = 0
results = [elf_sum]  # total carried by each elf represented as separate list elements

counter = 0

for line in data:
    if line.isnumeric():
        elf_sum += int(line)
        results[counter] = elf_sum
    else:
        # New elf represented by an empty line resets sum
        elf_sum = 0
        counter += 1
        results.append(elf_sum)
        
# Sort the list so we can figure out the max collected
results.sort()
print("Top elf: ", results[-1])
print("Top 3 elves: ", sum(results[-3:]))