def bestGcd(a, b):
    if b == 0:
        return a
    a_prime = a % b
    return bestGcd(b, a_prime)

if __name__ == '__main__':
    a, b = map(float, input().split())
    print(bestGcd(a, b))