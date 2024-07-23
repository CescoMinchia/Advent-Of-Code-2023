import os
import copy

class Map():
    map = None
    copy_map = None
    tiles = None

    width = None
    height = None

    n_marked_tiles = 0

    memory = None

    def __init__(self,map):
        self.map = copy.deepcopy(map)
        self.copy_map = copy.deepcopy(map)
        self.width = len(map[0])
        self.height = len(map)

        self.tiles = {}
        self.memory = {}
        self.create_dynamic_tile(".",[(0,-1),(1,0),(0,1),(-1,0)])
        self.create_dynamic_tile("/",[(1,0),(0,-1),(-1,0),(0,1)])
        self.create_dynamic_tile("\\",[(-1,0),(0,1),(1,0),(0,-1)])
        self.create_dynamic_tile("|",[(0,-1),(0,-1),(0,1),(0,1)],two_beams=["R","L"])
        self.create_dynamic_tile("-",[(1,0),(1,0),(1,0),(-1,0)],two_beams=["U","D"])
        
    def create_dynamic_tile(self,char,dynamic,two_beams=None):
        self.tiles[char] = Tile(char,dynamic,two_beams=two_beams)

    def get_next_direction(self,x,y,d):
        tile_character = self.get_tile(x,y)
        tile_obj = self.tiles[tile_character]
        return tile_obj.interact_with_tile(d)

    def set_tile(self,x,y,new_char):
        old_tile = self.get_tile_copy(x,y)
        if old_tile != new_char:
            self.n_marked_tiles += 1
            self.copy_map[y][x] = new_char

    def get_tile(self,x,y):
        return self.map[y][x]

    def get_tile_copy(self,x,y):
        return self.copy_map[y][x]

    def move_beam_to_next_tile(self,x,y,d):
        # for debugging purpose, the crossing tiles of the copy map are marked with '#'
        self.set_tile(x,y,'#')

        # it is a list of 1 or 2 tuples. The latter if there is a splitter
        new_d = self.get_next_direction(x,y,d)
        new_coords_and_dir = \
            [(x+d[0],y+d[1],self.get_direction_from_delta(d[0],d[1])) for d in new_d] 
        new_beams = []
        # check one by one if inside map, otherwise remove beam
        for new_x,new_y,new_dir in new_coords_and_dir:
            # check boundaries
            if new_x < 0 or new_x > self.width - 1 or\
                new_y < 0 or new_y > self.height - 1:
                continue

            # check if already crossed, so no need to compute the dynamic again
            if (new_x,new_y) not in self.memory.keys():
                self.memory[(new_x,new_y)] = [new_dir]
            elif new_dir not in self.memory[(new_x,new_y)]:
                self.memory[(new_x,new_y)].append(new_dir)
            else: 
                continue

            # if checks are passed, eligible to be a new beam
            new_beams.append((new_x,new_y,new_dir))
        
        return new_beams

    def get_direction_from_delta(self,dx,dy):
        if dx == 0 and dy == -1:
            return "U"        
        if dx == 1 and dy == 0:
            return "R"
        if dx == 0 and dy == 1:
            return "D"
        if dx == -1 and dy == 0:
            return "L"

    def display(self):
        for i in self.copy_map:
            print(''.join(i))
        print("\n")


class Tile():
    char = None
    dynamic = None
    two_beams = None

    def __init__(self,char,dynamic,two_beams=None):
        self.char = char
        self.dynamic = copy.deepcopy(dynamic)
        if two_beams is None:
            self.two_beams = []
        else:
            self.two_beams = copy.deepcopy(two_beams)

    def interact_with_tile(self,d):
        match d:
            case "U":
                dx = self.dynamic[0][0]
                dy = self.dynamic[0][1]
            case "R":
                dx = self.dynamic[1][0]
                dy = self.dynamic[1][1]
            case "D":
                dx = self.dynamic[2][0]
                dy = self.dynamic[2][1]
            case "L":
                dx = self.dynamic[3][0]
                dy = self.dynamic[3][1]
        if d in self.two_beams:
            return[(dx,dy),(-dx,-dy)]
        return[(dx,dy)]

def extract_input(filename):
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'input',filename)
    with open(path,"r") as f:
        content = f.read()
    
    return [list(i) for i in content.split('\n')]

def move_beam_mirror(beam):
    x,y,d = beam
    dx = 0
    dy = 0
    match beam:
        case "U":
            dy = 1
        case "R":
            dx = 1
        case "D":
            dy = -1
        case "L":
            dx = -1

def move_beam_straight(beam):
    '''
    If you give one beam, it gives next coord as if the map were infinite and no obstacle
    '''
    x,y,d = beam
    dx = 0
    dy = 0
    match beam:
        case "U":
            dy = 1
        case "R":
            dx = 1
        case "D":
            dy = -1
        case "L":
            dx = -1
    return x+dx,y+dy,d
    
# def get_next_move_beam(beam,map):
#     x,y,d = map.tiles[](beam)
#     if x < 0 or y < 0 or x >= len(map[0]) or y >= len(map):
#         return []
#     match map[y][x]:
#         case "/":
#             move_beam_mirror([x,y,d])



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


# da sistemare il transpose
def print_input(pattern,transpose=False):
    if transpose:
        x = rotate_pattern(pattern,1)
    else:
        output = '\n'.join([''.join(i) for i in pattern])
    print(output)


