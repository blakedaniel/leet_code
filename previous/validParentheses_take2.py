s = '()[]{}'
# s = '[({})]'
# = '([)]'
# s = '[({[]})]({})'


def isValid(string=''):
    open_brackets = ('(', '[', '{')
    opens = []
    for i in range(len(s)):
            if s[i] in open_brackets:
                opens.append(s[i])
            else:
                if len(opens) == 0:
                    return False
                last_open = opens.pop()
                if 0 < ord(s[i]) - ord(last_open) <= 2:
                    continue
                else:
                    return False
        if len(opens) == 0:
            return True
        else:
            return False


isValid(s)


