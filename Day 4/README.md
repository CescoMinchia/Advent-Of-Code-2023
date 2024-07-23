# Source
Day 4 challenge here: https://adventofcode.com/2023/day/4

# Instructions
- For each line, get the number of matches and equivalent points
- Sum the points obtained for each line
  
# Detailed
Input consists of multiple lines, and each of them has 2 groups of respectively 5  and 8 numbers. We check which numbers from the first group appear in the second.
The first match is worth 1 point, and each subsequent one double the current points.\
In other words: $points = 2^{n-1}$\
where $n > 0$ is the number of match of that line.\
Input example:
```
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
```
-Card 1 has four winning numbers (48, 83, 17, and 86), so it is worth 8 points (1 for the first match, then doubled three times for each of the three matches after the first)\
-Card 2 has two winning numbers (32 and 61), so it is worth 2 points.\
-Card 3 has two winning numbers (1 and 21), so it is worth 2 points.\
-Card 4 has one winning number (84), so it is worth 1 point.\
-Card 5 has no winning numbers, so it is worth no points.\
-Card 6 has no winning numbers, so it is worth no points.

Therefore, for this example, the answer is 13.
