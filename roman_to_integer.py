class Solution(object):
    def romanToInt(self, s):
        help_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        result = 0
        for i in range(len(s)):
            if i + 1 < len(s) and help_dict[s[i]] < help_dict[s[i + 1]]:
                result -= help_dict[s[i]]
            else:
                result += help_dict[s[i]]

        return result


x = Solution()
y = "MCMXCIV"
print(x.romanToInt(y))