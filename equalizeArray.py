def equalizeArray(arr):
    # print(sorted(arr))
    duplicates = []
    seen = set()
    for x in arr:
        if x in seen and x not in duplicates:
            duplicates.append(x)
        seen.add(x)

    len_arr = len(arr)
    count = 1
    # print(sorted(duplicates))
    # print(len(arr))
    for x in duplicates:
        if count<arr.count(x):
            count = arr.count(x)


    return len_arr - count

if __name__ == '__main__':
    str = "37 32 97 35 76 62"

    arr = list(map(int, str.split()))
    # 5
    result = equalizeArray(arr)
    print(result)