class Solution(object):
    # def smallerNumbersThanCurrent(self, nums):
    #     hash = {}
    #     result = []
    #
    #     for i in range(len(nums)):
    #         if nums[i] in hash:
    #             result.append(hash[nums[i]])
    #             continue
    #
    #         counter = 0
    #
    #         for j in range(len(nums)):
    #             if nums[i] > nums[j]:
    #                 counter += 1
    #
    #         hash[nums[i]] = counter
    #         result.append(counter)
    #
    #     return result

    def smallerNumbersThanCurrent(self, nums):
        temp = sorted(nums)
        mapping = {}
        result = []
        for i in range(len(temp)):
            if temp[i] not in mapping:
                mapping[temp[i]] = i
        for i in range(len(nums)):
            result.append(mapping[nums[i]])
        return result

test = Solution()
a = 8, 1, 2, 2, 3
print(test.smallerNumbersThanCurrent(a))

