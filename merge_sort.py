def mergeSort(arr):
    length = len(arr)
    if length>1:
        middle = length//2
        left_arr = arr[:middle]
        right_arr = arr[middle:]

        #recur
        mergeSort(left_arr)
        mergeSort(right_arr)

        #merge
        i=0
        j=0
        r=0
        while i < len(left_arr) and j<len(right_arr):
            print(i, left_arr)



if __name__ == '__main__':
    arr = [4, 1, 6, 2, 3, 8, 9]
    print('merge', mergeSort(arr))