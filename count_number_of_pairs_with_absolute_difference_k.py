class Solution(object):
    def countKDifference(self, nums, k):
        result = 0

        for i in range(len(nums)):
            if nums[i] + k in nums:
                result += nums.count(nums[i] + k)

        return result

test = Solution()
a = [1,2,2,1]
b = 1
print(test.countKDifference(a, b))