class Solution(object):
    def isValid(self, s):

        brackets = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        y = []

        for value in s:
            if value in brackets.values():
                y.append(value)
            elif y and brackets[value] == y[-1]:
                y.pop()
            else:
                return False

        return y == []
