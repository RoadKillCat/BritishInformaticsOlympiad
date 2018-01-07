def p_sieve(limit):
    flags = [True] * limit
    flags[0] = flags[1] = False
    primes = []
    for (index, flag) in enumerate(flags):
        if flag:
            primes.append(index)
            for n in range(index * index, limit, index):
                flags[n] = False
    return primes


def prime(n):
    return n in primes
    if n in (0,1):
        return False
    for d in range(2, int(n ** 0.5)+1):
        if n % d == 0:
            return False
    return True

lim, start, end = 614700, 3643, 90149

primes = p_sieve(lim)
print("gened primes")

ps = [(1, start)]
shrt_pth = float('inf')
found = False
while not found:
    p = 1
    while p < lim:
        for l, n in ps[:]:
            nxt = p + n
            if prime(nxt):
                ps.append((l+1, nxt))
                if nxt == end:
                    shrt_pth = min(shrt_pth, l+1)
                    found = True
    p *= 2

    print(len(ps))

print(shrt_pth)