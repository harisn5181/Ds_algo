with open('readme.txt', 'w') as f:
    for i in range(200000):
        f.write(str(i))
        f.write(" ,")

