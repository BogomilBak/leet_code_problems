class Solution(object):
    def kthDistinct(self, arr, k):
        hash_ignore = {}
        for l in arr:
            if l in hash_ignore:
                continue
            if arr.count(l) > 1:
                hash_ignore[l] = True
                continue
            k -= 1
            if k == 0:
                return l
        return ""


test = Solution()
a = ["d","b","c","b","c","a"]
b = 2
print(test.kthDistinct(a, b))
