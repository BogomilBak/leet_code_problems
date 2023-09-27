class Solution(object):
    def maxProfit(self, prices):
        best_result = 0

        min_value = min(prices)
        max_value = max(prices)

        if prices.index(min_value) < prices.index(max_value):
            return max_value - min_value

        for first_day in range(len(prices) - 1):

            for second_day in range(first_day + 1, len(prices)):

                first_value = prices[first_day]
                second_value = prices[second_day]

                if first_value < second_value and second_value - first_value > best_result:
                    best_result = second_value - first_value

        return best_result


x = Solution()
print(Solution.maxProfit(x, [7,1,5,3,6,4]))