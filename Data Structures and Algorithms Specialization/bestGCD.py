def gcd(a, b):
    best = 0
    for d in range(1, (a+b)):
        if a%d==0 and b%d==0:
            best = d

    return best

if __name__ == '__main__':
    print(gcd(10, 4))