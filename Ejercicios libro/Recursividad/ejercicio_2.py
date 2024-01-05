def sumatoria(n):
    if n == 1:
        return n
    return n + sumatoria(n-1)

print(sumatoria(100))