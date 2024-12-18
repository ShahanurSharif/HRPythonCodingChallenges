def mergeSort(arr):
    length = len(arr)
    if length>1:
        middle = length//2
        left_arr = arr[:middle]
        right_arr = arr[middle:]

        #recur
        # print(f"middle={middle}; left={left_arr}; right={right_arr}")
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
            # print(f"middle={middle}; left={left_arr}; right={right_arr}")

        
        # while i < len(left_arr):
        #     arr[k] = left_arr[i]
        #     i += 1
        #     k += 1
        #     print(f"i middle={middle}; left={left_arr}; right={right_arr}")

        # while j < len(right_arr):
        #     arr[k] = right_arr[j]
        #     j += 1
        #     k += 1
        #     print(f"j middle={middle}; left={left_arr}; right={right_arr}")





if __name__ == '__main__':
    arr = [4, 1, 6, 2, 3, 8, 9]
    mergeSort(arr)
    print(arr)