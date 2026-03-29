from math import log


def log_scale(data, base):
    return [log(x, base) for x in data]
