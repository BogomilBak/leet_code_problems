class Solution(object):
    def removeElement(self, nums, val):
        n = 0

        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = float('inf')
                n += 1
        nums.sort()
        return(len(nums) - n)

x = [3,2,2,3]
y = 3
z = Solution()
print(z.removeElement(x, y))
