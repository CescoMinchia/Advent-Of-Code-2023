# Source 
Day 8 challenge here: https://adventofcode.com/2023/day/8

# Instructions
- Following the instructions, count the number of steps to reach the target location.
- The number of step is the answer for this challenge
  
# Detailed
The input consists of two part. The first line is a string, a sequence of letters "R" and "L", which stand respectively for "right" and "left". This string is the instructions we have to follow for the next part of the input.

The second part of the input is a list of coordinates, and the locations they can access.\
Example:
```
AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
```
The first location "AAA" can access "BBB" (second line), and "CCC" (third line).
The second location "BBB" can access "DDD" (fourth line), and "GGG" (sixth line).
You have to count the number of steps to reach "ZZZ".

With this example:
```
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
```

Starting with AAA, you need to look up the next element based on the next left/right instruction in your input. In this example, start with AAA and go right (R) by choosing the right element of AAA, CCC. Then, L means to choose the left element of CCC, ZZZ. By following the "RL" instruction, you reach ZZZ in 2 steps.
2 is the answer for this example. 

With this second example you reach the "ZZZ" in 6 steps (answer of the following example):
```
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
```
(LLR is read again when you reach the end of the instruction. In other words:
LLR = LLRLLRLLRLLRLLR...)
