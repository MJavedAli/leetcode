def romanToInt(self, s: str) -> int:
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num =0

    s=s.replace("IV","IIII").replace("IX","VIIII").replace("XL","XXXXX").replace("XC","LCCCC").replace("CD", "CCCC").replace("CM", "DCCCC")

    for i in s:
        num +=roman_map["i"]
    return num
