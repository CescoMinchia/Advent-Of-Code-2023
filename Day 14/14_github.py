from src import helper

if __name__ == "__main__":
    initial_pattern = helper.extract_input('long.txt')
    memory = [initial_pattern]

    long_n = 1000000000

    it2 = 0
    x = [[j for j in i]for i in initial_pattern]
    while True:
        it2 += 1
        x = helper.cycle(x)
        if x in memory:
            print(f"Found repeated pattern")
            repeated = [[j for j in i]for i in x]
            break
        else:
            memory.append(x)

    # Find first instance of the repeated pattern
    temp = [[j for j in i]for i in initial_pattern]
    it1 = 0
    while True:
        it1 += 1
        temp = helper.cycle(temp)
        if temp == repeated:
            period = it2-it1
            break

        

    y = [[j for j in i]for i in repeated]
    for _ in range((long_n-it1)%period):
        y = helper.cycle(y)


    print(helper.get_points(y))
