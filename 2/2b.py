file = open("input2.txt", "r")
input = file.read()
input = input.split(',')
input = list(map(int, input))
reset = input
ind = 0
input[1] = 0
input[2] = 0
laskuri = 0
for noun in range(99):
    for verb in range(99):
        while(input[ind] != 99):
            if input[ind] == 1:
                cache = input[input[ind+1]]+input[input[ind+2]]
                input[input[ind+3]] = cache
            elif input[ind] == 2:
                cache = input[input[ind+1]]*input[input[ind+2]]
                try:
                    input[input[ind+3]] = cache
                except IndexError:
                    print("overflow")
                    break
            ind += 4
        laskuri += 1
        print("laskuri @ ", laskuri)
        if input[0] == 19690720:
            print(100*noun+verb)
            exit()
        input = reset
        ind = 0
        input[1] = verb
        input[2] = noun
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
