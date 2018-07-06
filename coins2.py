from collections import deque


def exchange(coins, s):
    """
        exchange(coins, s)

        Finds minimal combinations of given coins which sum equals to s.
        If no combinations exist, returns None, otherwise a list of combinations.
        Combinations is a tuple with length being equal to len(coins),
        its first element is a number of coins with maximal value,
        the last element is a number of coins with minimal value, and all other in between:
        If a combination exists, it is a tuple so that
        combo[0]*sorted_coins[0] + combo[1]*sorted_coins[1] + ... = s,
        where sorted_coins is coins sorted in descending order.
    """
    coins.sort(reverse=True)
    coins_count = len(coins)

    minimum = set()
    count = s ** len(coins)

    deq = deque()
    deq.append((coins, s, tuple()))
    while len(deq):
        coins, s, combo = deq.popleft()

        if len(coins) == 0 or s == 0:
            continue

        max_coin = coins[0]
        if s % max_coin == 0:
            found = combo + (int(s / max_coin),)
            # add zeros, so found combo is the same length as coins list
            if len(found) != coins_count:
                found = found + (0,) * (coins_count - len(found))
            if count > sum(found):
                count = sum(found)
                minimum = {found}
            elif count == sum(found):
                minimum.add(found)
            continue

        coins.remove(max_coin)
        if len(coins) == 0:
            continue

        for i in range(int(s / max_coin), -1, -1):
            deq.append((list(coins), s - i * max_coin, combo + (i,)))

    return minimum if len(minimum) > 0 else None
