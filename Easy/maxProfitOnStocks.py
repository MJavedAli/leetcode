from typing import List


def maxProfit(prices: List[int]) -> int:
    min_price=float('inf')
    max_profit=0
    for price in prices:
        if price<min_price:
            min_price=price
        elif price-min_price>max_profit:
            max_profit=price-min_price

    return max_profit

def maxProfit2(prices: List[int]) -> int:
    total_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            total_profit += prices[i] - prices[i - 1]
    
    return total_profit 


prices = [7,1,5,3,6,4]
print(maxProfit2(prices))
