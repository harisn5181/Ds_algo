# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered. When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

def max_frequency(string):
    d={}
    for i in string:
        d[i] = d.get(i, 0) + 1



    max=0

    for i in d:
        if d[i] > max:
            max= d[i]
            max_key=i

    print(max_key)


#{2: 6, 12: 3, 11: 2, 1: 1, 6: 1}



max_frequency([2, 12, 2, 11, 12, 2 ,1 ,2 ,2, 11, 12, 2, 6 ])