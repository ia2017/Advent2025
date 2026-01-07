lines = []

with open("inputs/Day7_test") as f:
    for line in f:
        lines.append(line.split("\n")[0])

beam = []
for i, line in enumerate(lines):
    for j, val in enumerate(line):
        if val == "S":
            beam.append(j)
        if val == "^":

