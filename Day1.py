lines = []

with open("inputs/Day1") as f:
    for line in f:
        lines.append(line.split("\n")[0])

dial = 50
passw = 0


for line in lines:
    if str(line[0]) == "L":
        prev_dial = dial
        dial -= int(line[1:])
        if dial < 0 < prev_dial:
            passw += 1 - int(dial / 100)
        else:
            passw -= int(dial / 100)
        if dial == 0:
            passw += 1
        dial = dial % 100

    elif str(line[0]) == "R":
        dial += int(line[1:])
        passw += int(dial / 100)
        dial = dial % 100

    print(line, dial, passw)


print(passw)
