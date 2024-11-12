if __name__ == "__main__":
    low = 1
    high = 311
    numbers = [i for i in range(low+1, high+1) if i%2!=0]
    numbers.insert(0,1)
    print(numbers)
