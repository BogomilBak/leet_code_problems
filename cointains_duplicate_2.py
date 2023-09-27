class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        d = {}

        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = [i]
            else:
                for q in d[nums[i]]:
                    if abs(q - i) <= k:
                        return True
                d[nums[i]].append(i)

        return False


x = Solution()
y = [1,0,1,1]
z = 1
print(x.containsNearbyDuplicate(y, z))

