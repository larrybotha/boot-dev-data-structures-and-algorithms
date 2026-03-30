def bubble_sort(xs):
    end = len(xs)
    swapping = True

    while swapping:
        swapping = False

        for i in range(1, end):
            if xs[i - 1] > xs[i]:
                swapping = True
                xs[i - 1], xs[i] = xs[i], xs[i - 1]

        # mitigate unnecessary iterations - each loop guarantees one
        # fewer value to swap in list
        end -= 1

    return xs
