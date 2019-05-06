# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Runtime: 44ms (80.50%)
# Memory: 13.9 MB (5.08%)

def maxProfit(prices):
    profit = 0
    minPrice = float('inf')
    print(minPrice)
    for price in prices:
        minPrice = min(minPrice, price)
        profit = max(profit, price - minPrice)
    return profit
