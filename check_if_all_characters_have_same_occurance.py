class Solution(object):
    def areOccurrencesEqual(self, s):
        # hash = {}
        #
        # for i in range(len(s)):
        #     if s[i] in hash:
        #         continue
        #
        #     hash[s[i]] = s.count(s[i])
        #
        # if len(set(hash.values())) == 1:
        #     return True
        # return False

        l = []

        for i in set(s):
            l.append(s.count(i))

        if len(set(l)) != 1:
            return False
        return True

s = Solution()
a = "vvvvvvvvvvvvvvvvvvv"
print(s.areOccurrencesEqual(a))

