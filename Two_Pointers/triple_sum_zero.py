#!/usr/bin/python3

# Given an array of unsorted numbers, find all unique triplets
# in it that add up to zero

# Reduce the problem down to problem of finding a pair
# with a target sum
# Time complexity: O(N * log(N)) to sort and O(N) to find the
# target pair, which is called for every single number in
# the array, so triplet_sum has time complexity O(N * log(N) +
# N^2), which makes the overall complexity asymptotically O(N^2)
# Space complexity: O(N) for sorting
def triplet_sum(arr):

    # first sort array
    arr.sort()

    triplets = []

    for i in range(len(arr)):

        # skip same element to avoid duplicate triplets
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        new_triplet = target_pair(arr, -arr[i], i + 1)
        if len(new_triplet) > 0:
            triplets += new_triplet

    return triplets


def target_pair(arr, target, l):

    r = len(arr) - 1

    res = []
    
    while l < r:

        curr_sum = arr[l] + arr[r]

        if curr_sum > target:
            r -= 1
        elif curr_sum < target:
            l += 1
        else:
            res.append([-target, arr[l], arr[r]])
            l += 1
            r -= 1

            # Need to skip element if it's the same
            # to avoid duplicate triplets
            while l < r and arr[l] == arr[l - 1]:
                l += 1
            while l < r and arr[r] == arr[r + 1]:
                r -= 1

    return res
                                  

if __name__ == "__main__":

    input_arr = [-3, 0, 1, 2, -1, 1, -2]

    # Expected output: [-3, 1, 2], [-2, 0, 2]
    # [-2, 1, 1], and [-1, 0, 1]
    print(triplet_sum(input_arr))



    input_arr = [-5, 2, -1, -2, 3]

    # Expected output: [-5, 2, 3], [-2, -1, 3]
    print(triplet_sum(input_arr))
