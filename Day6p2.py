lines = []

with open("inputs/Day6") as f:
    for line in f:
        lines.append(line.split("\n")[0])

arrays = []

score = 0
for i, line in enumerate(lines):
    val = ""
    sarray = []
    j = 0
    for char in line:
        if char == " " and len(sarray) > 0:
            # Maths
            if i == len(lines) - 1:
                if val == "*":
                    subscore = 1
                    for s in arrays:
                        subscore *= s[j]
                    score += subscore
                elif val == "+":
                    subscore = 0
                    for s in arrays:
                        subscore += s[j]
                    score += subscore
                else:
                    print("Warning", val)
                val = ""
            else:
                if i < len(lines) - 1:
                    arrays.append(sarray)
                    sarray = []
            j += 1
        elif char == " " and len(val) == 0:
            pass
        else:
            if i == 0:
                sarray.append(val)
            else:
                sarray[j] = sarray[j] + char
    # Last char
    if len(val) > 0:
        # Maths
        if i == len(lines) - 1:
            if val == "*":
                subscore = 1
                for s in arrays:
                    subscore *= s[j]
                score += subscore
            elif val == "+":
                subscore = 0
                for s in arrays:
                    subscore += s[j]
                score += subscore
            else:
                print("Warning 2", val)
            val = ""
        else:
            sarray.append(int(val))
            val = ""
    if i < len(lines) - 1:
        arrays.append(sarray)

print(score)
