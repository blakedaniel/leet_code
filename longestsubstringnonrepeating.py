def lengthOfLongestSubstring(s: str) -> int:
    # initialize: left, right, longest_length_n, longest_length_c
    # output: longest_length_n
    # "abcabcbb"
    # ab (2) -> abc (3) -> abca | -> 3
    # keep LEFT at 0 position, while moving RIGHT 1 space until dup found
    # calculate length of string, if greater than max, replace

    left = 0
    right = 1
    longest_length_n = 0
    longest_length_c = set()
    while left < len(s):
        if s[left] not in longest_length_c and s[right] not in longest_length_c:
            longest_length_c.add(s[left])
            longest_length_c.add(s[right])
            right += 1
        else:
            max(longest_length_n, len(s[left:right]))
            longest_length_c.remove(s[left])
            left += 1
    return longest_length_n


test = "abcabcbb"
lengthOfLongestSubstring(test)
