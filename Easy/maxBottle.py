def numWaterBottles(numBottles: int, numExchange: int) -> int:
    return numBottles + (numBottles-1)//(numExchange-1)




print(numWaterBottles(15,4))


#  9/3 = 3
# 9+3+1 =13

# 15/4 !=0 , 15+(15%4) = 15+3 =18, 18/4 = 4 + 2 = 6 
# 

