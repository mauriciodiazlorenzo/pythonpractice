# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# a couple of edge cases around the number of zeroes within the array
# time: O(n)
# space: O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totprod=1
        zerocount=0
        for x in nums:
            if x!=0:
                totprod *= x
            else:
                zerocount+=1
        outarray=[]
        if zerocount>1:
            return [0 for x in range(len(nums))]
        for ind, x in enumerate(nums):
            if x==0:
                outarray.append(int(totprod))
            else:
                if zerocount==0:
                    outarray.append(int(totprod/x))
                else:
                    outarray.append(0)
        return outarray