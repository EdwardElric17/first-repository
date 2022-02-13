def primes():
    i = 2
    while True:
        e = 2
        y = 0
        while e <= i:
            if i % e == 0:
                y += 1
            e += 1
        if y == 1:
            yield i
        i += 1

yo = primes()

print(next(yo))
print(next(yo))
print(next(yo))
print(next(yo))
print(next(yo))
print(next(yo))