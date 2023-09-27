class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        result = 0

        for i in range(len(words)):
            if words[i][::-1] in words[i + 1:]:
                result += 1

        return result


test = Solution()
a = ["cd","ac","dc","ca","zz"]
print(test.maximumNumberOfStringPairs(a))

