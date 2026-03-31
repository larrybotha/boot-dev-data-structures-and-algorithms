def _merge(xs: list, ys: list) -> list:
    num_xs, num_ys = len(xs), len(ys)
    i, j = 0, 0
    zs = []

    while i < num_xs and j < num_ys:
        if xs[i] < ys[j]:
            zs.append(xs[i])
            i += 1
        else:
            zs.append(ys[j])
            j += 1

    while i < num_xs:
        zs.append(xs[i])
        i += 1

    while j < num_ys:
        zs.append(ys[j])
        j += 1

    return zs


def merge_sort(xs: list) -> list:
    if len(xs) < 2:
        return xs

    mid = len(xs) // 2
    left = xs[0:mid]
    right = xs[mid:]

    return _merge(merge_sort(left), merge_sort(right))
