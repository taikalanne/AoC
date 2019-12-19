import wire as Wire

file = open("input.txt", "r")
input = file.read()
input = input.split('\n')
wire1input = input[0].split(',')
wire2input = input[1].split(',')
wire1 = Wire.Wire()
wire2 = Wire.Wire()

for input in wire1input:
    if input[0] == 'U':
        wire1.up(int(input[1:]))
    elif input[0] == 'D':
        wire1.down(int(input[1:]))
    elif input[0] == 'R':
        wire1.right(int(input[1:]))
    elif input[0] == 'L':
        wire1.left(int(input[1:]))

for input in wire2input:
    if input[0] == 'U':
        wire2.up(int(input[1:]))
    elif input[0] == 'D':
        wire2.down(int(input[1:]))
    elif input[0] == 'R':
        wire2.right(int(input[1:]))
    elif input[0] == 'L':
        wire2.left(int(input[1:]))

crossroads = list(set(wire1.route[1:]).intersection(wire2.route[1:]))
pienin = abs(crossroads[0][0] + abs(crossroads[0][1]))
for x in crossroads:
    dist = abs(x[0]) + abs(x[1])
    if dist < pienin:
        pienin = dist
print(pienin)
