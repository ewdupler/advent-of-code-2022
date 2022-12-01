#!/bin/bash
##
# advent of code 2022 - Day 1 (parts 1 & 2) [bash]
##
#
# Author: Eugene Dupler

infile="Day1/input_data.txt"
TMPFILE="/tmp/$(basename $0).$$"

cat $infile | while read line; do
    if [ "$(echo $line | grep '[0-9]')" ]; then
        let sum+=$line
    else
        echo $sum
        sum=0
    fi
done | sort -n > "${TMPFILE}"

top=$(tail -1 ${TMPFILE})
top3=0
for num in $(tail -3 ${TMPFILE}); do
    let top3+=$num
done

echo "Top Elf:  ${top}"
echo "Top 3 elves:  ${top3}"

rm -f "${TMPFILE}"