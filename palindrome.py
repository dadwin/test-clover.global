
def _is_palindrome(s):
    for i in range(int(len(s)/2)):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True


def _try_expand(s, j, k):
    guess = None
    while True:
        if j < 0 or k == len(s):
            break
        if not _is_palindrome(s[j:k + 1]):
            break
        else:
            guess = s[j:k + 1]
            j -= 1
            k += 1
    return guess


def get_longest_palindrome(s):
    """
        get_longest_palindrome(s)

        Returns a set of largest palindromes for given string s.
        If no palindromes inside s, returns empty set
        If there are several different palindromes of the same length,
        returns all of them
    """
    if len(s) == 0:
        return {""}

    if len(s) == 1:
        return {s}

    palindromes = set()
    for i in range(len(s)-1):
        j, k = i, i+1
        guess = _try_expand(s, j, k)
        if guess:
            palindromes |= {guess}

        j, k = i-1, i+1
        guess = _try_expand(s, j, k)
        if guess:
            palindromes |= {guess}

    if len(palindromes) == 0:
        return {}
    maximum = max(palindromes, key=len)
    return {p for p in palindromes if len(p) == len(maximum)}
