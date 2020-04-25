#!usr/bin/env python3

# and, or,
# in, not, not in
# is, is not

x = (1, "one", [3, 3.0], "diane")
if "diane" in x:
    print("diane is in the sequence x")
else:
    print("No")

if "one" is not x[1]:
    print("one is in the x[1]")
else:
    print("x[1] is one")