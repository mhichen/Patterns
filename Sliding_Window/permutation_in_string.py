#!/usr/bin/python3

# Given a string and a pattern, find out if string contains
# permutation of the pattern

def permutation_in_string(st, pattern):

    # Use a dictionary to keep track of frequency
    # of characters in the pattern
    freq = {}
    for c in pattern:
        if c not in freq:
            freq[c] = 0
        freq[c] += 1

    # Index i to track window start
    i = 0

    # Track number of matched characters
    match = 0

    # Index j to track window end
    for j in range(len(st)):

        if st[j] in freq:
            freq[st[j]] -= 1

            if freq[st[j]] == 0:
                match += 1

        if match == len(freq):
            return True
        
        if (j - i + 1) > len(pattern):
            i += 1

            if st[i] in freq:
                if freq[st[i]] == 0:
                    match -= 1
                freq[st[i]] += 1

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
