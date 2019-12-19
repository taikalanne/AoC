file = open("input2.txt", "r")
input = file.read()
input = input.split(',')
input = list(map(int, input))
reset = input.copy()
ind = 0
# input[1] = 0
# input[2] = 0
for noun in range(0, 100):
    for verb in range(0, 100):
        input[1] = noun
        input[2] = verb
        while(input[ind] != 99):
            if input[ind] == 1:
                cache = input[input[ind+1]]+input[input[ind+2]]
                input[input[ind+3]] = cache
            elif input[ind] == 2:
                cache = input[input[ind+1]]*input[input[ind+2]]
                input[input[ind+3]] = cache
            ind += 4
        if input[0] == 19690720:
            print(100*noun+verb)
            exit()
        input = reset.copy()
        ind = 0

    '''
else:
        input = reset
        ind = 0
        input[1] = verb
        input[2] = noun
        ind += 4
'''
else:
    print("ei loydy")
