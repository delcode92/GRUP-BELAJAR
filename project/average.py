def rata_rata(deret):
    y = 0
    for x in data:
        y = y + x
    return y / len(deret)

    # return sum(deret) / len(deret)
data = [10, 12, 18, 19, 21, 24]


print(f" Data -> {data}")
print(f" Rata-ratanya adalah {rata_rata(data)}")
