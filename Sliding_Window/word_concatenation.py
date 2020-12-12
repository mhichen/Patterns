#!/usr/bin/python3

# Given a string and a list of words, find all the
# starting indices of substrings in the given string
# that are a concatenation of all the given words exactly once
# without any overlapping of words.  It is given that all words
# are of the same length

# Time complexity: O(N / K), where N is the number of
# characters in the string and K is the length of the words
# Space complexity: O(M + N), where M is the total number of words
def word_concatenation(st, words):

    # Store words into hash table
    freq = {}
    for w in words:
        if w not in freq:
            freq[w] = 0
        freq[w] += 1


    # Variable to store length of words, which
    # are all the same length
    k = len(words[0])
    
    # Keep track of number of word matches
    match = 0

    # Index to track beginning of window
    i = 0

    # Array to track resuls
    results = []

    for j in range(0, len(st), k):

        w = st[j:j+k]

        if w in freq:
            freq[w] -= 1
            
            if freq[w] == 0:
                match += 1
        print(freq)

        if match == len(freq):
            results += [i]

            freq[st[i:i+k]] += 1
            match -=1

            i += k

    return results
    




if __name__ == "__main__":

    
    S = "catfoxcat"
    words = ["cat", "fox"]

    # Expected output: [0, 3]
    print(word_concatenation(S, words))


    S = "catcatfoxfox"
    words = ["cat", "fox"]

    # Expected output: [3]
    print(word_concatenation(S, words))
    
