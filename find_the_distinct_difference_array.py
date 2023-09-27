class Solution(object):
    def distinctDifferenceArray(self, nums):
        res = []
        for i in range(len(nums)):
            prefix = len(set(nums[i + 1:]))
            suffix = len(set(nums[:i + 1]))

            res.append(suffix - prefix)

        return res

test = Solution()
a = [3,2,3,4,2]
test.distinctDifferenceArray(a)