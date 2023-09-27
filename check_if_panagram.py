class Solution(object):
    def checkIfPangram(self, sentence):
        return len(set(sentence)) == 26

test = Solution()
a = "thequickbrownfoxjumpsoverthelazydog"
print(test.checkIfPangram(a))