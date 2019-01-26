import sys

args = sys.argv[1:]

with open(args[0], "r") as f:
    cpfile = f.read()
# with open(args[1], "w") as f:
with open(args[1], "w") as f:
    decopfile = f.write(cpfile)
