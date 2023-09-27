class Solution(object):
    def wordPattern(self, pattern, s):

        s = s.split()

        if len(pattern) != len(s):
            return False

        hash = {}

        for x in range(len(pattern)):
            if pattern[x] in hash:
                if hash[pattern[x]] != s[x]:
                    return False

            elif s[x] in hash.values():
                return False

            hash[pattern[x]] = s[x]

        return True



test = Solution()
a = "abba"
b = "dog dog dog dog"
print(test.wordPattern(a, b))

