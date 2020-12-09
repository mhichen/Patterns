#!/usr/bin/python3

# Given a string, find the length of the longest
# substring with at most two distinct characters
def longest_substring_two_distinct(st):

    mdict = {}
    max_len = 0
    i = 0

    for j in range(len(st)):

        if st[j] not in mdict:
            mdict[st[j]] = 1
        else:
            mdict[st[j]] += 1

        while len(mdict) > 2:
            if mdict[st[i]] == 1:
                del mdict[st[i]]
            else:
                mdict[st[i]] -= 1

            i += 1

        max_len = max(max_len, j - i + 1)

    return max_len
    

if __name__ == "__main__":

    S = "bbcaacacb"

    # Expected output: 6 - "caacac"
    print(longest_substring_two_distinct(S))
