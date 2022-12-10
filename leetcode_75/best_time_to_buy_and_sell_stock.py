
from typing import List

# Constraints
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104


# [7,1,5,3,6,4,20]
# my_profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min = prices[0]
        for item in prices:
            if item < min:
                min = item
            profit_if_i_sell_today = item - min
            if profit_if_i_sell_today > max_profit:
                max_profit = profit_if_i_sell_today
        return max_profit


r = Solution()
print(r.maxProfit([7, 1, 5, 3, 6, 4]))
