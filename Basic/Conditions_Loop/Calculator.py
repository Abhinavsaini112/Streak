def calculator(arr,k):
    if k == 1:
        print(arr[0] + arr[1])
    elif k == 2:
        print(arr[0] - arr[1])
    elif k == 3: 
        print(arr[0] * arr[1])
    elif k == 4:
        print(arr[0] // arr[1])
    elif k == 5:
        print(arr[0] // arr[1])
    elif k == 6:
        exit()
    else: 
        print("Invalid Operation")


arr = [int(input("Enter the integer : ")) for i in range(2)]
n = int(input("Enter the value of n : "))
calculator(arr,n)
