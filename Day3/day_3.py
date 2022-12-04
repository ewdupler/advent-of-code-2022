"""
advent of code 2022 - Day 3 (parts 1 & 2) [python3]

Author: Eugene Dupler
"""

def main():
    # Open our data file
    input_file = "Day3/input_data.txt"

    try:
        with open(input_file, 'r') as file:
            data = file.read().splitlines()
    except Exception as e:
        print(e)

    sum=0

    for line in data:
        half = len(line)//2
        p1 = line[0:half]
        p2 = line[half:]
        sum += letterval(dchar(p1,p2))

    print(f"sum1: {sum}")

    c = 0
    sum = 0
    for n in range(len(data)//3):
        letter = dchar3(data[c], data[c+1], data[c+2])
        c += 3
        sum += letterval(letter)

    print(f"sum2: {sum}")

def dchar(s1, s2):
    for letter in s1:
        if letter in s2:
            return letter

def dchar3(s1, s2, s3):
    for letter in s1:
        if letter in s2 and letter in s3:
            return letter            

def letterval(letter):
    import string
    return str(" " + string.ascii_lowercase + string.ascii_uppercase).find(letter)

if __name__ == "__main__":
    main()
