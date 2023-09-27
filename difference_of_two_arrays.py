class Solution(object):
    def findDifference(self, nums1, nums2):
        x = set(nums1)
        y = set(nums2)

        return [list(x -y), list(y - x)]

        # return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]


test = Solution()
a = [1,2,3,3]
b = [1,1,2,2]
print(test.findDifference(a, b))