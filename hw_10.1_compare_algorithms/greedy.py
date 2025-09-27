def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    """
    Жадібний алгоритм для знаходження решти.
    Повертає словник із кількістю монет для формування суми.
    """
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result
