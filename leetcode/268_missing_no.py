class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        # if all numbers were present, the array would sum to n*(n+1)/2, so we know the target
        # take the target minus the sum of numbers actually in the array to get the missing integer
        # to save computation, perform both steps at once
        for ind, val in enumerate(nums):
            sum += ((ind + 1) - val)
        return sum
