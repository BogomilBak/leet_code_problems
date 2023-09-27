class Solution(object):
    def majorityElement(self, nums):
        hash = {}

        for i in range(len(nums)):
            if nums[i] not in hash:
                hash[nums[i]] = nums.count(nums[i])
                if hash[nums[i]] > len(nums) / 2:
                    return nums[i]


x = Solution()
y = [3,2,3]
print(x.majorityElement(y))