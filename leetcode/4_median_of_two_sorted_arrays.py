nums1 = [1,2]
nums2 = [3,4]
totnum = len(nums1)+len(nums2)
partnum = totnum/2
prevnum=[0,0]
ind1 =0
ind2 =0
while True:
    if ind1 == len(nums1):
        nextnum=nums2[ind2]
        ind2 += 1
    elif ind2 == len(nums2):
        nextnum=nums1[ind1]
        ind1 += 1
    elif nums1[ind1]<=nums2[ind2]:
        nextnum=nums1[ind1]
        ind1 += 1
    else:
        nextnum=nums2[ind2]
        ind2 += 1
    prevnum[1] = prevnum[0]
    prevnum[0] = nextnum
    if ind1+ind2>partnum:
        if totnum%2==0:
            print((prevnum[0]+prevnum[1])/2)
        else:
            print(prevnum[0])
        break
