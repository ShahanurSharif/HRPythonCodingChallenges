def test_sum(first_digit, second_digit):
    return first_digit + second_digit

if __name__ == '__main__':
    a, b = map(float, input().split())
    print(test_sum(a, b))