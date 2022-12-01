with open("input_01") as f:
    data = f.readlines()
    data = [line.rstrip() for line in data]

mainlist = []
sublist = []
for item in data:
    if item == "":
        mainlist.append(sublist)
        sublist = []
    else:
        sublist.append(item)

mainlist = [[int(item) for item in list] for list in mainlist]
sums = [sum(list) for list in mainlist]

# Part 1 answer:
max(sums)

sums.sort(reverse=True)
# Part 2 answer:
sum(sums[:3])