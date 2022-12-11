with open("input_06") as f:
    data = f.readlines()
    data = [line.rstrip() for line in data][0]

from collections import Counter
for i in range(len(data)):
    subdata = data[i:i+14]  # for part 2 change 4 to 14
    max_count = Counter(subdata).most_common(1)[0][1]
    if max_count == 1:
        break
# print(i+4)  # part 1 solution 
print(i+14) # part 2 solution 
