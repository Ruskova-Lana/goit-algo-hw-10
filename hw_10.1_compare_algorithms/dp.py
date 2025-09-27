def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    """
    Алгоритм динамічного програмування для знаходження мінімальної кількості монет.
    Повертає словник із номіналами та їх кількістю.
    """
    dp = [0] + [float("inf")] * amount
    coin_used = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    result = {}
    while amount > 0:
        c = coin_used[amount]
        result[c] = result.get(c, 0) + 1
        amount -= c

    return result

