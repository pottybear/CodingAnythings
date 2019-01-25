def sum_digit(n):
    return sum(map(int, list(n)))

if __name__ == '__main__':
    print(sum_digit(input()))
