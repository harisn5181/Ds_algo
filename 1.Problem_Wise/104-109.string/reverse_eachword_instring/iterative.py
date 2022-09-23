from sys import stdin


def reverseEachWord(string):
    # Your code goes here
    rev_str = ''
    rev_word = ''
    for i in string:
        if i == " ":
            rev_str = rev_str + rev_word + i
            rev_word = " "

        else:
            rev_word = i + rev_word
    return rev_str + rev_word


# main
string = "Hello i am haris"

ans = reverseEachWord(string)

print(ans)