from collections import Counter

def canConstruct(ransomNote, magazine):
    magazine_count = Counter(magazine)
    for letter in ransomNote:
        if magazine_count[letter] > 0:
            magazine_count[letter] -= 1
        else:
            return False
    return True    


print(canConstruct("sdz","asdfgbz"))    