






def printPermutations(strg, outputStrg = ""):
    #Implement Your Code Here
    if len(strg) == 0:
        print(outputStrg)
        return
    for i in range(len(strg)):
        temp = strg[: i] + strg[i + 1: ]
        printPermutations(temp, outputStrg + strg[i])
        

printPermutations("abc")
        
