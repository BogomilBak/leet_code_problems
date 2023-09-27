class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        i = 0
        counter = 0
        while i < len(nums) - 2:

            j = i + 1

            while j < len(nums) - 1:
                j += 1
                if nums[j - 1] != nums[i] + diff:
                    continue

                k = j

                while k < len(nums):
                    k += 1
                    if nums[k - 1] != nums[j - 1] + diff:
                        continue

                    counter += 1

            i += 1

        return counter



test = Solution()
a = [0,1,4,6,7,10]
b = 3
print(test.arithmeticTriplets(a, b))