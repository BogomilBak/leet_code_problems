class Solution(object):
    def decodeMessage(self, key, message):
        hash = {' ': ' '}
        letter = 97

        for element in key:
            if element in hash or element == ' ':
                continue

            hash[element] = chr(letter)
            letter += 1

        return ''.join([hash[i] for i in message])





test = Solution()
a = "the quick brown fox jumps over the lazy dog"
b = "vkbs bs t suepuv"
print(test.decodeMessage(a, b))

