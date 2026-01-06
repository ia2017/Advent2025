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
        str_n = str(n)
        mult = 0
        for j in range(2, len(str_n) + 1):
            status = 0
            if len(str_n) % j == 0:
                left = str_n[0:int(len(str_n) / j)]
                for k in range(1, j):
                    right = str_n[k*int(len(str_n) / j):(k + 1)*int(len(str_n) / j)]
                    if left != right:
                        status += 1
                        break
                if not status:
                    # print(n)
                    score += n
                    break



print(score)



