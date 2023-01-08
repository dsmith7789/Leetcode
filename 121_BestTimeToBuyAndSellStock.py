class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # new window: next value is less than previous min
        # record last window's max range (max profit)
        # find maximum of all window max profits
        max_profit = 0
        window_min = prices[0]
        window_max = prices[0]
        window_max_profit = 0
        for i in range(len(prices)):
            if prices[i] < window_min:
                window_max_profit = window_max - window_min
                max_profit = max(max_profit, window_max_profit)
                window_min, window_max = prices[i], prices[i]  # "reset" window
                window_max_profit = 0
            elif prices[i] > window_max:
                window_max = prices[i]
                window_max_profit = window_max - window_min
        return max(max_profit, window_max_profit)
                    
