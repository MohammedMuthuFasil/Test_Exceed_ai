"""Merge Sort Algorithm.

Standalone implementation of merge sort.
Generated with AI assistance (GitHub Copilot).

Time complexity:  O(n log n)
Space complexity: O(n)
"""


def merge_sort(array: list) -> list:
    """
    Sort an array using the merge sort algorithm.
    Time complexity: O(n log n)
    Space complexity: O(n)
    """
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_half = merge_sort(array[:mid])
    right_half = merge_sort(array[mid:])

    return merge(left_half, right_half)


def merge(left: list, right: list) -> list:
    """Merge two sorted arrays into one sorted array."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    sample = [38, 27, 43, 3, 9, 82, 10]
    print(merge_sort(sample))  # [3, 9, 10, 27, 38, 43, 82]
