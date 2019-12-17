file = open("input2.txt", "r")
input = file.read()
input = input.split(',')
input = list(map(int, input))
input[1] = 12
input[2] = 2
index = 0
while (1):
    if input[index] == 1:
        input[input[index+3]] = input[input[index+1]] + input[input[index+2]]
    elif input[index] == 2:
        input[input[index+3]] = input[input[index+1]] * input[input[index+2]]
    elif input[index] == 99:
        print(input[0])
        exit()
    index += 4
