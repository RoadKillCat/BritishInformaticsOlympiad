n = int(input("input: "))
d = sorted(list(str(n)))

p = False
for m in range(2, 10):
    if sorted(list(str(m*n))) == d:
        p = True
        print(m, end=" ")

if not p:
    print("NO")
else:
    print()
