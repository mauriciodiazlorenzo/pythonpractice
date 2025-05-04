# time O(n)
# space O(1)
def maxArea(self, height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    maxwater = 0
    while left < right:
        maxwater = max(maxwater, (right - left) * min(height[left], height[right]))
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
    return maxwater
    # the hard part is proving that this outside in approach, always moving the small wall inwards,
    # results in finding the best solution