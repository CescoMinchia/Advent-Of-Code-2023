import os

def open_file_in_same_directory(file_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)

    with open(file_path, 'r') as file:
        content = file.read()

    return content
    
content = open_file_in_same_directory("input.txt")
#print(content)

input = "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1"


from collections import Counter
import re

def calculate_points(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 2*calculate_points(n-1)


def parse_line(line):
    pattern = re.compile(r"[:|] ")
    game, win_numb, draw_numb = pattern.split(line)
    
    win_numb =  [i for i in win_numb.split(" ") if i]#.sort()
    draw_numb =  [i for i in draw_numb.split(" ") if i]
    matched_numb = [i for i in draw_numb if i in win_numb]
    
    n_game = [int(s) for s in game.split() if s.isdigit()][0]
    result = dict.fromkeys(list(range(n_game+1,n_game+len(matched_numb)+1)),1)
    
    return result

def parse_input(text):
    
    n_cards = len(text.split("\n"))
    result = Counter(dict.fromkeys(list(range(1,n_cards+1)),1))
    for n, line in enumerate(text.split("\n"),1):
        print(f"Game {n}: play {result[n]} card(s)")
        res = Counter(parse_line(line))
        for key in res:    
            res[key] *=  (result[n])
        #print(res)
        result += res
    #print(result)
    print(sum(result.values()))
    
    #return total
    #print(result)

print(parse_input(content))


