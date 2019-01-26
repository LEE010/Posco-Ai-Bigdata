import sys

args = sys.argv[1:]

with open(args[0], "r") as f:
    scorefile = f.read()

scores = list(map(lambda x: x.split(), scorefile.split('\n')))

for i, student in enumerate(scores):
    try:
        total = int(student[1])*0.4 + int(student[2])*0.6
        if total >= 90:
            scores[i].append('%.1f(A)' %total)
        elif total >= 80 :
            scores[i].append('%.1f(B)' %total)
        elif total >= 70 :
            scores[i].append('%.1f(C)' %total)
        elif total >= 60 :
            scores[i].append('%.1f(D)' %total)
        else:
            scores[i].append('%.1f(F)' %total)
    except IndexError:
        continue

with open(args[1], "w") as f:
    for score in scores:
        try:
            f.write("%s %s %s %s\n" % tuple(score))
        except TypeError:
            continue
