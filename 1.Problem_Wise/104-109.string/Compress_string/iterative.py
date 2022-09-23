from sys import stdin


def getCompressedString(string):
    # Write your code here.
    k = 1
    new = string[0]
    for i in range(1, len(string)):

        if string[i] == string[i - 1]:
            k += 1
        else:
            if k > 1:
                new += str(k)
                k = 1

            new += string[i]
    if k > 1:
        new += str(k)

    return new


# Main.
string = "aaabbccdsa"
ans = getCompressedString(string)
print(ans)