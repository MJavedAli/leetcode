from typing import List


def minOperations(logs: List[str]) -> int:

    level=0

    for i in range(len(logs)):
        if logs[i]!="./" and logs[i]!="../":
            level+=1
        elif logs[i]=="../" and level!= 0:
            level-=1
    return level            








logs = ["d1/","../","../","../"]

print(minOperations(logs))