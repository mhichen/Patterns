#!/usr/bin/python3

# Given a string with lowercase letters only, if
# allowed to replace no more than k letters with
# any letter, find length of longest substring
# having same letters after replacement

# Time complexity: O(N^2)?
# Space complexity: O(1)
def longest_substring_same_letter_replacement(st, k):

    # number of replacements
    nrep = 0

    # maximum substring length
    max_len = 0

    # use i as index of window beginning
    i = 0

    # use j as index of window end
    j = 0
    
    while j < len(st):

        # if char at j is different from char at i
        # then need to increment nrep
        if st[j] != st[i]:
            nrep += 1
        

        if nrep > k:

            # increment i until first instance
            # where a new character is reached
            while st[i + 1] == st[i]:
                i += 1

            i += 1
            j = i + 1
            nrep = 0

        max_len = max(max_len, j - i + 1)
        j += 1

                
    return max_len

# Better version
def longest_substring_same_letter_replacement_2(st, k):

    i = 0
    max_len = 0
    max_repeat = 0
    freq = {}
    
    for j in range(len(st)):

        if st[j] not in freq:
            freq[st[j]] = 0
        freq[st[j]] += 1

        max_repeat = max(max_repeat, freq[st[j]])

        if (j - i + 1 - max_repeat) > k:
            freq[st[i]] -= 1
            i += 1

        max_len = max(max_len, j - i + 1)

    return max_len
    
    

if __name__ == "__main__":

    S = "aabccbb"
    k = 2

    # Expected output: 5
    # Replace two "c" with "b" to get
    # longest repeating substring "bbbbb"
    print(longest_substring_same_letter_replacement(S, k))
    print(longest_substring_same_letter_replacement_2(S, k))


    S = "abbcb"
    k = 1

    # Expected output: 4
    # Replace "c" with "b" to get
    # substring "bbbb"
    print(longest_substring_same_letter_replacement(S, k))
    print(longest_substring_same_letter_replacement_2(S, k))

    S = "abccde"
    k = 1

    # Expected output: 3
    # Replace "b" or "d" with "c"
    # to get substring "ccc"
    print(longest_substring_same_letter_replacement(S, k))
    print(longest_substring_same_letter_replacement_2(S, k))
