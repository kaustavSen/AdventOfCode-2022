with open("input_02") as f:
    data = f.readlines()
    data = [line.rstrip() for line in data]
    data = [line.split(" ") for line in data]

def round_score(opponent, own):
    own = {"X": "A", "Y": "B", "Z": "C"}.get(own)
    if own == opponent:
        win_loss_score = 3
    elif (own == "A" and opponent == "C") or (own == "B" and opponent == "A") or (own == "C" and opponent == "B"):
        win_loss_score = 6
    else:
        win_loss_score = 0
    return win_loss_score + {"A": 1, "B": 2, "C": 3}.get(own)

score = 0
for opponent, own in data:
    score += round_score(opponent, own)

# part 1 answer:
print(score)

def deduce_own(opponent, outcome):
    if outcome == "X":
        return {"A": "Z", "B": "X", "C": "Y"}.get(opponent)
    elif outcome == "Y":
        return {"A": "X", "B": "Y", "C": "Z"}.get(opponent)
    else:
        return {"A": "Y", "B": "Z", "C": "X"}.get(opponent)

score2 = 0
for opponent, outcome in data:
    own = deduce_own(opponent, outcome)
    score2 += round_score(opponent, own)

# part 2 answer:
print(score2)