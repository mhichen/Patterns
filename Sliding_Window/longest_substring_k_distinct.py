#!/usr/bin/python3

# Given a string, find the length of the longest substring
# in it with no more than K distinct characters
# This solution has time complexity O(N) and space complexity
# O(k)
def longest_substring_k_distinct(st, k):

    # dictionary / hash table to track distinct letters
    mdict = {}

    # max length of substring
    max_len = 0

    # index for beginning of window
    i = 0

    # j is index for end of window
    for j in range(len(st)): 

        if st[j] in mdict:
            mdict[st[j]] += 1
        else:
            mdict[st[j]] = 1

        # if number of distinct char in dictionary
        # is equal or less than k, we update max_len
        if len(mdict) <= k:
            max_len = max(max_len, j - i + 1)

        # otherwise, we need to increment i, before
        # which we update the dictionary to reflect
        # accurate count of each char
        else:
            if mdict[st[i]] == 1:
                del mdict[st[i]]
            else:
                mdict[st[i]] -= 1

            i += 1

    return max_len

if __name__ == "__main__":


    S = "araaci"
    k = 2

    # Expected output is 4 - araa
    print(longest_substring_k_distinct(S, k))


    S = "araaci"
    k = 1

    # Expected output is 2 - aa
    print(longest_substring_k_distinct(S, k))


    S = "cbbebi"
    k = 3

    # Expected output is 5 - cbbeb / bbebi
    print(longest_substring_k_distinct(S, k))
          
