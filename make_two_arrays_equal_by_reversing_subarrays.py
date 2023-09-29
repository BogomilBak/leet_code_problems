class Solution(object):
    def canBeEqual(self, target, arr):
        return sorted(target) == sorted(arr)

test = Solution()
a = [3,7,9]
b = [3,7,11]
print(test.canBeEqual(a, b))