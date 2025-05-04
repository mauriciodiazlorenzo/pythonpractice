def coinChange(coins: list[int], amount: int) -> int:
    coins.sort()
    # making amount 0 requires 0 coins
    coins_needed = [0]
    for curamount in range(1, amount + 1):
        mincoins = 1E6
        for c in coins:
            if c==curamount:
                mincoins=1
                break
            # if there's no exact coin match
            elif c<curamount:
                # the best we can do
                mincoins = min(mincoins, 1+coins_needed[curamount-c])
            else:
                break
        coins_needed.append(mincoins)
    if coins_needed[amount]>1E5:
        return -1
    else:
        return coins_needed[amount]

    # naive and too slow
    # for curamount in range(1, amount + 1):
    #     mincoins = 1E6
    #     for c in coins:
    #         if c>curamount:
    #             break
    #         n = 1
    #         while n * c <= curamount and mincoins > n:
    #             remainder = curamount - n * c
    #             mincoins = min(mincoins, n + coins_needed[remainder])
    #             n +=1
    #     coins_needed.append(mincoins)
    # if coins_needed[amount]==1E6:
    #     return -1
    # else:
    #     return coins_needed[amount]

coinChange([1,2,5],11)