"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock

IDEA:
Sliding windows: initial window of [0,1] then extend

7 3 2 5 4 6 1 8 9
b s                buy > sell -> no
  b s              buy > sell -> no
    b s            buy < sell -> profit = 3 -> max
    b   s          buy < sell -> profit = 2
    b     s        buy < sell -> profit = 4 -> max
    b       s      buy > sell -> no
            b s    buy < sell -> profit = 7 -> max
            b   s  buy < sell -> profit = 8 -> max
"""


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    buy, sell = 0, 1
    max_profit = 0

    while sell < len(prices):
        if prices[sell] > prices[buy]:  # we want profit
            max_profit = max(max_profit, prices[sell] - prices[buy])
        else:
            buy = sell
        sell += 1

    return max_profit


if __name__ == '__main__':
    prices = [7, 3, 2, 5, 4, 6, 1, 8, 9]
    res = maxProfit(prices)
    print(res)
