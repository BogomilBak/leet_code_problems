class Solution(object):
    def repeatedCharacter(self, s):
        #
        # hash_map = {}
        #
        # for i in range(len(s) - 1):
        #     if not s[i] in s[i + 1:] or s[i] in hash_map:
        #         continue
        #
        #     for j in range(i + 1, len(s)):
        #         if s[i] == s[j]:
        #             hash_map[s[i]] = j
        #             break
        #
        # hash_map_sorted = sorted(hash_map.items(), key=lambda x: x[1])
        #
        # for key, value in hash_map_sorted:
        #     return key

        hash_map = {}

        for c in s:
            if c not in hash_map:
                hash_map[c] = True
                continue
            return c


test = Solution()
a = "abccbaacz"
print(test.repeatedCharacter(a))

