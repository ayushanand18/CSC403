def binary_search(array: list, target: int, low: int = 0, high: int = None) -> int:
    """
    Performs Binary Search in the array

    :param array: [List] The sorted input array of values
    :param target: [int] The value to search in the array
    :param low: [int] The lower index value of the subarray to search in
    :param high: [int] The upper index value of the subarray to search in

    :return: [int] Returns index of found element or -1 (if not found)
    """
    high = array.__len__()-1 if not high else high
    mid = low + (high-low)//2
    if high<low:
        return -1

    if array[mid]==target:
        return mid
    elif array[mid]<target:
        return binary_search(array, target, mid+1, high)
    else:
        return binary_search(array, target, low, mid-1)
