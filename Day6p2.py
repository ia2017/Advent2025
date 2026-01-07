lines = []

with open("inputs/Day6") as f:
    for line in f:
        lines.append(line.split("\n")[0])

buffer = 2
score = 0
sline = []
for i, line in enumerate(lines[:-1]):
    if i == 0:
        sline = list(line)
        sline += ['' for i in range(buffer)]
    else:
        for j, char in enumerate(line):
            sline[j] += char

temp = []
op_ind = 0
for s in sline:
    if len(s.split()) == 0:
        subscore = 0
        for i in range(op_ind, len(lines[-1])):
            if lines[-1][i] == "*":
                subscore = 1
                for t in temp:
                    subscore *= t
                op_ind = i + 1
                break
            elif lines[-1][i] == "+":
                subscore = 0
                for t in temp:
                    subscore += t
                op_ind = i + 1
                break
        score += subscore
        temp = []
        pass
    else:
        temp.append(int(s))



# print(sline)

print(score)
