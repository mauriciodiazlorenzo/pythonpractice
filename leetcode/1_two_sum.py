
# use hashmap to store seen values as the map's key, and store the index as the map's value
# time: O(n) space: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, ni in enumerate(nums):
            targ = target-ni
            if targ in map:
                return map[targ],i
            map[ni]=i
        return

# brute force
# time: O(n^2) space: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, ni in enumerate(nums):
            jtarg = target-ni
            for j in range(i+1,len(nums)):
                if nums[j]==jtarg:
                    return i,j
        return