class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        div = 1
        while x >= 10 * div:
            div *= 10

        while x:
            right = x % 10
            left = x // div

            if left != right:
                return False

            x = (x % div) // 10
            div /= 100

        return True


x = Solution()
print(x.isPalindrome(12001))

