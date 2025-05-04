nums = [4,5,6,7,0,1,2]

# Time O(log n)
# Space O(1)

left=0
right=len(nums)-1
while True:
    mid = int((left+right)/2)
    # supposed to be in ascending order, so wherever descent occurs is the min
    # equality catches the single element edge case
    if (nums[right-1]>=nums[right]):
        return nums[right]
    elif (nums[left-1]>=nums[left]):
        return nums[left]
    else:
        if nums[mid]>nums[left]: # in order from left to mid, so the break must be on the right
            left=mid
        else: # not in order from left to mid, so the break is on the left
            right=mid
