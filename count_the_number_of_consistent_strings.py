class Solution(object):
    def countConsistentStrings(self, allowed, words):
        allowed = set(allowed)
        counter = 0
        for w in words:
            for l in w:
                if l not in allowed:
                    counter += 1
                    break

        return len(words) - counter

test = Solution()
a = "ab"
b = ["ad","bd","aaab","baa","badab"]
print(test.countConsistentStrings(a, b))

