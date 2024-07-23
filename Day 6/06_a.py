import os

def open_file_in_same_directory(file_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)

    with open(file_path, 'r') as file:
        content = file.read()

    return content
    
content = open_file_in_same_directory("input.txt")
#print(content)

# def total_distance(min_t,max_t,tot_t,record):
#     n_win = 0
#     for i in range(min_t,max_t+1):
#         v = i
#         t_remaining = tot_t - i
#         d = t_remaining * v
#         if d >= record:
#             n_win+=1
#     print(f"n_win: {n_win}")
    #return(v)

def total_distance(tot_t,record):
    n_win = 0
    for i in range(tot_t+1):
        v = i
        t_remaining = tot_t - i
        d = t_remaining * v
        print(d)
        if d >= record:
            n_win+=1
        print(i)
    print(f"n_win: {n_win}")

def total_distance2(min_t,max_t,tot_t,record):
    n_win = 0
    for i in range(min_t,max_t+1):
        v = i
        t_remaining = tot_t - i
        d = t_remaining * v
        #print(d)
        if d >= record:
            n_win+=1
        #print(i)
    print(f"n_win: {n_win}")

def get_min_t(t_tot,d):
    # t^2-t*t_tot+min_d=0
    # a = 1
    # b = -t_tot
    # c =  d
    # deta =t_tot**2 -  4 * d
    # t11,t2 = (tot-(t_tot - 4 + 4 * d)**(1/2))/2
    #
    t = t_tot-(t_tot**2 - 4 * d)**(1/2)/2
    print(t)
max_t=43998541
min_t=5980953
#get_min_t(49979494,263153213781851)
print(max_t-min_t)
#total_distance2(min_t,max_t,49979494,263153213781851)