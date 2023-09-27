class Solution(object):
    def merge(self, nums1, m, nums2, n):
        x = nums1[:m]
        y = nums2[:n]

        nums1 = x + y
        nums1 = sorted(nums1)
        return


asd = Solution()
one = [1,2,3,0,0,0]
two = 3
three = [2,5,6]
four = 3

print(asd.merge(one, two, three, four))