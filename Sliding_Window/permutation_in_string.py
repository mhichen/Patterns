#!/usr/bin/python3

# Given a string and a pattern, find out if string contains
# permutation of the pattern

def permutation_in_string(st, pattern):

    # Use a hash table to keep track of frequencies
    # of characters in pattern
    freq = {}
    for p in pattern:
        if p not in freq:
            freq[p] = 0
        freq[p] += 1


    # Use match to track number of characters matched
    # if match == len(freq), then return True
    match = 0

    # Use i as index to track beginning of window
    i = 0

    # Use j as index to track end of window
    for j in range(len(st)):

        if st[j] in freq:
            freq[st[j]] -= 1

            # mark 1 letter matched if frequency is 0
            if freq[st[j]] == 0:
                match += 1

        if match == len(freq):
            return True

        # shrink window if greater than length
        if (j - i + 1) >= len(pattern):

            # remember to add back to frequency map
            # if st[i] is indeed in the map
            if st[i] in freq:
                if freq[st[i]] == 0:
                    match -= 1

                freq[st[i]] += 1

            i += 1

    return False
    

if __name__ == "__main__":

    S = "oidbcaf"
    pattern = "abc"

    # Expected outcome: True
    # "bca" is a permutation of "abc"
    print(permutation_in_string(S, pattern))

    S = "odicf"
    pattern = "dc"

    # Expected outcome: False
    # "dic" is not a permutation of "dc"
    print(permutation_in_string(S, pattern))

    S = "bcdxabcdy"
    pattern = "bcdyabcdx"

    # Expected outcome: True
    print(permutation_in_string(S, pattern))
    
    S = "aaacb"
    pattern = "abc"

    # Expected outcome: True
    print(permutation_in_string(S, pattern))
