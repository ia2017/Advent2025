ranges = []
ingred = []
switch_bool = False
with open("inputs/Day5") as f:
    for line in f:
        inline = line.split("\n")[0]
        if inline == "":
            switch_bool = True
            continue
        if not switch_bool:
            tup_in = (int(inline.split("-")[0]), int(inline.split("-")[1]))
            ranges.append(tup_in)
        else:
            ingred.append(int(inline))

score = 0
for i in ingred:
    for r in ranges:
        if r[0] <= i <= r[1]:
            score += 1
            break

print(score)
