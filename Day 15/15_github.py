from src import helper

if __name__ == "__main__":
    list_of_string = helper.extract_input('long.txt')
    tot = 0
    box_dict= {i:[] for i in range(256)}
    for i in list_of_string:
        helper.operation(i,box_dict)

    for i in box_dict.keys():
        if box_dict[i]:
            tot += helper.get_focusing_power_box(box_dict,i) 
    print(tot)
    # z = helper.tilt_north(x)
    # print(helper.get_points(z))
    # helper.print_input(z,transpose=False)
