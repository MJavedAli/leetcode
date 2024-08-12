def strStr(haystack: str, needle: str) -> int:
    w = haystack.split(needle)
    print(w)
    index=0
    for i in w:
        if i=='':
            return index
        index=index+len(i)






haystack = "butsad"
needle = "sad"

print(strStr(haystack,needle))