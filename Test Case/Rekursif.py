def kurangSampaiNol(n):
    if n == -1:
        return []
    else:
        return [n] + kurangSampaiNol(n - 1)


print(kurangSampaiNol(10))
