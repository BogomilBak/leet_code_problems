class Solution(object):
    def minimumOperations(self, nums):
        counter = 0
        temp_nums = [x for x in nums if x != 0]
        len_nums = len(temp_nums) * [0]
        while temp_nums != len_nums:
            try:
                min_number = min(x for x in temp_nums if x > 0)
            except ValueError:
                break
            temp_nums = [x - min_number for x in temp_nums]
            counter += 1
        return counter

test = Solution()
a = [1,5,0,3,5]
print(test.minimumOperations(a))
