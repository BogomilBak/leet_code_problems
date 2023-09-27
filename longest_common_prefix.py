class Solution(object):
    def longestCommonPrefix(self, strs):
        sorted_strs = sorted(strs, key=lambda x: len(x))
        result = ''

        i, j, k = 0, 1, 0

        while k < len(sorted_strs[0]):

            letter = sorted_strs[i][k]

            while j < len(sorted_strs) and sorted_strs[j][k] == letter:
                j += 1

            if j == len(sorted_strs):
                result += letter
                k += 1
                j = 0
                continue

            else:
                break

        return result


x = Solution()
y = ["flower","flow","flight"]
print(x.longestCommonPrefix(y))
