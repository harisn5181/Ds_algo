#print minimum of array
import sys


def min_array(arr,smallest):
    if len(arr) ==0:
        print(smallest)
        return

    if arr [0] < smallest:
        smallest=arr[0]
    min_array(arr[1:],smallest)

min_array([10,330,-30,4,30],sys.maxsize)




#anothe approach



def printmin(l,minsofar=10000):
    if len(l) ==0:
        print(minsofar)
        return

    newmin=min(minsofar,l[0])
    printmin(l[1:],newmin)
#printmin([1,2,3,4,-1,0,2,-4,5,6])