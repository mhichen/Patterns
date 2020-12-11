#!/usr/bin/python3

import numpy as np

# Given a string and pattern, find smallest substring
# which has all the characters of the given pattern

# Time Complexity: O(2N) -> O(N) where N is the length of the string
# Space Complexity: O(M) where M is the lenth of the pattern
def smallest_window_substring(st, pattern):

    # use hash table to track frequency of
    # characters in pattern
    freq = {}
    for p in pattern:
        if p not in freq:
            freq[p] = 0
        freq[p] += 1

    # Keep track of character matches
    match = 0

    # Keep track of min substring length
    min_len = np.inf
    min_j = -1
    min_i = -1

    for j in range(len(st)):

        if st[j] in freq:
            freq[st[j]] -= 1

            if freq[st[j]] == 0:
                match += 1

        if match == len(freq):
            min_len = min(min_len, j + 1)
            min_j = j


    for i in range(0, len(st) - len(pattern) + 1):

        if match == len(freq):
            min_len = min(min_len, j - i + 1)
            min_i = i

        if st[i] in freq:
            freq[st[i]] += 1

            if freq[st[i]] > 0:
                match -= 1


    if min_len is not np.inf:
        return st[min_i:min_j+1]
    else:
        return ""
    
    #return min_len
        



if __name__ == "__main__":

    S = "aabdec"
    pattern = "abc"

    # Expected output: "abdec"
    print("Smallest substring", smallest_window_substring(S, pattern))


    S = "abdbca"
    pattern = "abc"

    # Expected output: "bca"
    print("Smallest substring", smallest_window_substring(S, pattern))


    S = "adcad"
    pattern = "abc"

    # Expected output: ""
    print("Smallest substring", smallest_window_substring(S, pattern))
