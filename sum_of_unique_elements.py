class Solution(object):
    def sumOfUnique(self, nums):
        return sum(set(x for x in nums if nums.count(x) == 1))


test = Solution()
a = [1,2,3,2]
print(test.sumOfUnique(a))
