st = input().split(",")
res = [int(st[i]) for i in range(len(st))]


def validate(nums: list) -> bool:
    if len(nums) != 3:
        return False
    for i in nums:
        print(type(i))
        if not isinstance(i, int):
            return False
    return True

def solve(nums: list) -> int:
    if not validate(nums):
        return "invalid input"
    for i in range(len(nums) - 1):
        print(i)
        if nums[i] + 1 != nums[i+1]:
            return "unexpected error"

    return sum(nums)

print(solve(res))