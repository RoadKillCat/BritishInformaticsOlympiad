def triangle(r):
    if len(r) == 1:
        return r
    return triangle(''.join(r[i] if r[i] == r[i+1] else next(s for s in 'RGB' if s not in (r[i], r[i+1])) for i in range(0, len(r)-1)))


s = input()
if 0 < len(s) < 11 and all(c in 'RGB' for c in s):
    print(triangle(s))
else:
    print("invalid entry")
