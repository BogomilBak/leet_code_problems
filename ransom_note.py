class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        if len(ransomNote) > len(magazine):
            return False

        hash = {}

        for letter in magazine:
            if letter not in hash:
                hash[letter] = 1
            else:
                hash[letter] += 1

        for letter in ransomNote:
            if letter not in hash:
                return False

            hash[letter] -= 1

            if hash[letter] == 0:
                del hash[letter]

        return True

x = Solution()
y = 'aa'
z = 'ab'
print(x.canConstruct(y, z))