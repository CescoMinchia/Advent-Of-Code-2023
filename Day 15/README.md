# Source
Day 15 challenge here: https://adventofcode.com/2023/day/15

# Instructions
- From the input, process each string to obtain a number
- Sum all these numbers
  
# Detailed
The input is a sequence of comma-separated strings.
Given a string, it is processed character by character to give a number.

## Algorithm
For each string, process character by character.\
Perform the below steps for each character.
```
1 - Start from a current value of 0
2 - Determine the ASCII code for the current character of the string.
3 - Increase the current value by the ASCII code you just determined.
4 - Set the current value to itself multiplied by 17.
5 - Set the current value to the remainder of dividing itself by 256.

Start this sequence of steps again, but use the new current value instead of 0 in the first step.
```
After the last character has been processed, the value obtained is the answer for this challenge.

## Example 1:
This input consists of 1 string:
HASH

The current value starts at 0.\
The first character is H; its ASCII code is 72.\
The current value increases to 72.\
The current value is multiplied by 17 to become 1224.\
The current value becomes 200 (the remainder of 1224 divided by 256).\
The next character is A; its ASCII code is 65.\
The current value increases to 265.\
The current value is multiplied by 17 to become 4505.\
The current value becomes 153 (the remainder of 4505 divided by 256).\
The next character is S; its ASCII code is 83.\
The current value increases to 236.\
The current value is multiplied by 17 to become 4012.\
The current value becomes 172 (the remainder of 4012 divided by 256).\
The next character is H; its ASCII code is 72.\
The current value increases to 244.\
The current value is multiplied by 17 to become 4148.\
The current value becomes 52 (the remainder of 4148 divided by 256).\
So, the result of running the HASH algorithm on the string HASH is 52.

## Example 2
This example has 11 strings to be processed.\
Input:\
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7

rn=1 becomes 30.\
cm- becomes 253.\
qp=3 becomes 97.\
cm=2 becomes 47.\
qp- becomes 14.\
pc=4 becomes 180.\
ot=9 becomes 9.\
ab=5 becomes 197.\
pc- becomes 48.\
pc=6 becomes 214.\
ot=7 becomes 231.\

In this example, the sum of these results is 1320.
