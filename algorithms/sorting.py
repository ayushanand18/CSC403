def quick_sort_deterministic(arr: list) -> list:
    """
    Deterministic Quicksort algorithm, works in O(nlgn) average time.

    :param arr: [list] List of elements to sort.
    :return: [list] Sorted list of elements.
    """
    # wel'll pick the last element as the pivot
    if arr.__len__()<=1:
        return arr

    pivot = arr.__len__()-1
    # partition around the array
    lesser_arr, greater_arr = [], []
    # since pivot is the last element, iterate till the second last element
    for i in range(len(arr)-1):
        if arr[i]<=arr[pivot]:
            lesser_arr.append(arr[i])
        else:
            greater_arr.append(arr[i])
    # recursively perform quicksort of left and right subarrays and return sorted list
    return (quick_sort_deterministic(lesser_arr) + [arr[pivot]] +
            quick_sort_deterministic(greater_arr))
