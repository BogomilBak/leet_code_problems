class Solution(object):
    def isAnagram(self, s, t):

        return sorted(s) == sorted(t)

x = Solution()
print(x.isAnagram("anagram", "nagaram"))
