import os

def extract_input(filename):
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'input',filename)
    with open(path,"r") as f:
        content = f.read()
    
    return [list(i) for i in content.split('\n')]

def tilt_north(pattern,iter=None):
    previous_pattern = [[j for j in i]for i in pattern]
    next_pattern = []
    it = 0
    while True:
        next_pattern = [[j for j in i]for i in previous_pattern]
        if it == iter:
            break
        for r,i in enumerate(previous_pattern):
            if r == 0:
                continue
            for c,j in enumerate(i):
                if j != 'O':
                    continue
                if previous_pattern[r - 1][c] == '.':
                    previous_pattern[r - 1][c] = 'O'
                    previous_pattern[r][c] = '.'
        if  next_pattern == previous_pattern:
            break
        it += 1
    return next_pattern

def tilt_south(pattern,iter=None):
    previous_pattern = [[j for j in i]for i in pattern]
    previous_pattern = rotate_pattern(previous_pattern,2)
    next_pattern = []
    it = 0
    while True:
        next_pattern = [[j for j in i]for i in previous_pattern]
        if it == iter:
            break
        for r,i in enumerate(previous_pattern):
            if r == 0:
                continue
            for c,j in enumerate(i):
                if j != 'O':
                    continue
                if previous_pattern[r - 1][c] == '.':
                    previous_pattern[r - 1][c] = 'O'
                    previous_pattern[r][c] = '.'
        if  next_pattern == previous_pattern:
            break
        it += 1
    next_pattern=rotate_pattern(next_pattern,-2)
    return next_pattern 

def tilt_west(pattern,iter=None):
    previous_pattern = [[j for j in i]for i in pattern]
    previous_pattern = rotate_pattern(previous_pattern,1)
    next_pattern = []
    it = 0
    while True:
        next_pattern = [[j for j in i]for i in previous_pattern]
        if it == iter:
            break
        for r,i in enumerate(previous_pattern):
            if r == 0:
                continue
            for c,j in enumerate(i):
                if j != 'O':
                    continue
                if previous_pattern[r - 1][c] == '.':
                    previous_pattern[r - 1][c] = 'O'
                    previous_pattern[r][c] = '.'
        if  next_pattern == previous_pattern:
            break
        it += 1
    next_pattern = rotate_pattern(next_pattern,-1)
    return next_pattern 

def tilt_east(pattern,iter=None):
    previous_pattern = [[j for j in i]for i in pattern]
    previous_pattern = rotate_pattern(previous_pattern,-1)
    next_pattern = []
    it = 0
    while True:
        next_pattern = [[j for j in i]for i in previous_pattern]
        if it == iter:
            break
        for r,i in enumerate(previous_pattern):
            if r == 0:
                continue
            for c,j in enumerate(i):
                if j != 'O':
                    continue
                if previous_pattern[r - 1][c] == '.':
                    previous_pattern[r - 1][c] = 'O'
                    previous_pattern[r][c] = '.'
        if  next_pattern == previous_pattern:
            break
        it += 1
    next_pattern = rotate_pattern(next_pattern,1)
    return next_pattern 

def cycle(pattern):
    x = [[j for j in i]for i in pattern]
    x = tilt_north(x)
    x = tilt_west(x)
    x = tilt_south(x)
    x = tilt_east(x)
    return(x)
    
def rotate_pattern(pattern,n_rotation=1):
    # anti clock wise situation => convert to positive (-1 anticlockwise = 3 clockwise)
    while n_rotation < 0:
        n_rotation += 4 
    n_rotation = n_rotation % 4
    x = [[j for j in i]for i in pattern]
    while n_rotation > 0:
        x = list(map(list, zip(*x)))
        for row in x:
            row.reverse()
        n_rotation -= 1
    return(x)


def get_points(pattern):
    p = len(pattern)
    tot = 0
    for i in pattern:
        tot += len([j for j in i if j == 'O'])*p
        p -= 1
    return(tot)

# da sistemare il transpose
def print_input(pattern,transpose=False):
    if transpose:
        x = rotate_pattern(pattern,1)
    else:
        output = '\n'.join([''.join(i) for i in pattern])
    print(output)


