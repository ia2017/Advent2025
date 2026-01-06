lines = []

with open("inputs/Day4") as f:
    for line in f:
        lines.append(line.split("\n")[0])

score = 0

def check_adjacent(lines, i, j):
    # Check adjacent
    if i < 0 or j < 0 or i >= len(lines) or j >= len(lines):
        return 0
    else:
        if lines[i][j] == "@":
            return 1
    return 0


for i in range(len(lines)):
    for j in range(len(lines[i])):
        check_sum = 0
        if lines[i][j] == "@":
            check_sum += check_adjacent(lines, i - 1, j - 1)
            check_sum += check_adjacent(lines, i - 1, j)
            check_sum += check_adjacent(lines, i - 1, j + 1)
            check_sum += check_adjacent(lines, i, j - 1)
            check_sum += check_adjacent(lines, i, j + 1)
            check_sum += check_adjacent(lines, i + 1, j - 1)
            check_sum += check_adjacent(lines, i + 1, j)
            check_sum += check_adjacent(lines, i + 1, j + 1)

            if check_sum < 4:
                score += 1

print(score)


