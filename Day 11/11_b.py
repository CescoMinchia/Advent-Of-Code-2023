import os

def open_file_in_same_directory(file_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)

    with open(file_path, 'r') as file:
        content = file.read()

    return content
    
content = open_file_in_same_directory("input.txt")

map_universe = []

REAL_EXPANSION = 1000000

for n,row in enumerate(content.split('\n'),0):
    map_universe.append(list(row))

no_galaxies_row = []
for n,i in enumerate(map_universe):
    if "#" in i:
        continue
    no_galaxies_row.append(n)

no_galaxies_col = []
for n,i in enumerate(zip(*map_universe)):
    if "#" in i:
        continue
    no_galaxies_col.append(n)

d_coords = {}
n = 0
for r,i in enumerate(map_universe):
    for c,j in enumerate(i):
        if j == '#':
            d_coords[n] = (r,c)
            n += 1

from itertools import combinations
 
all_pairs = list(combinations(list(d_coords.keys()), 2))

def calculate_distance(obj_1,obj_2):
    x1,y1 = d_coords[obj_1]
    x2,y2 = d_coords[obj_2]

    not_expanded_d_x = abs(x2-x1)
    not_expanded_d_y = abs(y2-y1)

    real_d_x = not_expanded_d_x
    for i in range(min(x1+1,x2+1),max(x1+1,x2+1)):
        if i in no_galaxies_row:
            real_d_x += REAL_EXPANSION - 1

    real_d_y = not_expanded_d_y
    for i in range(min(y1+1,y2+1),max(y1+1,y2+1)):
        if i in no_galaxies_col:
            real_d_y += REAL_EXPANSION - 1

    return(real_d_x+real_d_y)

total = 0
for i,j in all_pairs:
    # print(f"({i},{j}): {calculate_distance(i,j)}")
    total += calculate_distance(i,j)

print(total)