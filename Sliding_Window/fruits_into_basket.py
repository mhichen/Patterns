#!/usr/bin/python3

# Given array of characters where each character represents
# a fruit tree, are given two baskets.  Goal is to put
# max number of fruits in each basket, but each basket
# can only have 1 type of fruit.

# Can start with any tree, but can't skip a tree once
# started.  Will pick one fruit from each tree until cannot

# Time complexity: O(N)
# Space complexity: O(1)
def pick_fruit(arr):

    # dictionary to keep track of frequencies
    baskets = {}

    # maximum length of substring, which represents
    # total number of fruit collected
    max_len = 0

    # start of window
    i = 0

    # j tracks end of window
    for j in range(len(arr)):
        
        if arr[j] not in baskets:
            baskets[arr[j]] = 1

        else:
            baskets[arr[j]] += 1

        # if number of unique char in dictionary
        # is greater than 2, then need to increment i
        # and remove corresponding chars from dictionary
        while len(baskets) > 2:

            if baskets[arr[i]] == 1:
                del baskets[arr[i]]
            else:
                baskets[arr[i]] -= 1

            i += 1

        max_len = max(max_len, j - i + 1)

    return max_len
            
    

if __name__ == "__main__":

    fruit = ["A", "B", "C", "A", "C"]

    # Expected output: 3
    # 2 C and 1 A from ["C", "A", "C"]
    print(pick_fruit(fruit))
    

    fruit = ["A", "B", "C", "B", "B", "C"]

    # Expected output: 5
    # 3 B and 2 C from ["B", "C", "B", "B", "C"]
    print(pick_fruit(fruit))
