class Solution(object):
    def numberOfPairs(self, nums):
        # i = 0
        # result = 0
        # while len(set(nums)) != len(nums):
        #     if nums[i] in nums[i + 1:]:
        #         index = nums[i + 1:].index(nums[i])
        #         pass

        i = 0
        sorted_nums = sorted(nums)
        result = [0]

        while i < len(sorted_nums) - 1:
            if sorted_nums[i] == sorted_nums[i + 1]:
                result[0] += 1
                sorted_nums.remove(sorted_nums[i])
                sorted_nums.remove(sorted_nums[i])
                continue

            i += 1

        result.append(len(sorted_nums))

        return result

test = Solution()
a = [1,3,2,1,3,2,2]
print(test.numberOfPairs(a))
