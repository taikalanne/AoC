import math

file = open("input.txt", "r")
lines = file.readlines()
lines = list(map(int, lines))
sum = 0
for number in lines:
    int(number)
    number = math.floor(number / 3) - 2
    sum += number
    if number > 8:
        lines.append(number)
print(sum)
