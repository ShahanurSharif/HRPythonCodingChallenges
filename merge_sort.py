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
        i=0 #left idx
        j=0 #right idx
        k=0 #merged idx
        while i < len(left_arr) and j<len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i+=1
            else:
                arr[k] = right_arr[j]
                j+=1
            k+=1



if __name__ == '__main__':
    arr = [4, 1, 6, 2, 3, 8, 9]
    print('merge', mergeSort(arr))