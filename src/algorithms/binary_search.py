def binary_search(array: list, target: int) -> int:
    """
    Search for target in a sorted array using binary search.
    Returns index if found, -1 otherwise.
    Time complexity: O(log n)
    """
    left, right = 0, len(array) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print(binary_search(data, 7))   # returns 3
    print(binary_search(data, 6))   # returns -1