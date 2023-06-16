# s = '()[]{}'
s = '([)]'
# s = '[({[]})]({})'


def isValid(string=''):
    # when open bracket found, add to dictionary and add everything until it closes
    pairings = {}
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            cur_bracket = ord(s[i])
            j = i + 1
            pairings[i] = s[i]
            closing = (cur_bracket + 1, cur_bracket + 2)
            while (ord(s[j]) not in closing):
                sub_bracket = ord(s[j])
                if j == len(s) - 1:
                    return False
                pairings[i] += s[j]
                j += 1
        # when a set of brackets closes, check that all enclosed brackets have a pair
            if j - i % 2 == 0:
                isValid(pairings[i])
        # check that a bracket closes by comparing the index of the open bracket to the key
        # until the last closing bracket or an unclosed bracket is found
    return True


isValid(s)


# ord('[') -> 91
# ord(']') -> 93

# ord('(') -> 40
# ord(')') -> 41

# ord('{') -> 123
# ord('}') -> 125
