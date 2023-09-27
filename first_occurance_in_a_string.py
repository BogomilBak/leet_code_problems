class Solution(object):
    def strStr(self, haystack, needle):
        if needle not in haystack:
            return -1

        for i in range(len(haystack)):
            j = 0
            l = i
            if haystack[l] == needle[j]:
                while haystack[l] == needle[j]:
                    j += 1
                    l += 1
                    if j == len(needle):
                        return i






x = Solution()
y = "sadbutsad"
z = "sad"
print(x.strStr(y, z))
