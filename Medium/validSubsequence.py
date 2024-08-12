def isValidSubsequence(array, sequence):
    seqIdx = 0
    for value in array:
        if sequence[seqIdx] == value:
            seqIdx+=1
    
    return seqIdx == len(sequence)
        
def isSubsequence(s: str, t: str) -> bool:
    i, j = 0, 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == len(s)


array=[5,1,22,25,6,-1,8,10]
sequence=[1,6,-1,10] 
# print(isValidSubsequence(array,sequence))    
print(isSubsequence("abc","ahbgdc"))  