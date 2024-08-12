from typing import List


def averageWaitingTime(customers: List[List[int]]) -> float:
        totalWaitTime = 0
        nextAvailableTime = 0
        
        for arrival, cookTime in customers:
            if arrival >= nextAvailableTime:
                totalWaitTime += cookTime
                nextAvailableTime = arrival + cookTime
            else:
                totalWaitTime += (nextAvailableTime - arrival) + cookTime
                nextAvailableTime += cookTime
        
        averageTime = totalWaitTime / len(customers) 
        return averageTime


c1 = [[1,2],[2,5],[4,3]]
c2=[[5,2],[5,4],[10,3],[20,1]]
c3 = [[2,3],[6,3],[7,5],[11,3],[15,2],[18,1]]


print(averageWaitingTime(c3))