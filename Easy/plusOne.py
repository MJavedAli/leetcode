def plusOne(digits):
    n=len(digits)
    print(n)
    sum=0
    for i in range(0,n):
        sum = sum+digits[i]*(10 ** (n-1-i))
    return [int(i) for i in str(sum+1)]


digits = [4,3,2,1]
s=plusOne(digits)
print(s)

    