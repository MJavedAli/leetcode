def maximumGain(s: str, x: int, y: int) -> int:
    def removePair(pair,score):
        nonlocal s
        res=0
        stack=[]

        for c in s:
            if c==pair[1] and stack and c==pair[-1]:
                res+=score
                stack.pop()
            else:
                stack.append(c)
        s="".join(stack)





    res =0
    pair = "ab" if x>y else "ba"
    res+=removePair(pair,max(x,y))
    res+=removePair(pair[::-1],min(x,y))
    return res


s = "cdbcbaab"
x , y = 4, 5

print(maximumGain(s,x,y))


''' 
1717. Maximum Score From Removing Substrings

You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.

 

Example 1:

Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.
Example 2:

Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20
 

Constraints:

1 <= s.length <= 105
1 <= x, y <= 104
s consists of lowercase English letters.
'''