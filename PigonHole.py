import  random

pigeons = []
holes = []

# ------------------------------
for a in range(10, 30):
    function = (5 * a) + 8
    pigeons.append(function)

random.shuffle(pigeons)
pigeons.append(pigeons[0])
# ------------------------------

holeCount = len(pigeons) - 1
pigeons.sort()
xContains = False
j = 0
x = 0
while x < len(pigeons):
    for m in holes:
        if pigeons[x] in m:
            xContains = True
            break
    if xContains:
        xContains = False
        x += 1
        continue

    if x <= holeCount:
        sameNumCount = pigeons.count(pigeons[x])
        if sameNumCount > 1:
            newHole = []
            i = 0
            while i < sameNumCount:
                newHole.append(pigeons[x])
                i += 1
            holes.append(newHole)
            x += 1
        else:
            newHole2 = []
            newHole2.append(pigeons[x])
            holes.append(newHole2)
            x += 1
    else:
        holes[j].append(pigeons[x])
        j += 1
        x += 1
        if j >= len(holes):
            j = 0


print(holes)
