#!/usr/bin/perl
##
# advent of code 2022 - Day 2 (parts 1 & 2) [perl]
##
#
# Author: Eugene Dupler

$INFILE = "Day2/input_data.txt";

open(INFILE, "<$INFILE") || die("Could not open $INFILE");
@data = <INFILE>;
close(INFILE);

$s1 = $s2 = 0;

# Detect patterns and add values
foreach (@data) {
    if (/A X/) { $s1+=4 ; $s2+=3 };
    if (/A Y/) { $s1+=8 ; $s2+=4 };
    if (/A Z/) { $s1+=3 ; $s2+=8 };
    if (/B X/) { $s1+=1 ; $s2+=1 };
    if (/B Y/) { $s1+=5 ; $s2+=5 };
    if (/B Z/) { $s1+=9 ; $s2+=9 };
    if (/C X/) { $s1+=7 ; $s2+=2 };
    if (/C Y/) { $s1+=2 ; $s2+=6 };
    if (/C Z/) { $s1+=6 ; $s2+=7 };
}

print("score1 " .$s1."\n");
print("score2 ".$s2."\n");