# Source
Day 16 challenge here: https://adventofcode.com/2023/day/16

# Instructions
- Get the path of the beam
- Count the number of squares where the beam irradiates, including other objects
  
# Detailed
An input consists of a two-dimensional square grid containing empty space (.), mirrors (/ and \), and splitters (| and -).

Input example:
```
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
```

The beam enters in the top-left corner from the left and heading to the right. Then, its behavior depends on what it encounters as it moves:

- If the beam encounters empty space (.), it continues in the same direction.
- If the beam encounters a mirror (/ or \), the beam is reflected 90 degrees depending on the angle of the mirror. For instance, a rightward-moving beam that encounters a / mirror would continue upward in the mirror's column, while a rightward-moving beam that encounters a \ mirror would continue downward from the mirror's column.
- If the beam encounters the pointy end of a splitter (| or -), the beam passes through the splitter as if the splitter were empty space. For instance, a rightward-moving beam that encounters a - splitter would continue in the same direction.
- If the beam encounters the flat side of a splitter (| or -), the beam is split into two beams going in each of the two directions the splitter's pointy ends are pointing. For instance, a rightward-moving beam that encounters a | splitter would split into two beams: one that continues upward from the splitter's column and one that continues downward from the splitter's column.

This is what we get:
```
>|<<<\....
|v-.\^....
.v...|->>>
.v...v^.|.
.v...v^...
.v...v^..\
.v../2\\..
<->-/vv|..
.|<<<2-|.\
.v//.|.v..
```

The answer of the challenge, is the number of squares irradiated by the beam (including any mirror and splitter)

This is the same example, where a "#" symbol has been used to show where the beam is:

```
######....
.#...#....
.#...#####
.#...##...
.#...##...
.#...##...
.#..####..
########..
.#######..
.#...#.#..
```

We have 46 "#" symbols, which is the answer for this example.
