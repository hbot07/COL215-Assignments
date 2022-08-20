def get_squares(kmap_function, coordinate_start, coordinate_end):
    x_div = len(kmap_function)
    y_div = len(kmap_function[0])

    squares = []
    x = coordinate_start[0]

    while x != coordinate_end[0]+1:
        x %= x_div
        y = coordinate_start[1]
        while y != coordinate_end[1]+1:
            y %= y_div
            squares.append((x, y))
            y += 1
        x += 1

    return squares


def get_values(kmap_function, squares):
    values = []
    for i in squares:
        values.append(kmap_function[i[0]][i[1]])

    return values


def check_values(values):
    if 0 in values:
        return False
    return True


def check_legal_region(kmap_function, coordinate_start, coordinate_end):
    return (coordinate_start, coordinate_end,
            check_values(get_values(kmap_function,
                                    get_squares(kmap_function,
                                                coordinate_start, coordinate_end))))


def is_legal_region(kmap_function, term):
    """
    determines whether the specified region is LEGAL for the K-map function
    Arguments:
        kmap_function: n * m list containing the kmap function
        for 2-input kmap this will 2*2
            3-input kmap this will 2*4
            4-input kmap this will 4*4
        term: a list of size k, where k is the number of inputs in function (2,3 or 4)
            (term[i] = 0 or 1 or None, corresponding to the i-th variable)
    Return:
        three-tuple: (top-left coordinate, bottom right coordinate, boolean value)
                     each coordinate is represented as a 2-tuple
"""
    pass
