def reverseWords(s: str) -> str:
    words = s.split()[::-1]
    res=''
    for i in words:
        res=res+i+' '
    return res[:-1]





s = "the sky is  blue"
print(reverseWords(s))
