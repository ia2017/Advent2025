lines = []

with open("inputs/Day3") as f:
    for line in f:
        lines.append(line.split("\n")[0])

score = 0
for line in lines:
    jolt = [0, 0]
    jolt_iter = 0
    for i, val in enumerate(line[:len(line) - 1]):
        if int(val) > jolt[0]:
            jolt[0] = int(val)
            jolt_iter = i + 1

    for i, val in enumerate(line[jolt_iter:len(line) - 1 + 1]):
        if int(val) > jolt[1]:
            jolt[1] = int(val)
    jolt = [str(jolt[0]), str(jolt[1])]
    num = "".join(jolt)
    score += int(num)

print(score)



