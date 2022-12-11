data = []
with open("input_08") as f:
    for lines in f.readlines():
        row = [int(line.rstrip()) for line in lines if len(line.rstrip())]
        data.append(row)
max_row = len(data) - 1
max_col = len(data[0]) - 1

def score_count(height, trees):
    score = 0
    for tree in trees:
        if tree >= height:
            score += 1
            break
        else:
            score += 1
    return score

def is_visible_and_get_score(height, row, col):
    if row in [0, max_row] or col in [0, max_col]:
        return True, 0
    trees_left = data[row][:col]
    trees_right = data[row][col+1:]
    trees_bottom = [data[data_row][col] for data_row in range(row+1, max_row+1)]
    trees_top = [data[data_row][col] for data_row in range(0, row)]
    left_visible, right_visible, top_visible, bottom_visible = [True] * 4
    if any([tree >= height for tree in trees_left]):
        left_visible = False
    if any([tree >= height for tree in trees_right]):
        right_visible = False
    if any([tree >= height for tree in trees_top]):
        top_visible = False
    if any([tree >= height for tree in trees_bottom]):
        bottom_visible = False
    # scenic score computation (for part 2)
    score_left = score_count(height, reversed(trees_left))
    score_right = score_count(height, trees_right)
    score_bottom = score_count(height, trees_bottom)
    score_top = score_count(height, reversed(trees_top))
    score = score_left * score_right * score_top * score_bottom
    return any([left_visible, right_visible, top_visible, bottom_visible]), score

num_visible = 0
max_score = 0
for row in range(max_row+1):
    for col in range(max_col+1):
        is_visible, score = is_visible_and_get_score(data[row][col], row, col)
        num_visible += is_visible
        max_score = max(max_score, score)
print(num_visible) # part 1 answer
print(max_score) # part 2 answer