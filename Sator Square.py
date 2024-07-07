def is_sator_square(tablet):
    length = len(tablet)
    for i in range(length):
        for j in range(length):
            if tablet[i][j] != tablet[length-1-i][length-1-j] or tablet[j][i] != tablet[length-1-j][length-1-i]:
                return False
            if tablet[i][j] != tablet[j][i]:
                return False
    return True
