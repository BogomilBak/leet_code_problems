class Solution(object):
    def removeDuplicates(self, nums):
        n = 0
        hash = {}

        for i in range(len(nums)):
            if nums[i] not in hash:
                hash[nums[i]] = True
                continue
            else:
                nums[i] = float('inf')
                n += 1

        nums.sort()
        return len(nums) - n


x = Solution()
y = [0,0,1,1,1,2,2,3,3,4]
print(x.removeDuplicates(y))
