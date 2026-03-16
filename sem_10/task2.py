s = input().split()

nums = []
for x in s:
    nums.append(int(x))

count = 0
#  0  1  2  3  4
# [3, 3, 3, 3, 3]
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            count += 1

print(count)