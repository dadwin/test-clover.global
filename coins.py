
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
    if len(coins) == 0:
        return
    if s == 0:
        return

    coins.sort(reverse=True)

    max_combo = [int(s / c) for c in coins]
    combo = [0] * len(max_combo)

    found = []
    while combo != max_combo:
        guess = sum(map(lambda x, y: x * y, combo, coins))
        if guess == s:
            found.append(tuple(combo))

        for i in range(0, len(max_combo)):
            if combo[i] == max_combo[i]:
                combo[i] = 0
            else:
                combo[i] += 1
                break

    if sum(map(lambda x, y: x * y, max_combo, coins)) == s:
        found.append(tuple(max_combo))

    if len(found) == 0:
        return

    minimum = {found[0]}
    count = sum(found[0])

    for f in found[1:]:
        if sum(f) < count:
            minimum = {f}
            count = sum(f)
        elif sum(f) == count:
            minimum.add(f)

    return minimum
