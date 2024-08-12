def isPalindrome(s: str) -> bool:
    filtered_chars = [char.lower() for char in s if char.isalnum()]

    return filtered_chars == filtered_chars[::-1]



s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))