from goit_hw_10.greedy import find_coins_greedy
from goit_hw_10.dp import find_min_coins

if __name__ == "__main__":
    amount = 113

    greedy_result = find_coins_greedy(amount)
    dp_result = find_min_coins(amount)

    print(f"Greedy ({amount}):", greedy_result)
    print(f"DP ({amount}):", dp_result)
