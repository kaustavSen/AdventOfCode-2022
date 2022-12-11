with open("input_07") as f:
    data = f.readlines()
    data = [line.rstrip() for line in data]

import re

paths = []
current_path = "/"
for command in data:
    if command == "$ cd ..":
        current_path = "/".join(current_path.split("/")[:-2]) + "/"
    elif command.startswith("$ cd") and not command.endswith("/"):
        current_path += (command.replace("$ cd ", "") + "/")
    paths.append(current_path)    

commands_with_paths = list(zip(data, paths))
dirs = list(set(paths))
dir_sizes = []
for dir in dirs:
    subset_commands_with_paths = [command for command, path in commands_with_paths if path.startswith(dir)]
    dir_size = 0
    for command in subset_commands_with_paths:
        if command[0].isdigit(): dir_size += int(re.sub("[a-z\\. ]+", "", command))
    dir_sizes.append(dir_size)

print(sum([size for size in dir_sizes if size <= 100000])) # part 1 solution

total_space = 70_000_000
available_space = total_space - max(dir_sizes)
space_required = 30_000_000
dir_to_del_size = min([dir for dir in dir_sizes if available_space + dir >= space_required])
print(dir_to_del_size) # part 2 solution
