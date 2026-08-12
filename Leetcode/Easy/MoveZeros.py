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

'''Can you minimize the total number of operations done?'''

def Movezeros(list):
    write = 0 
    for read in range(len(list)):
        if list[read] != 0:
            list[write], list[read] = list[read], list[write]
            write += 1
    return list

li = [0, 4, 1, 2, 0, 0, 2, 3, 1, 0]
print(Movezeros(li))