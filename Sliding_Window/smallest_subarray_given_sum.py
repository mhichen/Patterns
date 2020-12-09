#!/usr/bin/python3
import math

# Given array of positive numbers and a positive number S
# find the *length* of the smallest contiguous subarray whose
# sum is greater than or equal to S
# Return 0 if no such subarray exists
def smallest_subarray_with_given_sum(arr, S):

    _sum = 0
    min_length = math.inf
    wstart = 0

    for wend in range(0, len(arr)):
        _sum += arr[wend]

        while _sum >= S:
            min_length = min((wend - wstart + 1), min_length)
            _sum -= arr[wstart]
            wstart += 1
            #_sum = 0
            #wend = wstart

    if min_length == math.inf:
        return 0
    
    return min_length

if __name__ == "__main__":

    A = [2, 1, 5, 2, 3, 2]
    S = 7

    # Expected output: 2
    # Smallest subarray with sum greater than
    # or equal to S is [5, 2]
    print(A)
    print(smallest_subarray_with_given_sum(A, S))
    
    A = [2, 1, 5, 2, 8]
    S = 7

    # Expected output: 1
    # Smallest subarray with sum greater than
    # or equal to S is [8]
    print(A)
    print(smallest_subarray_with_given_sum(A, S))

    A = [3, 4, 1, 1, 6]
    S = 8

    # Expected output: 3
    # Smallest subarray with sum greater than
    # or equal to S is [3, 4, 1] or [1, 1, 6]
    print(A)
    print(smallest_subarray_with_given_sum(A, S))
