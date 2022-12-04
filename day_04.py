with open("input_04") as f:
    data = f.readlines()
    data = [line.rstrip() for line in data]
    data = [line.split(",") for line in data]

def get_units(elf_alloc):
    units_range = range(*[int(num) + adder for num, adder in zip(elf_alloc.split("-"), [0, 1])])
    return set(units_range)

def is_fully_contained(units1, units2):
    return units1.issuperset(units2) or units2.issuperset(units1)

def is_disjoint(units1, units2):
    return units1.isdisjoint(units2)

num_fully_contained = 0
num_disjoint = 0
for elf1, elf2 in data:
    elf1_units = get_units(elf1)
    elf2_units = get_units(elf2)
    num_fully_contained += is_fully_contained(elf1_units, elf2_units)
    num_disjoint += is_disjoint(elf1_units, elf2_units)

# part 1 solution
print(num_fully_contained)

# part 2 solution
print(len(data) - num_disjoint)