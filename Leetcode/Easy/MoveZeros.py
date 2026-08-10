def MoveZeros(lst):
    write = 0
    read = 0

    for i in range(len(lst)):
        if lst[read] != 0:
            lst[write] = lst[read]
            write += 1
        read += 1

    # Fill remaining positions with zeros
    while write < len(lst):
        lst[write] = 0
        write += 1

    return lst


li = [0, 4, 1, 2, 0, 0, 2, 3, 1, 0]

print(MoveZeros(li))