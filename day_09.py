from math import sqrt, isclose

with open("input_09") as f:
    data = f.readlines()
    data = [line.rstrip().split(" ") for line in data]
    data = [(line[0], int(line[1])) for line in data]

def calc_distance(p_1, p_2):
    return sqrt((p_1[0] - p_2[0])**2 + (p_1[1] - p_2[1])**2)

def move(head_pos, tail_pos):
    distance = calc_distance(head_pos, tail_pos)
    if distance in [0, 1] or isclose(distance, sqrt(2)):
        return tail_pos
    moves = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, -1], [-1, 1]]
    tail_pos_new = [[tail_pos[0] + move[0], tail_pos[1] + move[1]] for move in moves]
    distanes_new = [calc_distance(head_pos, tail_new) for tail_new in tail_pos_new]
    min_index = distanes_new.index(min(distanes_new))
    return tail_pos_new[min_index]

curr_head = [4, 0]
curr_tail = [4, 0]
curr_pos = [[15, 11] for _ in range(10)]

pos_visited = list([curr_tail])
pos_visited2 = list([curr_pos[-1]])

for move_dir, steps in data:
    for step in range(steps):
        if move_dir == "R":
            curr_head = [curr_head[0], curr_head[1] + 1]
            curr_tail = move(curr_head, curr_tail)
            curr_pos[0] = [curr_pos[0][0], curr_pos[0][1] + 1]
            for i in range(1, 10):
                curr_pos[i] = move(curr_pos[i-1], curr_pos[i])
        elif move_dir == "U":
            curr_head = [curr_head[0] - 1, curr_head[1]]
            curr_tail = move(curr_head, curr_tail)
            curr_pos[0] = [curr_pos[0][0] - 1, curr_pos[0][1]]
            for i in range(1, 10):
                curr_pos[i] = move(curr_pos[i-1], curr_pos[i])
        elif move_dir == "L":
            curr_head = [curr_head[0], curr_head[1] - 1]
            curr_tail = move(curr_head, curr_tail)
            curr_pos[0] = [curr_pos[0][0], curr_pos[0][1] - 1]
            for i in range(1, 10):
                curr_pos[i] = move(curr_pos[i-1], curr_pos[i])
        elif move_dir == "D":
            curr_head = [curr_head[0] + 1, curr_head[1]]
            curr_tail = move(curr_head, curr_tail)
            curr_pos[0] = [curr_pos[0][0] + 1, curr_pos[0][1]]
            for i in range(1, 10):
                curr_pos[i] = move(curr_pos[i-1], curr_pos[i])
        pos_visited.append(curr_tail)
        pos_visited2.append(curr_pos[-1])

print(len(set([tuple(pos) for pos in pos_visited]))) # part 1 answer
print(len(set([tuple(pos) for pos in pos_visited2]))) # part 2 answer