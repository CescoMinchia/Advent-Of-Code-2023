# Source
Day 14 challenge here: https://adventofcode.com/2023/day/14

# Instructions
- Roll all the rocks by north
- Get the total amount of load
  
# Detailed
We have a lever that can be tilted along the 4 cardinal directions.\
Each round we select 1 of the directions and all the rocks ("O" symbols) will shift by that direction until they are blocked.\
They can be blocked by a cube-shaped rock ("#" symbols) or a wall (perimeter)

Example:\
Given an input as below:
```
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
```

If we select north, this is what we get:
```
OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#....
```

The amount of load caused by a single rounded rock (O) is equal to the number of rows from the rock to the south edge of the platform, including the row the rock is on.
```
OOOO.#.O.. 10
OO..#....#  9
OO..O##..O  8
O..#.OO...  7
........#.  6
..#....#.#  5
..O..#.O.O  4
..O.......  3
#....###..  2
#....#....  1
```
That is: 5 x 10+2 x 9+4 x 8+3 x 7+4 x 3+3 = 136.\
In this example, 136 is the correct answer to this challenge.
