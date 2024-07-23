import os

def open_file_in_same_directory(file_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)

    with open(file_path, 'r') as file:
        content = file.read()

    return content
    
content = open_file_in_same_directory("input.txt")

def get_previous_n(list_n):
    if len(set(list_n)) == 1:
        return list_n[0]
    else:
        return list_n[0] - get_previous_n([list_n[i]-list_n[i-1] for i in range(1,len(list_n))])

tot = 0
for i in content.split("\n"):
    numbs = [int(n) for n in i.split(" ")]
    res = get_previous_n(numbs)
    tot += res

print(tot)