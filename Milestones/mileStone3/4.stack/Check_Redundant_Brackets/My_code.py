from sys import stdin


def checkRedundantBrackets(Str):

    st = []
    for ch in Str:

        if (ch == ')'):
            count=0

            while (top != '('):
                top = st[-1]
                st.pop()
                count=count+1
            if count==0:
                return true

            if (flag == True):
                return True

        else:
            st.append(ch)

    return False


# main
expression = stdin.readline().strip()

if checkRedundantBrackets(expression):
    print("true")

else:
    print("false")