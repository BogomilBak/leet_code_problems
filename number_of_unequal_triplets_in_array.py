class Solution(object):
    def unequalTriplets(self, nums):
        # ll = []
        #
        # i = 0
        #
        # while i < len(nums) - 2:
        #     j = i + 1
        #     while j < len(nums) - 1:
        #         k = j + 1
        #         while k < len(nums):
        #             if nums[i] != nums[j] != nums[k] != nums[i]:
        #                 ll.append([i, j, k])
        #             k += 1
        #         j += 1
        #     i += 1
        # return len(ll)

        result = 0
        n = len(nums)
        nums.sort()
        i = 0

        while i < n:
            ctr = 1
            while i < n - 1 and nums[i] == nums[i + 1]:
                ctr += 1
                i += 1
            i += 1
            result += (i - ctr) * ctr * (n - i)

        return result





test = Solution()
a = [4,4,2,4,3]
print(test.unequalTriplets(a))
