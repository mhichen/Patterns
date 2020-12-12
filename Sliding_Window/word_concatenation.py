#!/usr/bin/python3

# Given a string and a list of words, find all the
# starting indices of substrings in the given string
# that are a concatenation of all the given words exactly once
# without any overlapping of words.  It is given that all words
# are of the same length

# Time complexity: O(N * M * K), where N is the number of
# characters in the string, M is the total number of words
# and K is the length of the words
# Space complexity: O(M + N)
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

    # Store number of words
    nwords = len(words)
    
    # Keep track of number of word matches
    match = 0

    # Array to track resuls
    results = []

    # only need to iterate i to beginning of last
    # possible string of concatenated words
    for i in range((len(st) - nwords * k) + 1):

        # Keep track of words encountered
        words_seen = {}
        
        for j in range(nwords):

            next_word_index = i + j * k
            
            w = st[next_word_index:next_word_index + k]

            # if the word is not in our dictionary of required
            # words, don't need this word, so skip
            if w not in freq:
                break

            if w not in words_seen:
                words_seen[w] = 0
            words_seen[w] += 1

            # If word frequency is higher than that in dictionary
            # of required words, break
            if words_seen[w] > freq.get(w, 0):
                break

            if j + 1 == nwords:
                results += [i]

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
    
