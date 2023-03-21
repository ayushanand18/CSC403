"""
##############################
#  Ayush Anand               #
#  ___________               #
#  21CS8109                  #
##############################
"""
from random import random, randint
from time import time

def quick_sort_deterministic(arr: list) -> list:
    """
    Deterministic Quicksort algorithm, works in O(nlgn) average time.

    :param arr: [list] List of elements to sort.
    :return: [list] Sorted list of elements.
    """
    # the base case, if the subarray contains only 1 element
    # return the same element
    if arr.__len__()<=1:
        return arr
    # pick the last element as the pivot
    pivot = arr.__len__()-1
    # initialise the left subarray, and the right subarray
    lesser_arr, greater_arr = [], []
    # since pivot is the last element, iterate till the second last element
    for i in range(len(arr)-1):
        # partition around the pivot element,
        # all elements lesser equals to pivot into left subarray
        if arr[i]<=arr[pivot]:
            lesser_arr.append(arr[i])
        # all elements greater than pivot into the right subarray
        else:
            greater_arr.append(arr[i])
    # recursively perform quicksort of left and right subarrays and return sorted list
    return (quick_sort_deterministic(lesser_arr) + [arr[pivot]] +
            quick_sort_deterministic(greater_arr))

def quick_sort_randomised(arr: list) -> list:
    """
    Randomised Quicksort algorithm, works in O(nlgn) average time.

    :param arr: [list] List of elements to sort.
    :return: [list] Sorted list of elements.
    """
    # the base case, if the subarray contains only 1 element
    # return the same element
    if arr.__len__()<=1:
        return arr
    # pick a random index in the array
    pivot = int(random()*(arr.__len__()-1))
    # initialise the left subarray, and the right subarray
    lesser_arr, greater_arr = [], []
    # Partitioning the array with respect to the pivot element
    # since pivot is any element, iterate for all except when equal to pivot
    for i in range(len(arr)):
        # skip the pivot element from partition
        if i==pivot:
            continue
        # add the elements lesser equals to the pivot into the left subarray
        if arr[i]<=arr[pivot]:
            lesser_arr.append(arr[i])
        # add the elements greater equals to the pivot into the right subarray
        else:
            greater_arr.append(arr[i])
    # recursively perform quicksort of left and right subarrays and return sorted list
    return (quick_sort_randomised(lesser_arr) + [arr[pivot]] +
            quick_sort_randomised(greater_arr))

print('> Running tests...')
# benchmarking performance on a set of 1000,000 elements
input_list = [randint(1,10000) for i in range(1000000)]
print(f'.. Generated input of length {input_list.__len__()}')
a = time()
quick_sort_randomised(input_list)
b = time()
print(f'.. Ran randomised in {b-a} second')
a = time()
quick_sort_deterministic(input_list)
b = time()
print(f'.. Ran deterministic in {b-a} second')
"""
> Results
> -------
>   Deterministic: 7.305710554122925 sec
>   Randomised: 6.567975044250488 sec
> .......

"""
