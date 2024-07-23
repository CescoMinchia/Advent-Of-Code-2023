import os

def extract_input(filename):
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'input',filename)
    with open(path,"r") as f:
        content = f.read()
    
    return [i for i in content.split(',')]

def convert_char(char,starting_value=0):
    x = starting_value + ord(char) # ascii code
    x *= 17
    x %= 256
    return(x)

def convert_string(string,starting_value=0):
    for ch in list(string):
        starting_value = convert_char(ch,starting_value)
    return(starting_value)

def convert_list(list_of_string):
    tot = 0
    for i in list_of_string:
        tot += convert_string(i)

def add_lens(box_dict,n_box,label,lens):
    list_labels = [i for i,_ in box_dict[n_box]]
    if label not in list_labels:
        box_dict[n_box].append([label,lens])
    else:
        i = list_labels.index(label)
        box_dict[n_box][i][1] = lens

def remove_lens(box_dict,n_box,label):
    list_labels = [i for i,_ in box_dict[n_box]]
    if label in list_labels:
        i = list_labels.index(label)
        box_dict[n_box].pop(i)

def operation(string,box_dict):
    if '=' in list(string):
        label=string.split('=')[0]
        lens_to_add=int(string.split('=')[1])
        n_box=int(convert_string(label))
        # print(f"add to label: {label}, box: {str(n_box)},lens {str(lens_to_add)}")
        add_lens(box_dict,n_box,label,lens_to_add)
    else:
        label=string.split('-')[0]
        n_box=int(convert_string(label))
        # print(f"remove to label: {label}, box: {str(n_box)}")
        remove_lens(box_dict,n_box,label)



def get_focusing_power_box(box_dict,n_box):
    tot = sum([ (n_box+1)*(n+1)*x[1] for n,x in enumerate(box_dict[n_box])])
    return(tot)