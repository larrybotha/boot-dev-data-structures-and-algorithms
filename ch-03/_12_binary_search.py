from math import floor


def binary_search(target, xs) -> bool:
    result = False

    if len(xs) == 0:
        return result

    low = 0
    high = len(xs)

    while low < high and not result:
        mid = low + floor((high - low) / 2)
        value = xs[mid]
        result = value == target

        if target < value:
            high = mid
        else:
            low = mid + 1

    return result
