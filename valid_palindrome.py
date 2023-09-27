class Solution(object):
    def isPalindrome(self, s):

        s_lower = [x.lower() for x in s if x.isalnum()]

        message_1 = ''.join(s_lower)
        message_2 = message_1[::-1]

        return message_1 == message_2


x = Solution()
y = "race a car"
print(x.isPalindrome(y))