class Solution(object):
    def twoSum(self, nums, target):
        x = {}
        for index, value in enumerate(nums):
            if target - value in x:
                return [x[target - value], index]
            x[value] = index

x = Solution()
print(x.twoSum([0,4,3,0], 0))