class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        a = set(nums1) and set(nums2)
        return set(nums1) & set(nums2) | set(nums2) & set(nums3) | set(nums1) & set(nums3)


test = Solution()
a = [1,1,3,2]
b = [2,3]
c = [3]
print(test.twoOutOfThree(a, b, c))

