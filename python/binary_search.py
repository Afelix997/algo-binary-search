
def binary_search(num, val_arr):
    min = val_arr[0]
    max = val_arr[len(val_arr)-1]

    mid = (max+min)//2
    print(num, mid)

    if num != mid and len(val_arr) <= 1:
        return -1

    if num == mid:
        return True
    elif num > mid:
        val_arr = val_arr[len(val_arr)//2:]
        return binary_search(num,val_arr)
    elif num < mid:
        val_arr = val_arr[:len(val_arr)//2]
        return binary_search(num,val_arr)
