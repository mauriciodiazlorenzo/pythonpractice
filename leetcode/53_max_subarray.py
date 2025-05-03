class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # essentially compute the integral
        # then take the max - min of the integral from left to right
        maxsum = -1E5
        min = 0
        maxval = -1E5
        runsum = 0
        min_ind = 0

        # edge case of only one element
        if len(nums) == 1:
            return nums[0]

        # edge case of all negtive elements
        if max(nums) <= 0:
            return max(nums)

        for x in nums:
            runsum += x
            if runsum < min:
                min = runsum
                maxval = min
            if runsum > maxval:
                maxval = runsum
            if maxval - min > maxsum:
                maxsum = maxval - min
        return maxsum
