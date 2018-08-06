# 003. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


def longest_substring_length(s):
    """
    :param s: string
    :return: int
    ===========================
    returns length of longest substring without repeating characters
    """
    start = 0
    max_length = 0
    char_index = {}  # key:val => character:index

    for i, ch in enumerate(s):

        if ch in char_index and start <= char_index[ch]:
            start = char_index[ch]+1

        else:
            max_length = max(max_length, i-start+1)

        char_index[ch] = i

    return max_length


if __name__ == "__main__":
    # Given "abcabcbb", the answer is "abc", with the length of 3.
    # Given "bbbbb", the answer is "b", with the length of 1.
    # Given "pwwkew", the answer is "wke" or "kew", with the length of 3.

    result1 = longest_substring_length("abcabcbb")
    result2 = longest_substring_length("bbbbb")
    result3 = longest_substring_length("pwwkew")

    print(result1, result2, result3)  # should print 3 1 3
