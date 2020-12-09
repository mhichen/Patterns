#!/usr/bin/python3

# Given a string, find length of longest substring
# that has no repeating characters

# Time complexity: O(N)
# Space complexity: O(K)
def no_repeat_substring(st):

    # frequency of characters
    freq = {}

    # track max length of substring
    max_len = 0

    # index of beginning of window
    i = 0

    # j is index of end of window
    for j in range(len(st)):

        if st[j] not in freq:
            freq[st[j]] = 1
        else:
            freq[st[i]] += 1
            
            while freq[st[i]] > 1:
                freq[st[i]] -= 1
                i += 1

                # cleanup
                if freq[st[i]] == 0:
                    del freq[st[i]]

            max_len = max(max_len, j - i + 1)

    return max_len

# Use hash table to track last index of each character
# processed
def no_repeat_substring_2(st):

    mdict = {}
    max_len = 0
    i = 0

    for j in range(len(st)):

        if st[j] in mdict:
            i = j

        mdict[st[j]] = j

        max_len = max(max_len, j - i + 1)

    return max_len

if __name__ == "__main__":


    S = "aabccbb"

    # Expected output is 3 - "abc"
    print(no_repeat_substring(S))
    print(no_repeat_substring_2(S))


    S = "abbbb"

    # Expected output is 2 - "ab"
    print(no_repeat_substring(S))
    print(no_repeat_substring_2(S))

    S = "abccde"

    # Expected output is 3 - "abc" / "cde"
    print(no_repeat_substring(S))
    print(no_repeat_substring_2(S))
