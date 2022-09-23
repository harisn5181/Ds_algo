s = input()
r = input()
ans = ""
for i in range(len(s)):
    if s[i] != r:
        ans = ans + s[i]
print(ans)
