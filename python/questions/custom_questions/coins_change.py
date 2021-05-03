# 33 cents = 1 quarter,  8 pennies


def exchange_coins(coins_available, coins):
    coin_values = coins_available
    i = 0
    coins_used = 0
    count = 0
    while coins > 0:
        coins_used += coins // coin_values[i]
        # 3 // 1 = 3
        coins -= (coin_values[i] * coins_used)
        # coins = 3 - (1 * 3) -> 0
        i += 1
        count += coins_used
        coins_used = 0
    return count


def min_coins(missing_coin, target):
    list = [25, 10, 5, 1]
    list.remove(missing_coin)
    print(list)
    list2 = []

    for x in range(0, 2):
        list2.append(exchange_coins(list, target))

    return min(list2)


if __name__ == '__main__':
    # print(Test.exchange_coins(33) == 5)
    # print(Test.exchange_coins(50) == 2)
    # print(Test.exchange_coins(0) == 0)
    # print(Test.exchange_coins(1) == 1)
    # print(Test.exchange_coins(2) == 2)
    # print(Test.exchange_coins(-1) == 0)
    print(exchange_coins([25, 10, 1], 31))
    print(min_coins(5, 31))
