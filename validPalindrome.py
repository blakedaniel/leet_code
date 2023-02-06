def alphaNum(char):
    char = ord(char.lower())
    letters = set(range(ord('a'), ord('z')))
    numbers = set(range(ord('0'), ord('9')))
    alphanum = letters.union(numbers)
    return char in alphanum


def validPalindrome(s=''):
    l_index, r_index = 0, len(s) - 1
    while l_index < r_index:
        while alphaNum(s[l_index]) == False:
            l_index += 1
        while alphaNum(s[r_index]) == False:
            r_index -= 1
        if s[l_index].lower() != s[r_index].lower():
            return False
        else:
            l_index += 1
            r_index -= 1
    return True


test = 'momm'

validPalindrome(test)

''
