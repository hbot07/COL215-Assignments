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


def get_coordinates(kmap_function, term):
    length = len(term)
    X = 0
    Y = 0
    X2 = length -1
    Y2 = length -1
    if length == 2:
        if (term[0] == 0):
            X = 0
            X2 = 0
        elif (term[0] == 1):
            X = 1
            X2 = 1
        if term[1] == 0:
            Y = 0
            Y2 = 0
        elif term[1] == 1:
            Y = 1
            Y2 = 1
    if length == 3:
        if term[0] == 0:
            X += 0
            X2 = 1
            if term[1] == 0:
                X = 0
                X2 = 0
            elif term[1] == 1:
                X = 1
        elif term[0] == 1:
            X = 2
            X2 = 3
            if term[1] == 0:
                X += 1
            elif term[1] == 1:
                X += 0
                X2 = 2
        else:
            if term[1] == 0:
                X = 3
                X2 = 0
            elif term[1] == 1:
                X = 1
                X2 = 2
        Y2 = 1
        if term[2] == 0:
            Y = 0
            Y2 = 0
        elif term[2] == 1:
            Y = 1
            Y2 = 1
    if length == 4:
        if term[0] == 0:
            X += 0
            X2 = 1
            if term[1] == 0:
                X = 0
                X2 = 0
            elif term[1] == 1:
                X = 1
        elif term[0] == 1:
            X += 2
            X2 = 3
            if term[1] == 0:
                X += 1
            elif term[1] == 1:
                X += 0
                X2 = 2
        else:
            if term[1] == 0:
                X = 3
                X2 = 0
            elif term[1] == 1:
                X = 1
                X2 = 2
        if term[2] == 0:
            Y += 0
            Y2 = 1
            if term[3] == 0:
                Y = 0
                Y2 = 0
            elif term[3] == 1:
                Y = 1
        elif term[2] == 1:
            Y += 2
            Y2 = 3
            if term[3] == 0:
                Y += 1
            elif term[3] == 1:
                Y += 0
                Y2 = 2
        else:
            if term[3] == 0:
                Y = 3
                Y2 = 0
            elif term[3] == 1:
                Y = 1
                Y2 = 2
    return((Y,X),(Y2,X2))
# X ,y is for top left corner. X increases to the right and Y to the left in
# contrast to what they said in the assignment X2 and Y2 are bottom right and same goes for them

def is_legal_region(kmap_function, term):
    t = get_coordinates(kmap_function, term)
    return check_legal_region(kmap_function, t[0], t[1])
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

print(is_legal_region([[0,1,1,0], ['x',1,'x',0], [1,0,0,0], [1,'x',0,0]],[0,0,None,1]))
print(get_coordinates([], [None, None, None]))
