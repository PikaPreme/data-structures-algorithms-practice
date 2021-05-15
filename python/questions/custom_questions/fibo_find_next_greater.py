# given a list of nums, find the next fibo


def fibo_question(seq):
    fibo = [0, 1]
    # generate the fibonacci sequence
    for x in range(0, 25):
        next_number = fibo[-1] + fibo[-2]
        print("{} = {} + {}".format(next_number, fibo[-1], fibo[-2]))
        fibo.append(next_number)
    print(fibo)

    expected_list = []
    # find the next fibonacci number that is greater than current number in sequence. then append to expected result
    for x in range(len(seq)):
        for y in range(len(fibo)):
            if fibo[y] > seq[x]:
                expected_list.append(fibo[y])
                break
    return expected_list


if __name__ == '__main__':
    seq = [1, -5, 9, 34]
    exp = [2, 0, 13, 55]
    print(fibo_question(seq) == exp)
