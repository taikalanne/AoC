import wire as Wire

file = open("testi1.txt", "r")
input = file.read()
input = input.split('\n')
wire1input = input[0].split(',')
wire2input = input[1].split(',')
wire1 = Wire.Wire()
wire2 = Wire.Wire()
breakout = 0

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
        for i in range(1, int(input[1:])):
            wire2.up_once()
            if wire2.current_pos() in wire1.route:
                breakout = 1
                break
    elif input[0] == 'D':
        for i in range(1, int(input[1:])):
            wire2.down_once()
            if wire2.current_pos() in wire1.route:
                breakout = 1
                break
    elif input[0] == 'R':
        for i in range(1, int(input[1:])):
            wire2.right_once()
            if wire2.current_pos() in wire1.route:
                breakout = 1
                break
    elif input[0] == 'L':
        for i in range(1, int(input[1:])):
            wire2.left_once()
            if wire2.current_pos() in wire1.route:
                breakout = 1
                break
    if breakout == 1:
        break

steps = 0
for x in wire1.route:
    if wire2.current_pos() == x:
        break
    else:
        steps += 1
print(steps)
print(len(wire2.route))
print(steps + len(wire2.route))
