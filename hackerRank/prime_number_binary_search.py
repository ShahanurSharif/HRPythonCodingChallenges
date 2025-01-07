def check_division(i):
    is_prime = True
    if i>3:
        n = i+1
        for j in range(2, n):
            divisor = j -1
            if  divisor != 1:
                if i%divisor == 0:
                    is_prime = False

    return is_prime


def check_guess(arr, target):
    low = 0
    high = len(arr)-1
    number_of_guess = 0
    while low <= high:
        number_of_guess += 1
        mid = (low + high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return number_of_guess

if __name__ == "__main__":
    low = 1
    high = 311
    prime_numbers = []
    for i in range(low, high+1):
        if check_division(i):
            prime_numbers.append(i)

    number_of_guess = check_guess(prime_numbers, 52)
    print(number_of_guess+1)

