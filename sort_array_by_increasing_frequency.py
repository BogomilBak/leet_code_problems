class Solution(object):
    def frequencySort(self, nums):
        return sorted(nums[::-1], key=lambda x: nums.count(x))



test = Solution()
a = [1,1,2,2,2,3]
print(test.frequencySort(a))

