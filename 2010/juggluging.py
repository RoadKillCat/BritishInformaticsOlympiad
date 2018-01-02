def minimum_jug_steps(capacities, no_jugs, target):
    def empty(i, jugs):
        jugs[i] = 0
        return jugs

    def fill(i, jugs):
        jugs[i] = capacities[i]
        return jugs

    def pour(fi, ti, jugs):
        poured = min(capacities[ti], jugs[ti] + jugs[fi]) - jugs[ti]
        jugs[ti] += poured
        jugs[fi] -= poured
        return jugs

    def jug_it_bud(jugs, steps):
        if tuple(jugs) in tried_jugs and tried_jugs[tuple(jugs)] <= steps:
            return
        tried_jugs[tuple(jugs)] = steps
        for i in range(no_jugs):
            jug_it_bud(fill(i, jugs[:]), steps+1)
            jug_it_bud(empty(i, jugs[:]), steps+1)
            for ti in range(no_jugs):
                if ti == i:
                    continue
                jug_it_bud(pour(i, ti, jugs[:]), steps+1)
    tried_jugs = {}
    jug_it_bud([0] * no_jugs, 0)
    minimum = float('inf')
    for jugs, steps in tried_jugs.items():
        if target in jugs:
            minimum = min(minimum, steps)
    return minimum

no_jugs, target = (int(i) for i in input().split())
capacities = tuple(int(i) for i in input().split())

print(minimum_jug_steps(capacities, no_jugs, target))
