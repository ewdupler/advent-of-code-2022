#!/bin/bash
##
# advent of code 2022 - Day 1 (parts 1 & 2) [bash]
##
#
# Author: Eugene Dupler

input_file="Day2/input_data.txt"

# Pre-calculate pattern values
changes1="
-e 's/A X/4%3/'
-e 's/A Y/8%4/'
-e 's/A Z/3%8/'
-e 's/B X/1%1/'
-e 's/B Y/5%5/'
-e 's/B Z/9%9/'
-e 's/C X/7%2/'
-e 's/C Y/2%6/'
-e 's/C Z/6%7/'
"

# Use sed to change patterns to numbers, then split each column to add up
for line in $(eval sed $changes1 $input_file); do
    p1=$(echo $line | cut -d% -f1)
    p2=$(echo $line | cut -d% -f2)
    let s1+=$p1
    let s2+=$p2
done

echo "score1" $s1
echo "score2" $s2