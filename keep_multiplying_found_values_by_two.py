class Solution(object):
    def findFinalValue(self, nums, original):
        while original in nums:
            nums.remove(original)
            original *= 2

        return original

