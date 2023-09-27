class Solution(object):
    def singleNumber(self, nums):

        hash = set()

        for x in nums:
            if x not in hash:
                hash.add(x)
            else:
                hash.remove(x)

        result = [x for x in hash]

        return result[0]


solution = Solution()
numz = [4,1,2,1,2]
print(solution.singleNumber(numz))