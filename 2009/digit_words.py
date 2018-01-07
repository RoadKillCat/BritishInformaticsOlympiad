import itertools

digits = ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']

def get_digit(word):
    for l in range(3, 6):
        possibles = [d for d in digits if len(d) == l]
        for c in itertools.combinations(word, l):
            for d in possibles:
                if ''.join(c) == d:
                    return d
    return False

r = get_digit(input())
if r:
    print(digits.index(r)+1)
else:
    print("NO")
