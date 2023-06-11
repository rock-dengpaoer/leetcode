# 哈希表
def twoSum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[num] = i


nums = [3, 3]
target = 6

result = twoSum(nums, target)
print(result)
