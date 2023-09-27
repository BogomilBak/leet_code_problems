class Solution(object):
    def isIsomorphic(self, s, t):

        def helper(word):
            output, lookup = [], {}
            i = 1
            for w in word:
                if w not in lookup:
                    lookup[w] = i
                    i += 1
                output.append(lookup[w])
            return output


        return helper(s) == helper(t)


test = Solution()
test_1 = "bbbaaaba"
test_2 = "aaabbbba"
print(test.isIsomorphic(test_1, test_2))

