class Solution(object):
    def numberOfPoints(self, nums):
        hash_set = set()

        for x, y in nums:
            for a in range(x, y + 1):
                hash_set.add(a)

        return len(hash_set)

test = Solution()
a = [[3,6],[1,5],[4,7]]
print(test.numberOfPoints(a))