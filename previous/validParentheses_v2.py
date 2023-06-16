# s = "()"
s = "()[]{}"
# s = "(]"
# s = '(('


def isValid(s: str) -> bool:
    open_brackets = ('(', '[', '{')

    opens = []
    for i in range(len(s)):
        if s[i] in open_brackets:
            opens.append(s[i])
        else:
            if len(opens) == 0:
                return False
            pair = opens.pop() + s[i]
            # if 0 < ord(cur_closed) - ord(last_open) <= 2:
            #     continue
            breakpoint()
            if pair in ('()', '[]', '{}'):
                continue
            else:
                return False
    return len(opens) == 0

isValid(s)