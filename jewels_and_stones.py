class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        result = 0

        for jewel in jewels:
            if jewel in stones:
                result += stones.count(jewel)

        return result


    

