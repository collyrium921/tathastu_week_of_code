def lps(s):
    n = len(s)
    L = [[0 for x in range(n)] for y in range(n)]

    for i in range(n):
        L[i][i] = 1

    for j in range(2, n + 1):
        for i in range(n - j + 1):
            k = i + j - 1
            if (str[i] == str[k] and k == 2):
                L[i][k] = 2
            elif (str[i] == str[k]):
                L[i][k] = L[i + 1][k - 1] + 2
            else:
                L[i][k] = max(L[i][k - 1], L[i + 1][k])
    return L[0][n - 1]


def Deletions(s):
    n = len(s)
    res = lps(s)
    return (n - res)


s = input("Enter the string: ")
print("Minimum number of deletions are: ", Deletions(s))
