"""
advent of code 2022 - Day 2 (parts 1 & 2) [python3]

Author: Eugene Dupler
"""

def main():
    # Open our data file
    input_file = "Day2/input_data.txt"


    points1 = {
        'A': { 'X':3, 'Y':6, 'Z':0 },
        'B': { 'X':0, 'Y':3, 'Z':6 },
        'C': { 'X':6, 'Y':0, 'Z':3 },
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    points2 = {
        'A': { 'X':3, 'Y':1, 'Z':2 },
        'B': { 'X':1, 'Y':2, 'Z':3 },
        'C': { 'X':2, 'Y':3, 'Z':1 },
        'X': 0,
        'Y': 3,
        'Z': 6
    }

    try:
        with open(input_file, 'r') as file:
            data = file.read().splitlines()
    except Exception as e:
        print(e)

    score1 = score2 = 0
    for line in data:
        (p1, p2) = line.split()
        score1 += points1[p1][p2] + points1[p2]
        score2 += points2[p1][p2] + points2[p2]

    print("score1", score1)
    print("score2", score2)
    

if __name__ == "__main__":
    main()
