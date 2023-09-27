class Solution(object):
    def numIdenticalPairs(self, nums):

        counter = 0

        for i in range(len(nums) - 1):
            counter += nums[i + 1:].count(nums[i])

        return counter

test = Solution()
a = [1,2,3,1,1,3]
print(test.numIdenticalPairs(a))

