def lengthOfLastWord(s: str) -> int:
    pstr=[]
    for i in s.split(" "):
        if i!='':
            pstr.append(i)

    return len(pstr.pop())
           




s = "   fly me   to   the moon  "
lengthOfLastWord(s)