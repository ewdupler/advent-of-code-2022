#!/usr/bin/perl
##
# advent of code 2022 - Day 1 (parts 1 & 2) [perl]
##
#
# Author: Eugene Dupler

$INFILE = "Day1/input_data.txt";

open(INFILE, "<$INFILE") || die("Could not open $INFILE");
@data = <INFILE>;
close(INFILE);

$sum = 0;
for $line (@data) {
    if ($line =~ /^$/) {
        push @sum, $sum;
        $sum = 0;
    } else {
        $sum += $line;
    }
}

@sum = sort { $a <=> $b } @sum;

$top = $sum[-1];
$top3 = 0;
for $num (@sum[-3..-1]) {
    $top3 += $num
}

print("Top Elf:\t$top\n");
print("Top 3 elves:\t$top3\n");