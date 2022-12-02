#!/usr/bin/perl

open(x,"<Day1/input_data.txt"); while (<x>) {
    /^$/ && $n++ && ($e[$n] = 0);
    $e[$n] += $_;
}; @s = sort { $a <=> $b } @e;
foreach (@s[-3..-1]) {$x+=$_}; print(@s[-1]."\n$x\n");