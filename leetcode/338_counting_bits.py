# count set bits in n, log n complexity
def weight(n: int) -> int:
    out=0
    while n>0:
        out += n&1
        n >>= 1
    return out

n=5


# keep track of the largest power of two that has been seen, and the next to be seen
countlist =[0]
nextexp = 1
for i in range(1,n+1):
    if i == nextexp:
        countlist.append(1)
        curexp=nextexp
        nextexp*=2
    else:
        countlist.append(1+countlist[i-curexp])
print(countlist)


# brute force n log n complexity
countlist =[]
for i in range(0,n+1):
    countlist.append(weight(i))
print(countlist)
