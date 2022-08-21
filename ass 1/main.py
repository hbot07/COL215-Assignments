def get_squares(kmap_function, coordinate_start, coordinate_end):
    x_div = len(kmap_function)
    y_div = len(kmap_function[0])

    squares = []
    x = coordinate_start[0]

    while x != coordinate_end[0] + 1:
        x %= x_div
        y = coordinate_start[1]
        while y != coordinate_end[1] + 1:
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
    length = len(term)
    y_start = 0
    x_start = 0
    y_end = length - 1
    x_end = length - 1
    if length == 2:
        if term[0] == 0:
            y_start = 0
            y_end = 0
        elif term[0] == 1:
            y_start = 1
            y_end = 1
        if term[1] == 0:
            x_start = 0
            x_end = 0
        elif term[1] == 1:
            x_start = 1
            x_end = 1
    if length == 3:
        if term[0] == 0:
            y_start += 0
            y_end = 1
            if term[1] == 0:
                y_start = 0
                y_end = 0
            elif term[1] == 1:
                y_start = 1
        elif term[0] == 1:
            y_start += 2
            y_end = 3
            if term[1] == 0:
                y_start += 1
            elif term[1] == 1:
                y_start += 0
                y_end = 2
        else:
            if term[1] == 0:
                y_start = 3
                y_end = 0
            elif term[1] == 1:
                y_start = 1
                y_end = 2
        if term[2] == 0:
            x_start = 0
            x_end = 0
        elif term[2] == 1:
            x_start = 1
            x_end = 1
    if length == 4:
        if term[0] == 0:
            y_start += 0
            y_end = 1
            if term[1] == 0:
                y_start = 0
                y_end = 0
            elif term[1] == 1:
                y_start = 1
        elif term[0] == 1:
            y_start += 2
            y_end = 3
            if term[1] == 0:
                y_start += 1
            elif term[1] == 1:
                y_start += 0
                y_end = 2
        else:
            if term[1] == 0:
                y_start = 3
                y_end = 0
            elif term[1] == 1:
                y_start = 1
                y_end = 2
        if term[2] == 0:
            x_start += 0
            x_end = 1
            if term[3] == 0:
                x_start = 0
                x_end = 0
            elif term[3] == 1:
                x_start = 1
        elif term[2] == 1:
            x_start += 2
            x_end = 3
            if term[3] == 0:
                x_start += 1
            elif term[3] == 1:
                x_start += 0
                x_end = 2
        else:
            if term[3] == 0:
                x_start = 3
                x_end = 0
            elif term[3] == 1:
                x_start = 1
                x_end = 2

    return check_legal_region(kmap_function, (x_start, y_start), (x_end, y_end))


print(is_legal_region([[0, 1, 1, 0], ['x', 1, 'x', 0], [1, 0, 0, 0], [1, 'x', 0, 0]],
                      [0, None, None, 1]))
