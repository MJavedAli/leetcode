def survivedRobotsHealths(positions, healths, directions):

    index_map = {p:i for i,p in enumerate(positions)}
    stack = []

    for p in sorted(positions):
        i = index_map[p]

        if directions[i]=="R":
            stack.append(i)
        else:
            while stack and directions[stack[-1]]=="R" and healths[i]:
                i2 = stack.pop()
                if healths[i]> healths[i2]:
                    healths[i2]=0
                    healths[i]-=1
                elif healths[i]<healths[i2]:
                    healths[i]=0
                    healths[i2]-=1
                    stack.append(i2)
                else:
                    healths[i]=healths[i2]=0
            if healths[i]:
                stack.append(i)    

    return [h for h in healths if h>0]


positions = [3,5,2,6]
healths=[10,10,15,12]
directions ="RLRL"

print(survivedRobotsHealths(positions,healths,directions))