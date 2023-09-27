class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        result = 0

        for i in range(len(nums) - 2):
            if nums[i] + diff in nums and nums[i] + 2 * diff in nums:
                result += 1

        return result