def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()  # helps us skip a number we've already seen
    sols = set()
    for i, x in enumerate(nums):
        # if we've reached positives, then all negatives have been processed
        # every solution with a positive must have a negative
        # therefore if all negatives have been processed so have all positives
        if x > 0:
            break
        # skip if we just processed the same number
        if i > 0 and x == nums[i - 1]:
            continue
        target = 0 - x
        map = {}
        for j, y in enumerate(nums[i + 1:]):  # skip the numbers we already processed
            if target - y in map:
                thissol = [x, y, target - y]
                thissol.sort()
                thissoltuple = tuple(thissol)
                sols.add(thissoltuple)
            if y not in map:
                map[y] = j
    return list(sols)

sols=threeSum([-1,0,1,2,-1,-4])
print(sols)


x=[4,2,5,1,46]
x.sort()
print(x)