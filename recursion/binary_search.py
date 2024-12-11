def binary_search(arr: list, left: int, right: int, target: int) -> int:
    if right >= left:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            return binary_search(arr, left, mid - 1, target)

        else:
            return binary_search(arr, mid + 1, right, target)

    else:
        return -1


arr1 = [1, 3, 5, 7, 9, 11, 13]
tar = 10

result = binary_search(arr1, 0, len(arr1) - 1, tar)

print(f"Element found at index: {result}" if result != 1 else "Element not found")
