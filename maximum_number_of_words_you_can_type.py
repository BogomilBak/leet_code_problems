class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        result = 0
        brokenLetters = set(brokenLetters)
        for w in text.split():
            if len(set(list(w)).intersection(brokenLetters)) == 0:
                result += 1

        return result

test = Solution()
a = "hello world"
b = "ad"
print(test.canBeTypedWords(a, b))


