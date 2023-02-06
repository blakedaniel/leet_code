def maxProfit(prices):
    max_profit = 0
    buy = 0
    sell = buy + 1
    end = len(prices)
    while sell < end:
        if prices[sell] < prices[buy]:
            buy = sell
            sell = buy + 1
        else:
            profit = prices[sell] - prices[buy]
            max_profit = max(max_profit, profit)
            sell += 1
    return max_profit


# test = [7, 1, 5, 3, 6, 4]
# test = [7, 6, 4, 3, 1]
# test = [1, 2]  # output: 1
test = [7, 1, 5, 3, 6, 4, 0, 9]
maxProfit(test)
