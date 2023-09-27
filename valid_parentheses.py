from collections import deque


class Solution(object):
    def isValid(self, s):

        brackets = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        x = deque(s)
        y = []

        while x:
            element = x.popleft()

            if element in brackets:
                if not y:
                    return False

                last_bracket = y.pop()

                if last_bracket != brackets[element]:
                    return False

            else:
                y.append(element)

        if not y:
            return True

z = Solution()
print(z.isValid("()[]{}"))