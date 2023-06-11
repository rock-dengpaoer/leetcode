# 暴力破解
def twoSum(nums, target):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            print(i, j)
            if nums[i] + nums[j] == target:
                result.append(i)
                result.append(j)
                return result



nums = [2, 7, 11, 15]
target = 9

result = twoSum(nums, target)
print(result)
