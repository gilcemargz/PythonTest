import math


def polysum(n, s):
    """
    n: number of sides
    s: length

    return: area of the polygon plus the square of perimeter
    """
    area = (0.25 * n * s**2) / (math.tan(math.pi / n))
    perimeter = (n * s)**2

    return round(area + perimeter, 4)
