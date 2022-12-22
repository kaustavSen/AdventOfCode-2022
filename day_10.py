with open("input_10") as f:
    data = f.readlines()
    data = [line.rstrip().split(" ") for line in data]

cycle = 1
X = 1
cycle_register = dict()
for instruction, *value in data:
    if instruction == "addx":
        cycle += 2  
        X += int(value[0])
    else:
        cycle += 1
    cycle_register[cycle] = X

signal_sum = 0
for signal in range(20, 221, 40):
    if not (signal_X := cycle_register.get(signal)):
        signal_X = cycle_register.get(signal-1)
    signal_sum += signal_X * signal
print(signal_sum) # part 1 answer

crt_image = ["." for _ in range(40*6)]
addx_wait = 2
sprite_pos = 1
instruction_pos = 0
for pixel_pos in range(40*6):
    if sprite_pos - 1 <= (pixel_pos % 40) <= sprite_pos + 1:
            crt_image[pixel_pos] = "#"
    if data[instruction_pos][0] == "noop":
        instruction_pos += 1
    else:
        addx_wait -= 1
        if addx_wait == 0:
            addx_wait = 2
            sprite_pos += int(data[instruction_pos][1])
            instruction_pos += 1

from textwrap import wrap
# part 2 answer
for line in wrap("".join(crt_image), width=40):
    print(line)