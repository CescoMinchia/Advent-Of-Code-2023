import os

def open_file_in_same_directory(file_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)

    with open(file_path, 'r') as file:
        content = file.read()

    return content
    
content = open_file_in_same_directory("input.txt")

def parse_input(text):
    import re
    inst = re.search("(L|R)+", text).group(0).strip()

    coords = [i for i in text.replace(inst,"").strip().split("\n")]
    # create dictionary
    keys = [i.split("=")[0].strip() for i in coords]
    values = [tuple(re.findall("[0-9a-zA-Z]+", i.split("=")[1].strip())) for i in coords]
    d = dict(zip(keys, values)) 
    coords_map = {}
    for k,v in d.items():
        x,y = v
        coords_map[(k,"L")] = x
        coords_map[(k,"R")] = y
    return inst, coords_map

inst, coords_map = parse_input(content)

from itertools import cycle
c=0
pos = list(set([k[0]  for k,v in coords_map.items() if k[0][-1] == "A"]))
pos.sort()
print(pos)

# check how long it taks before returning to same position
c=0
c_list = []
pos=['AAA', 'DVA', 'FJA', 'MPA', 'TDA', 'XPA']

for p in pos:
    starting_p = p
    for i in cycle(list(inst)):
     
        p = coords_map[(p,i)]

        c+=1

        if(p[-1] == "Z"):
            c_list.append(c)
            c = 0
            break

# import math
print(c_list)

# then you have to find the minimum multiple between numbers (the least number that is a multiple of all the numbers)
# done it online (with a built-in calculator)