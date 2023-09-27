class Solution(object):
    def repeatedNTimes(self, nums):
        n = len(nums) / 2

        for x in set(nums):
            if nums.count(x) == n:
                return x
