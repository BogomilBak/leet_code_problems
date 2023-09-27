from collections import deque


class Solution(object):
    def isPalindrome(self, x):
        y = str(x)
        z = y[::-1]
        middle = len(y) // 2

        for l in range(middle):
            left_value = y[l]
            right_value = z[l]
            if not left_value == right_value:
                return False

        return True


x = Solution()
print(x.isPalindrome(12001))

