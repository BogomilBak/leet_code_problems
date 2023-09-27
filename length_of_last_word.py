class Solution(object):
    def lengthOfLastWord(self, s):
        return len(s.strip().split()[-1])



x = Solution()
y = "Hello World"
print(x.lengthOfLastWord(y))