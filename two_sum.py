class Solution(object):
    def twoSum(self, nums, target):
        x = {}
        for index, value in enumerate(nums):
            if target - value in x:
                return [x[target - value], index]
            x[value] = index

test = Solution()
a = [2,7,11,15]
b = 9
print(test.twoSum(a, b))