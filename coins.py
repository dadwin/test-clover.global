
def exchange(coins, s):
    """
        exchange(coins, s)

        Finds minimal combinations of given coins which sum equals to s
    """
    if len(coins) == 0:
        return
    if s == 0:
        return

    max_combo = [int(s / c) for c in coins]
    combo = [0] * len(max_combo)

    found = []
    while combo != max_combo:
        guess = sum(map(lambda x, y: x * y, combo, coins))
        print(combo)
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

    minimum = [found[0]]
    count = sum(found[0])

    for f in found[1:]:
        if sum(f) < count:
            minimum = [f]
            count = sum(f)
        elif sum(f) == count:
            minimum.append(f)

    return count, minimum
