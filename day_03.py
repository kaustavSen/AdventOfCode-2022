with open("input_03") as f:
    data = f.readlines()
    data = [line.rstrip() for line in data]

common_items = []
for rugsack in data:
    part1 = rugsack[:len(rugsack)//2]
    part2 = rugsack[len(rugsack)//2:]
    for item in part1:
        if item in part2:
            common_items.append(item)
            break

from string import ascii_letters
priority_mapping = dict(zip(ascii_letters, range(1, 53)))

# part 1 answer:
print(sum([priority_mapping.get(item) for item in common_items]))

def flatten(nested_list):
    return [item for ind_list in nested_list for item in ind_list]

from collections import Counter
data_grouped = [data[x:x+3] for x in range(0, len(data), 3)]

badge_list = []
for group in data_grouped:
    badge = Counter(flatten([list(set(rugsack)) for rugsack in group])).most_common(1)[0][0]
    badge_list.append(badge)

# part 2 answer
print(sum([priority_mapping.get(item) for item in badge_list]))