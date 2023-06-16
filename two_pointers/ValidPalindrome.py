# A phrase is a palindrome if, after converting all uppercase letters into lowercase
# letters and removing all non-alphanumeric characters, it reads the same forward and
# backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

s = "A man, a plan, a canal: Panama"
# s = "race a car"
# s = " "

def isPalindrome(s: str) -> bool:
    s = s.lower()
    s = [c for c in s if c.isalnum()]
    p1 = 0
    p2 = len(s) - 1

    while p1 < p2:
        if s[p1] != s[p2]:
            return False
        p1 += 1
        p2 -= 1
    return True

isPalindrome(s)