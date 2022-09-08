

def is_legal_region(kmap_function, term):
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
# X ,y is for top left corner. X increases to the right and Y to the left in
# contrast to what they said in the assignment X2 and Y2 are bottom right and same goes for them
