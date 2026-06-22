def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        return float('inf')
    return sum(1 for a, b in zip(s1, s2) if a != b)

def indel_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1)
    return dp[m][n]

def levenshtein_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)
    return dp[m][n]


def get_keyboard_weight(c1, c2):
    adjacent = {
        'q': {'w', 'a'}, 'w': {'q', 'e', 'a', 's'}, 'e': {'w', 'r', 's', 'd'},
        'r': {'e', 't', 'd', 'f'}, 't': {'r', 'y', 'f', 'g'}, 'y': {'t', 'u', 'g', 'h'},
        'u': {'y', 'i', 'h', 'j'}, 'i': {'u', 'o', 'j', 'k'}, 'o': {'i', 'p', 'k', 'l'},
        'p': {'o', 'l'}, 'a': {'q', 'w', 's', 'z'}, 's': {'q', 'w', 'e', 'a', 'd', 'z', 'x'},
        'd': {'w', 'e', 'r', 's', 'f', 'x', 'c'}, 'f': {'e', 'r', 't', 'd', 'g', 'c', 'v'},
        'g': {'r', 't', 'y', 'f', 'h', 'v', 'b'}, 'h': {'t', 'y', 'u', 'g', 'j', 'b', 'n'},
        'j': {'y', 'u', 'i', 'h', 'k', 'n', 'm'}, 'k': {'u', 'i', 'o', 'j', 'l', 'm'},
        'l': {'i', 'o', 'p', 'k'}, 'z': {'a', 's', 'x'}, 'x': {'s', 'd', 'z', 'c'},
        'c': {'d', 'f', 'x', 'v'}, 'v': {'f', 'g', 'c', 'b'}, 'b': {'g', 'h', 'v', 'n'},
        'n': {'h', 'j', 'b', 'm'}, 'm': {'j', 'k', 'n'}
    }

    if c1 in adjacent and c2 in adjacent[c1]:
        return 0.5
    return 1

def custom_hamming_distance(s1, s2):
    if len(s1) != len(s2):
        return float('inf')
    dist = 0
    for a, b in zip(s1, s2):
        if a != b:
            dist += get_keyboard_weight(a, b)
    return dist

def custom_levenshtein_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0.0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                cost = get_keyboard_weight(s1[i - 1], s2[j - 1])
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)
    return dp[m][n]