

def profit(prices):
    # buy_index = 0
    # sell_index = len(prices)
    profit = 0
    for buy_index, buy_price in enumerate(prices):
        for sell_index, sell_price in enumerate(prices[buy_index:len(prices)]):
            profit = max(sell_price - buy_price, profit)
    return profit



# prices = [7,1,5,3,6,4]
# Output: 5
# prices = [7,6,4,3,1]
# result 0
prices = [2, 1, 3, 5]

print(profit(prices))
