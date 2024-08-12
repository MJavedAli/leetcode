def intToRoman(num: int) -> str:
    roman_map = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
        10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
        100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
        1000: 'M'
    }
    
    result = []
    values = sorted(roman_map.keys(), reverse=True)  
    
    for value in values:
        while num >= value:
            result.append(roman_map[value])
            num -= value
    
    return ''.join(result)

num = 3749
print(intToRoman(num))
