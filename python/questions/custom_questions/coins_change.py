# 33 cents = 1 quarter,  8 pennies

# i = pointer to current coin
# coins_used = coins used for this specific coin value
# count = total number of coins_used

# while we still have coins available,
#   floor division of coins // current coin, this will get highest number of coins we can use, without going over.
#   then we will have to subtract the value that we calculated from the total, and we are left with the remainder number of change
#   increment coin pointer, to go to next coin value
#   add the number of coins used to the total, reset coins used to prepare for next coin value calculations
#   this process repeats for all coin values (usually 25 -> 10 -> 5 -> 1)
#   time complexity is length of coins_available (usually O(4)) which is constant. O(1)

# example: 48 cents
# quarter: 1 quarter -> 48-25 = 23
# dime: 2 -> 23-20 = 3
# nickel: 0 -> 3-0 = 3
# penny: 3 -> 3-3 = 0
# return: 1+2+0+3 = 6


def exchange_coins(coins_available, coins):
    coin_values = coins_available
    i = 0
    coins_used = 0
    count = 0
    while coins > 0:
        coins_used += coins // coin_values[i]  # 3 // 1 = 3
        coins -= (coin_values[i] * coins_used)  # coins = 3 - (1 * 3) -> 0
        i += 1
        count += coins_used
        coins_used = 0
    return count


# brute force solution for problem with missing coin
# calculate all minimums for all combinations of missing coins
# return the one that gives the least

# example: 31 cents but missing nickels
# normal way: 1 quarter + 6 pennys = 7
# best way: 3 dimes + 1 penny = 4

# we can append results to a list and keep the minimum one
# in order to test all possible combinations of available coins, we use a list and remove and add them back in order.
# example of lists:
#  [0] [1] [2]
# [25, 10,  1] nickel gone
# [10, 1] quarter & nickel gone (remove 0, insert 0)
# [25, 1] dime & nickel gone (remove 1, insert 1)
# don't need to test the one with penny removed, because penny are essential for basically all change.
# IMPORTANT: need to remove coin, but insert them back in the correct spot. cannot just append them.

# 106 = 3 quarter, 3 dime, 1 penny = 7
# 106 = 4 quarter 6 penny = 10


def min_coins(missing_coin, target):
    list = [25, 10, 5, 1]
    list.remove(missing_coin)
    list2 = []
    # list2.append(exchange_coins(list, target))

    for x in range(0, 2):
        out = list[x]
        list.remove(out)
        print(list)
        list2.append(exchange_coins(list, target))
        list.insert(x, out)
    return min(list2)


if __name__ == '__main__':
    # print(exchange_coins(33) == 5)
    # print(exchange_coins(50) == 2)
    # print(exchange_coins(0) == 0)
    # print(exchange_coins(1) == 1)
    # print(exchange_coins(2) == 2)
    # print(exchange_coins(-1) == 0)
    # print(exchange_coins([25, 10, 5, 1], 31))
    print(min_coins(5, 106))


