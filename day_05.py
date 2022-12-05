from collections import deque
import re

with open("input_05") as f:
    data = f.readlines()
    data = [line.replace("\n", "") for line in data]

split_index = data.index("") - 1
initial_stack = data[:split_index]
instructions = data[split_index+2:]
max_length = max(map(len, initial_stack))

formatted_stacks = []
for i in range(0, max_length, 4):
    stack = [line[i:i+3].rstrip() for line in initial_stack]
    stack = [crate for crate in stack if len(crate) > 0 ]
    formatted_stacks.append(deque(stack))

instructions_formatted = []
for instruction in instructions:
    to_add = re.sub("[a-z]*", "", instruction).split(" ")
    to_add = [int(item) for item in to_add if len(item) > 0]
    instructions_formatted.append(to_add)

for move, crate_from, crate_to in instructions_formatted:    
    crate_from, crate_to = crate_from-1, crate_to-1
    for item_id in range(move):
        formatted_stacks[crate_to].appendleft(formatted_stacks[crate_from].popleft())

top_crates = "".join([stack.popleft() for stack in formatted_stacks]).replace("[", "").replace("]", "")

# part 1 answer:
print(top_crates)

formatted_stacks_2 = []
for i in range(0, max_length, 4):
    stack = [line[i:i+3].rstrip() for line in initial_stack]
    stack = [crate for crate in stack if len(crate) > 0 ]
    formatted_stacks_2.append(stack)

for move, crate_from, crate_to in instructions_formatted:    
    crate_from, crate_to = crate_from-1, crate_to-1
    formatted_stacks_2[crate_to] = formatted_stacks_2[crate_from][:move] + formatted_stacks_2[crate_to]
    del formatted_stacks_2[crate_from][:move]

top_crates_2 = "".join([stack[0] for stack in formatted_stacks_2]).replace("[", "").replace("]", "")

# part 2 answer:
print(top_crates_2)