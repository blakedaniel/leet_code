
s = 'cat'
t = 'atc'


def letterCount(word):
    count = {}
    for char in word:
        count[char] = count.get(char, 0) + 1
    return count


s_count = letterCount(s)
t_count = letterCount(t)
print(s_count)
print(t_count)

def isAnagram():
    if s_count != t_count:
        return False
    else:
        return True


isAnagram()