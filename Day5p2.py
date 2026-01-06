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

def quick_sort(seq, index):
    if len(seq) <= 1:
        return seq
    else:
        pivot = seq.pop()

    items_upper = []
    items_lower = []

    for i in seq:
        if i[index] > pivot[index]:
            items_upper.append(i)
        else:
            items_lower.append(i)

    return quick_sort(items_lower, index) + [pivot] + quick_sort(items_upper, index)

# Quicksort
sranges = quick_sort(ranges, 0)
sranges_new = [sranges[0]]  # Init
# Merge
j = 0
for i in range(1, len(sranges)):
    if sranges_new[i - j - 1][1] >= sranges[i][0] and sranges_new[i - j - 1][1] <= sranges[i][1]:
        tup_in = (sranges_new[i - j - 1][0], sranges[i][1])
        sranges_new.pop(-1)
        sranges_new.append(tup_in)
        j += 1
    elif sranges_new[i - j - 1][1] <= sranges[i][0] and sranges_new[i - j - 1][1] >= sranges[i][1]:
        pass
    else:
        sranges_new.append(sranges[i])
    # print(sranges_new)

print(len(sranges), len(sranges_new))
score = 0
for i, sr in enumerate(sranges_new):
    score += sr[1] - sr[0] + 1

print(score)




