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


if __name__ == "__main__":
    low = 1
    high = 311
    prime_numbers = []
    for i in range(low, high+1):
        if check_division(i):
            prime_numbers.append(i)
    print(prime_numbers)

