def maxProfit(prices):
    l = len(prices)
    max_profit = 0
    for i in range(l+1):
        # [7, 1, 5, 3, 6]
        buy = prices[0:l - (i + 1)]
        # [1, 5, 3, 6, 4]
        sell = prices[i + 1:l]
        for b, s in zip(buy, sell):
            if s < b:
                continue
            else:
                profit = s - b
                if profit > max_profit:
                    max_profit = profit
    return max_profit


test = [7, 1, 5, 3, 6, 4]
# test = [7, 6, 4, 3, 1]
maxProfit(test)
