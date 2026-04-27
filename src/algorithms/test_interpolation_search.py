"""Additional searching tests - manually written for edge case coverage."""


def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high and arr[low] <= target <= arr[high]:
        if arr[high] == arr[low]:
            if arr[low] == target:
                return low
            break
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1


def test_interpolation_found():
    assert interpolation_search([10, 20, 30, 40, 50], 30) == 2

def test_interpolation_first():
    assert interpolation_search([10, 20, 30], 10) == 0

def test_interpolation_last():
    assert interpolation_search([10, 20, 30], 30) == 2

def test_interpolation_not_found():
    assert interpolation_search([10, 20, 30], 25) == -1

def test_interpolation_empty():
    assert interpolation_search([], 5) == -1

def test_interpolation_single_found():
    assert interpolation_search([7], 7) == 0

def test_interpolation_single_not_found():
    assert interpolation_search([7], 3) == -1

def test_interpolation_all_same():
    assert interpolation_search([5, 5, 5], 5) == 0

def test_interpolation_all_same_not_found():
    assert interpolation_search([5, 5, 5], 3) == -1

def test_interpolation_large_list():
    arr = list(range(0, 1000, 2))
    assert interpolation_search(arr, 500) == 250
