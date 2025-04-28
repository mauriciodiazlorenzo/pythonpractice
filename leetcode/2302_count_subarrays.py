nums=[2,1,4,3,5]
k=10

# brute force
# score = 0
# for sub_length in range(1, len(nums) + 1):
#     cursum = sum(nums[0:0 + sub_length])
#     for start_ind in range(0, len(nums) - sub_length + 1):
#         if start_ind > 0:
#             cursum = cursum - nums[start_ind - 1] + nums[start_ind + sub_length - 1]
#         if sub_length * cursum < k:
#             score += 1
# print(score)

score = 0
li = 0
ri = 0
cursum = nums[0]
curlength = 1
while ri < len(nums):
    if cursum * curlength < k:
        score += ri - li + 1
        ri += 1
        if ri < len(nums):
            cursum += nums[ri]
            curlength += 1
    else:
        cursum -= nums[li]
        curlength -= 1
        li += 1
print(score)