lines = []

with open("inputs/Day2") as f:
    for line in f:
        flines = line.split(",")

    for line in flines:
        a = (int(line.split("-")[0]), int(line.split("-")[1]))
        lines.append(a)

score = 0

for i in lines:
    for n in range(i[0], i[1] + 1):
        if len(str(n)) % 2 == 0:
            left = str(n)[:int(len(str(n)) / 2)]
            right = str(n)[int(len(str(n)) / 2):]
            if left == right:
                score += n
            # print(n, left, right)
        else:
            pass
            # print("ignored", n)

print(score)



