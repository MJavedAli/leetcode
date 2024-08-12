def isHappy(n):
    def get_next(number):
        return sum(int(char) ** 2 for char in str(number))

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    
    return n == 1


print(isHappy(19))