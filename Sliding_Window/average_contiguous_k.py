#!/usr/bin/python3

import numpy as np

# Given an array, find average of all contiguous subarrays of size 'K'
# Brute force method
def contiguous_avg_k_brute(arr, k):

    result = []

    # iterate up to last element where we have a
    # full k elements left in the list
    for i in range(len(arr) - k + 1):
        result += [np.mean(arr[i:i+5])]

    return result

# Use sliding window method
def contiguous_avg_k(arr, k):

    result = []

    _sum = sum(arr[0:k])
    result += [_sum / k]
    
    for i in range(1, len(arr) - k + 1):
        _sum -= arr[i - 1]
        _sum += arr[i + k - 1]
        result += [_sum / k]

    return result
        
# A better (?) sliding window method
def contiguous_avg_k_textbook(arr, k):

    result = []

    # initialize window sum and window start
    _sum, wstart = 0, 0

    for wend in range(len(arr)):
        _sum += arr[wend]

        if wend >= (k - 1):
            result += [_sum / k]
            _sum -= arr[wstart]
            wstart += 1

    return result

if __name__ == "__main__":

    A = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    k = 5
    
    print(contiguous_avg_k_brute(A, k))

    print(contiguous_avg_k(A, k))
    
    print(contiguous_avg_k_textbook(A, k))
