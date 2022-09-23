from sys import stdin


def highestOccuringChar(string):
    # Your code goes here
    all_freq = {}
    for i in string:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1

    max = 0
    for key in all_freq:
        if all_freq[key] > max:
            max = all_freq[key]
            temp_for_key = key
    return temp_for_key


# main
string = stdin.readline().strip();
ans = highestOccuringChar(string)

print(ans)
