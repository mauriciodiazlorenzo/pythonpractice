# space O(1)
# time O(n)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        globmax = max(nums)
        # the key is to keep track of both the max and the min seen so far
        maxprod = 1
        minprod = 1
        for x in nums:
            prevmax=maxprod
            maxprod=max(x,x*maxprod,x*minprod)
            minprod=min(x,x*prevmax,x*minprod)
            globmax=max(globmax,maxprod)
        return globmax