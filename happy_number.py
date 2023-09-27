class Solution(object):
    def isHappy(self, n):
        digits = []

        while n >= 10:
            digits.append(n % 10)
            n = n // 10
        digits.append(n)

        iteration = 1000

        while not iteration == 0:
            result = sum([x**2 for x in digits])
            if result == 1:
                return True

            digits = []
            while result >= 10:
                digits.append(result % 10)
                result = result // 10
            digits.append(result)

            iteration -= 1

        return False



x = Solution()
z = 19
print(x.isHappy(19))