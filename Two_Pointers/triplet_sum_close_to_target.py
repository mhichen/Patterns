#!/usr/bin/python3

import numpy as np

# Given array of unsorted numbers and a target number,
# find triplet in the array whose sum is as close to
# the target number as possible and return the sum of
# the triplet.  If more than one such triplet, return
# smallest sum

# Employ similar trick to triplet sum to zero, except
# here we keep track of the closest and smallest sum

# Time complexity: O(N^2)
# Space complexity: O(1)
def triplet_sum_close_to_target(arr, target):

    # First, sort the array
    arr.sort()
    
    # Keep track of which is smallest sum
    min_sum = np.inf

    # Keep track of which is the smallest difference
    # from target
    min_diff = np.inf

    # No need to iterate to the very last number
    for i in range(len(arr) - 2):

        curr_sum = target_pair(arr, target, i)
        curr_diff = abs(curr_sum - target)

        if curr_diff <= min_diff:

            if curr_diff == min_diff and curr_sum > min_sum:
                continue

            min_diff = curr_diff
            min_sum = curr_sum

    return min_sum


def target_pair(arr, target, i):

    l = i + 1
    r = len(arr) - 1

    min_sum = np.inf
    min_diff = np.inf

    while l < r:

        curr_sum = arr[i] + arr[l] + arr[r]

        curr_diff = abs(curr_sum - target)

        if curr_diff <= min_diff:

            if curr_diff == min_diff and curr_sum > min_sum:
                continue
            
            min_diff = curr_diff
            min_sum = curr_sum

        if curr_sum > target:
            r -= 1
        elif curr_sum < target:
            l += 1
        else:
            return min_sum

    return min_sum
        
        

if __name__ == "__main__":

    input_arr = [-2, 0, 1, 2]
    target = 2

    # Expected output: 1
    # Triplet [-2, 1, 2] has closest sum
    # to target
    print(triplet_sum_close_to_target(input_arr, target))



    input_arr = [-3, -1, 1, 2]
    target = 1

    # Expected output: 0
    # Triplet [2, 1, -3] has closest sum to target
    print(triplet_sum_close_to_target(input_arr, target))


    input_arr = [1, 0, 1, 1]
    target = 100

    # Expected output: 3
    # Triplet [1, 1, 1] has closet sum to target
    print(triplet_sum_close_to_target(input_arr, target))
    

    
