#!/usr/bin/python3

import numpy as np

# Given array of positive numbers and a positive number k
# find the maximum sum of any contiguous subarray of size k

# Use sliding window technique - keep track of
# the maximum sum encountered
def max_subarray_size_k(arr, k):

    _sum = 0
    wstart = 0
    max_sum = -np.inf

    for wend in range(len(arr)):

        _sum += arr[wend]

        if wend >= (k - 1):
            max_sum = max(max_sum, _sum)
            _sum -= arr[wstart]
            wstart += 1

    return max_sum
            

if __name__ == "__main__":


    A = [2, 1, 5, 1, 3, 2]
    k = 3

    # Expected output: 9
    # corresponding to subarray [5, 1, 3]

    print(max_subarray_size_k(A, k))

    A = [2, 3, 4, 1, 5]
    k = 2

    print(max_subarray_size_k(A, k))
