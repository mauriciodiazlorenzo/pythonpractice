class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while True:
            mid = int((left+right)/2)
            if nums[right]==target:
                return right
            elif nums[left]==target:
                return left
            elif nums[mid]==target:
                return mid
            else:
                if nums[left]<target and target<nums[mid]:
                    right=mid
                elif nums[mid]<target and target<nums[right]:
                    left=mid
                elif nums[left]>nums[mid]: # broken on the left
                    right=mid
                else:
                    left=mid
            if right-left<=1:
                return -1