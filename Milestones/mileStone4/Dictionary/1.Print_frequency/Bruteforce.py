




s=" this is a word string having many many word"

k=2

words=s.split()
print(words)

d={}

# for w in words:
#     if w in d:
#         d[w]=d[w]+1
#     else:
#         d[w] =1
#

#alternative apporach

for w in words:
    d[w]=d.get(w,0)+1


for w in d:
    if d[w] == k:
        print(w)