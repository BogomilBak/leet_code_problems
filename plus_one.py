class Solution(object):
    def plusOne(self, digits):
        finished, index = False, -1

        while not finished:
            if abs(index) <= len(digits):
                if digits[index] == 9:
                    digits[index] = 0
                    index -= 1
                else:
                    digits[index] += 1
                    finished = True
            else:
                digits.insert(0, 1)
                finished = True

        return digits


x = Solution()
print(x.plusOne([9]))