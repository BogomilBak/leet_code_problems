class Solution(object):
    def digitCount(self, num):
        for i in range(len(num)):
            if int(num[i]) != num.count(str(i)):
                return False
        return True

test = Solution()
a = "1210"
print(test.digitCount(a))