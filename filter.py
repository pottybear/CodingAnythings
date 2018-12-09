def even(x):
    return x % 2 == 0

xs = [1, 2, 3, 4]
ys = filter(even, xs)

# Lambda Way
# filter(lambda x: x % 2 == 0, xs)

print(list(ys))  # [2, 4]
