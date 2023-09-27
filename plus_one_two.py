class Solution(object):
    def plusOne(self, digits):
        digits = ''.join([str(x) for x in digits])
        digits = int(digits)
        digits += 1
        digits = str(digits)
        digits = list(digits)
        digits = [int(x) for x in digits]

        return digits