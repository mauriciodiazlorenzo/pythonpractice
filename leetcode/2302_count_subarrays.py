nums=[21,11,13,15,16,21,8,9,6,21]
k=2
mx = max(nums)
mx_in_window = 0
start = -1
end = 0
out = 0
while end < len(nums):
    if nums[end] == mx:
        mx_in_window += 1
        if mx_in_window >= k:
            start += 1
            while nums[start] != mx:
                start += 1
    if mx_in_window >= k:
        out += start + 1
    end += 1
print(out)