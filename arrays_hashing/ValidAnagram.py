# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly once.

# cases to consider:
# - a letter in 's' and not in 't' and vv
# - more of letter x in 's' than in 't' and vv
# - 

from collections import defaultdict
import time

# s, t = "anagram", "nagaram"
# s, t = "rat", "car"
# s, t = 'car', 'carr'
# s, t = 'abc', 'edf'

test = (
    ("anagram", "nagaram", True),
    ("rat", "car", False),
    ('car', 'carr', False),
    ('car', 'crr', False),
    ('abc', 'def', False)
)

# by defaultdict hashmap
def isAnagram1(s: str, t: str) -> bool:
    hashmap_s = defaultdict(list)
    hashmap_t = defaultdict(list)
    if len(s) == len(t):
        for char_s, char_t in zip(s, t):
            hashmap_s[char_s].append(char_s)
            hashmap_t[char_t].append(char_t)
        return hashmap_s == hashmap_t
    return False


# by defaultdict hashmap_v2
def isAnagram2(s: str, t: str) -> bool:
    hashmap_s = defaultdict(list)
    hashmap_t = defaultdict(list)
    if len(s) == len(t):
        for i in range(len(s)):
            hashmap_s[s[i]].append(s[i])
            hashmap_t[t[i]].append(t[i])
        return hashmap_s == hashmap_t
    return False

# by defaultdict hashmap_v3
def isAnagram3(s: str, t: str) -> bool:
    if len(s) == len(t):
        hashmap_s = {}
        hashmap_t = {}
        for i in range(len(s)):
            hashmap_s[s[i]] = hashmap_s.get(s[i], 0) + 1
            hashmap_t[t[i]] = hashmap_t.get(t[i], 0) + 1
        return hashmap_s == hashmap_t
    return False

funcs = (isAnagram1, isAnagram2, isAnagram3)

for func in funcs:
    stime = time.time()
    for s, t, op in test:
        print(func(s, t) == op, (s, t))
        print(func(t, s) == op, (t, s))
    ttime = time.time() - stime
    print('Run Time: ', ttime, '\n')