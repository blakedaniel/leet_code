import re
"""
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string ''.

The testcases will be generated such that the answer is unique.
"""
## insights
# if m (len(s)) < n (len(t)) => ''
# if there are two possible windows, return shortest windwo

## examples
# s: 'abcde'; t: 'cde' => 'cde'
# s: 'acabcac' t: 'abc' => 'abc'
# s: 'acabdcac' t: 'abc' => 'abdc : 5

# approachs
## two two-pointers, left: first (s and t), right: last (s and t)
## move left pointer on s until the char == left pointer of t
## move right pointer on s until the char = right pointer of t

def minWindow(s: str, t: str) -> str:
    min_substring = ''
    pos = 0
    pattern = re.compile('.*'.join([char for char in t]))
    while pos < len(s) - len(t):
        substring = pattern.search(s, pos=pos)
        if substring and (min_substring == '' or len(substring.string) < len(min_substring)):
            min_substring = substring.string
            pos = substring.pos + 1
            # breakpoint()
        else:
            pos += 1
    return min_substring
    


s = 'acabdcac'
t = 'abc'
print(minWindow(s, t))