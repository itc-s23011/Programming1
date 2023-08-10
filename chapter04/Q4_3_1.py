def func_square(*args):
    results = []
    for n in args:
        result.append(n * n)
    return result


many_numbers = list(range(100))
s = func_square(*many_numbers)
print(s)
