lines = []

with open("inputs/Day4") as f:
    for line in f:
        lines.append(line.split("\n")[0])


def check_adjacent(lines, i, j):
    # Check adjacent
    if i < 0 or j < 0 or i >= len(lines) or j >= len(lines):
        return 0
    else:
        if lines[i][j] == "@":
            return 1
    return 0

score = 0


def recursive_rolls(score, lines):
    sub_score = 0
    original_lines = lines
    for i in range(len(original_lines)):
        for j in range(len(original_lines[i])):
            check_sum = 0
            if original_lines[i][j] == "@":
                check_sum += check_adjacent(original_lines, i - 1, j - 1)
                check_sum += check_adjacent(original_lines, i - 1, j)
                check_sum += check_adjacent(original_lines, i - 1, j + 1)
                check_sum += check_adjacent(original_lines, i, j - 1)
                check_sum += check_adjacent(original_lines, i, j + 1)
                check_sum += check_adjacent(original_lines, i + 1, j - 1)
                check_sum += check_adjacent(original_lines, i + 1, j)
                check_sum += check_adjacent(original_lines, i + 1, j + 1)

                if check_sum < 4:
                    lines[i] = lines[i][:j] + "." + lines[i][j + 1:]
                    sub_score += 1
    score += sub_score
    # print(score, sub_score)
    if sub_score <= 0:
        return score
    else:
        return recursive_rolls(score, lines)


score = recursive_rolls(score, lines)

print(score)


