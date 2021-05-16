def find_fibo(n):
    fibo = [0, 1]
    if n == 0:
        return 0
    if n == 1:
        return 1
    for x in range(30):
        fibo.append(fibo[-1] + fibo[-2])

    val = fibo[n-1] + fibo[n-2]
    return 'F({}) = F({}) + F({}) = {} + {} = {}'.format(n, n-1, n-2, fibo[n-1], fibo[n-2], val)


if __name__ == '__main__':
    # print(find_fibo(0))
    # print(find_fibo(1))
    # print(find_fibo(2) == 1)
    # print(find_fibo(3) == 2)
    # print(find_fibo(4) == 3)
    for x in range(0,30):
        print(find_fibo(x))
