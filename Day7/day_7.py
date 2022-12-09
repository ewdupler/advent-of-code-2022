"""
advent of code 2022 - Day 7 (parts 1) [python3]

Author: Eugene Dupler
"""
data = list()
dirsizes = dict()
GOAL=30000000
MAX=70000000

def main():
    global data
    total_size = 0

    # Open our data file
    input_file = "Day7/input_data.txt"
    # input_file = "Day7/practice_data.txt"

    try:
        with open(input_file, 'r') as file:
            data = file.read().splitlines()
    except Exception as e:
        print(e)

    thisdir=""
    files = {}

    for line in data:
        name = line.split(" ")[-1]
        size = line.split(" ")[0]

        if "$ ls" in line:
            continue

        if "$ cd " in line:
            if name == "..":
                thisdir = "/".join(thisdir.split("/")[0:-2])
                if not thisdir.startswith("/"):
                    thisdir = "/"+thisdir
                if not thisdir.endswith("/"):
                    thisdir = thisdir+"/"
                # print("THISDIR",thisdir)
            
            else:
                if name == "/":
                    thisdir = "/"
                else:
                    thisdir += name + "/"
        elif size.isnumeric():
            size = int(size)
            file = thisdir + name
            filldir(thisdir, size)
            total_size += size
            # print("FOUND",thisdir,size)

    sum_most_100000 = 0
    sortedsizes = dict(sorted(dirsizes.items(), key=lambda item: item[1]))
    for size in sortedsizes.values():
        if size <= 100000:
            sum_most_100000 += size

    bigdir=0
    target = GOAL - (MAX - total_size)
    for dir in sortedsizes:
        if sortedsizes[dir] >= target:
            bigdir = sortedsizes[dir]
            break
    print("Sum at most 100000: ",sum_most_100000)
    print("Delete dir size: ", bigdir)



def filldir(directory, size=0):
    global dirsizes
    
    curdir = "/"
    try:
        dirsizes[curdir]
        dirsizes[curdir] += size
    except:
        dirsizes[curdir] = size

    for subdir in directory.split('/'):
        if subdir == "":
            continue
        curdir += subdir + "/"
        try:
            dirsizes[curdir]
            dirsizes[curdir] += size
        except:
            dirsizes[curdir] = size

    pass
     


if __name__ == "__main__":
    main()
