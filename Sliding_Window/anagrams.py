#!/usr/bin/python3

import copy

# Given string and pattern, find all
# anagrams of the patttern
def find_anagram(st, pattern):

    # create a master copy of the pattern freq hash map
    pdict = {}

    for c in pattern:
        if c not in pdict:
            pdict[c] = 0

        pdict[c] += 1


    cdict = copy.deepcopy(pdict)

    # index i to track window beginning
    i = 0

    # Track number of matched characters
    match = 0
    
    # array to track beginning index of found anagrams
    result = []

    # index j to track window end
    for j in range(len(st)):

        if st[j] in cdict:
            cdict[st[j]] -= 1

            if cdict[st[j]] == 0:
                match += 1

        if match == len(cdict):
            result += [i]

            
        # decrease window if exceed length of pattern
        if (j - i + 2) > len(pattern):
        #if j >= len(pattern) - 1:

            if st[i] in cdict:
                if cdict[st[i]] == 0:
                    match -= 1
                cdict[st[i]] += 1

            i += 1
            
    return result


if __name__ == "__main__":

    
    S = "ppqp"
    pattern = "pq"

    print(find_anagram(S, pattern))
    print()

    S = "abbcabc"
    pattern = "abc"

    print(find_anagram(S, pattern))
