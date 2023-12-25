def under_empty(playground, shape, row):
    first = len(shape[0])
    other = 4 - first

    empty_count = 0
    if other:
        for c in shape[1]:
            if playground[row][c] == ' ':
                empty_count += 1

    # Exception for shape 4
    if first == 4:
        other = first
        for c in shape[0]:
            if playground[row - 1][c] == ' ':
                empty_count += 1

    if empty_count == other:
        return True

    return False
