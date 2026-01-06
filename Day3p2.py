lines = []

with open("inputs/Day3") as f:
    for line in f:
        lines.append(line.split("\n")[0])


def jolt_recursive(line, jolt, jolt_iter, n):
    prev_jolt_iter = jolt_iter
    for i, val in enumerate(line[jolt_iter:len(line) - len(jolt) + 1 + n]):
        if int(val) > jolt[n]:
            jolt[n] = int(val)
            jolt_iter = prev_jolt_iter + i + 1
            iter = i

    # print(line, jolt, jolt_iter, iter, len(line) - len(jolt) + 1 + n)
    n += 1
    if n >= len(jolt):
        return

    jolt_recursive(line, jolt, jolt_iter, n)


score = 0
for line in lines:
    jolt = [0 for i in range(12)]
    jolt_iter = 0
    n = 0
    jolt_recursive(line, jolt, jolt_iter, n)

    jolt = [str(j) for j in jolt]
    num = "".join(jolt)
    # print(num)
    score += int(num)
    # break

print(score)



