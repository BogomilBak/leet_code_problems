class Solution(object):
    def removeDuplicates(self, nums):

        result_set = set()

        for x in range(len(nums)):
            if nums[x] in result_set:
                nums[x] = 9999
                continue

            result_set.add(nums[x])

        nums.sort()

        return len(result_set)
