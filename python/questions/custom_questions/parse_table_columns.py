# Parse through a string data file


data = '''Effect Veiler Ultimate 1st [3] - Market Price: $135.28
+-----------------------+-----------------------+---------+-----+
|         Seller        |       Condition       |  Price  | Qty |
+-----------------------+-----------------------+---------+-----+
|   98.1% (621 Sales)   | Near Mint 1st Edition | $268.99 |  1  |
|    100% (194 Sales)   | Near Mint 1st Edition | $270.00 |  1  |
|    100% (213 Sales)   | Near Mint 1st Edition | $274.88 |  1  |
| 99.8% (50,000+ Sales) | Near Mint 1st Edition | $274.88 |  1  |
| 99.8% (10,000+ Sales) | Near Mint 1st Edition | $280.00 |  1  |
| 99.8% (50,000+ Sales) | Near Mint 1st Edition | $349.99 |  1  |
|  99.7% (1,471 Sales)  | Near Mint 1st Edition | $355.01 |  1  |
+-----------------------+-----------------------+---------+-----+
'''


def get_name(split_rows):
    for x in range(0, len(split_rows[0])):
        if split_rows[0][x] == '[':
            card_name = (split_rows[0][0:x - 1])
    return card_name


def get_quantity(split_rows):
    for x in range(0, len(split_rows[0])):
        if split_rows[0][x] == '[':
            start = x
        if split_rows[0][x] == ']':
            end = x
    quantity = int(split_rows[0][start + 1:end])
    return quantity


def get_market_price(split_rows):
    market_price = (split_rows[0].split('$'))
    market_price = (float(market_price[1]))
    return market_price


def split_by_columns(split_rows):
    list_of_items = []
    for row in split_rows:
        row = row.split('|')
        for element in row:
            if element == '':
                row.remove(element)
        list_of_items.append(row)
    return list_of_items


def return_specific_column(list_of_items, column):
    this_column = []
    for row in range(len(list_of_items)):
        element = (list_of_items[row][column])
        element = float(element.strip(' ').strip('$'))
        this_column.append(element)
    # print(price_column)
    return this_column


def sort_price_column_great_to_least(price_column):
    prices_greatest_to_least = []
    for w in range(0, len(price_column)):
        greatest = price_column[0]
        for x in range(0, len(price_column)):
            if price_column[x] > greatest:
                greatest = price_column[x]
        prices_greatest_to_least.append(greatest)
        price_column.remove(greatest)
    return prices_greatest_to_least


def get_sellers_above_threshold(list_of_items, column, threshold, column_price):
    list_of_top_sellers = []
    # print(list_of_items)
    for row in range(len(list_of_items)):
        num_sales = list_of_items[row][column].split('(')
        num_sales = num_sales[1].split('S')
        num_sales = (num_sales[0].strip(' ')).replace(',', '').replace('+', '')
        num_sales = int(num_sales)
        if num_sales >= threshold:
            list_of_top_sellers.append(list_of_items[row][column_price])

    return list_of_top_sellers


def remove_first_last_lines(split_rows):
    for x in range(0, 4):
        split_rows.remove(split_rows[0])
    split_rows.remove(split_rows[-1])
    split_rows.remove(split_rows[-1])
    return split_rows


def parse_data_string(input_string):
    # # split by rows
    split_rows = input_string.split('\n')

    # Get Name
    card_name = get_name(split_rows)
    print(card_name)

    # # Find quantity
    card_quantity = get_quantity(split_rows)
    print(card_quantity)

    # Find market price
    market_price = get_market_price(split_rows)
    print(market_price)

    # remove first 4 lines, last line
    split_rows = remove_first_last_lines(split_rows)

    # # split by columns, put into 2d list
    list_of_items = split_by_columns(split_rows)

    # # return a specific column in a list
    column_sellers = 0
    column_edition = 1
    column_price = 2
    column_quantity = 3
    price_column = return_specific_column(list_of_items, column_price)
    print(price_column)

    # # sort by number values - greatest to least
    column_sales = sort_price_column_great_to_least(price_column)
    print(column_sales)

    # return prices of sellers with over 10k sales
    seller_threshold = 10000
    list_of_sellers_over_10k = get_sellers_above_threshold(list_of_items, column_sellers, seller_threshold,
                                                           column_price)
    print(list_of_sellers_over_10k)

    return 0


if __name__ == '__main__':
    print(parse_data_string(data))
