# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
# Note that you cannot sell a stock before you buy one.
#
# Example 1:
#
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Not 7-1 = 6, as selling price needs to be larger than buying price.
#
# Example 2:
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
#

class Solution(object):

    # Naive solution would be to start on day 1, and compare it against the remaining days.
    # see which one yields the highest profit (buy, then sell, so sell-buy)
    # time complexity O(N^2) because we are looping through the array for each element
    # space complexity O(1) We need to save the value of profit and compare it to see which is highest
    # edge cases: empty array, if max profit is negative or zero no transaction is done.
    def max_profit(self, prices):
        if len(prices) < 1:
            return 0
        max_profit = 0
        for x in range(len(prices)):
            for y in range(x + 1, len(prices)):
                if prices[y] - prices[x] > max_profit:
                    max_profit = prices[y] - prices[x]
        return max_profit

    # Time Complexity O(N)
    # space complexity O(1), the space does not increase with the size of the input
    def max_profit_2(self, prices):
        if len(prices) < 1:
            return 0
        max_profit = 0
        min_price = prices[0]
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit


if __name__ == '__main__':
    input = [7, 1, 5, 3, 6, 4]
    input = [7, 6, 4, 3, 1]
    ret = Solution.max_profit_2(0, input)
    print(ret)
