class Solution(object):
    def wordPattern(self, pattern, s):

        if len(pattern) != len(s.split()):
            return False

        pattern_list, pattern_hash,  = [], {}
        string_list, string_hash = [], {}

        i = 1

        for x in pattern:
            if x in pattern_hash:
                pattern_list.append(pattern_hash[x])
                continue

            pattern_hash[x] = i
            pattern_list.append(i)
            i += 1

        i = 1

        for x in s.split():
            if x in string_hash:
                string_list.append(string_hash[x])
                continue

            string_hash[x] = i
            string_list.append(i)
            i += 1

        return string_list == pattern_list

test = Solution()
a = "abba"
b = "dog cat cat dog"
print(test.wordPattern(a, b))

