from src import helper as h
import copy

def get_marked_tiles_from_chosen_beam(beam,map):
    '''
    beam as a a tuple: ex: (1,3,"R")
    '''
    m = copy.deepcopy(map)

    beams = [beam]
    while beams:
        new_b = []
        for b in beams:
            # m.display()
            new_b.extend(m.move_beam_to_next_tile(*b))
        beams = copy.deepcopy(new_b)
    return m.n_marked_tiles

if __name__ == "__main__":
    x = h.extract_input('long.txt')
    m = h.Map(x)
    best = 0
    # from above to below
    for x in range(0,m.width):
        beam = (x,0,"D")
        res = get_marked_tiles_from_chosen_beam(beam,m)
        if res > best:
            best = res

    # from below to above
    for x in range(0,m.width):
        beam = (x,m.height-1,"U")
        res = get_marked_tiles_from_chosen_beam(beam,m)
        if res > best:
            best = res

    # from left to right
    for y in range(0,m.height):
        beam = (0,y,"R")
        res = get_marked_tiles_from_chosen_beam(beam,m)
        if res > best:
            best = res

    # from right to left
    for y in range(0,m.height):
        beam = (m.width-1,y,"L")
        res = get_marked_tiles_from_chosen_beam(beam,m)
        if res > best:
            best = res

    print(best)
