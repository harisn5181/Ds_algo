"""

Dry run
A
BC
CDE
DEFG
"""
n = 4
i = 1
while i <= n:
    j = 1
    start_chr = chr(ord('A') + i - 1)
    while j <= i:
        charP = chr(ord(start_chr) + j - 1)
        print(charP, end = '')
        j = j + 1
    i = i + 1
    print()