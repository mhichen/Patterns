#!/usr/bin/python3

# Given array containings 0s and 1s, if allowed to
# replace no more than k 0s with 1s, find length
# of longest contiguous subarray having all 1s

# Time complexity: O(N)
# Space complexity: O(1)
def longest_subarray_ones_replacement(arr, k):

    nrep = 0
    max_len = 0
    i = 0

    for j in range(len(arr)):

        if arr[j] == 0:
            nrep += 1
        
        while nrep > k:

            if arr[i] == 0:
                nrep -= 1

            i += 1

        max_len = max(max_len, j - i + 1)

    return max_len

def longest_subarray_ones_replacement_2(arr, k):

    max_len = 0
    max_ones = 0
    i = 0

    for j in range(len(arr)):

        if arr[j] == 1:
            max_ones += 1

        if (j - i + 1 - max_ones) > k:

            if arr[i] == 1:
                max_ones -= 1

            i += 1

        max_len = max(max_len, j - i + 1)

    return max_len
        

if __name__ == "__main__":

    
    A = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
    k = 2

    # Expected outcome: 6
    # Replace 0s at 5 and 8
    print(longest_subarray_ones_replacement(A, k))
    print(longest_subarray_ones_replacement_2(A, k))


    A = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
    k = 3

    # Expected outcome: 9
    # Replace 0s at 6, 9, 10
    print(longest_subarray_ones_replacement(A, k))
    print(longest_subarray_ones_replacement_2(A, k))

    
