#structure is point: [straight_node, [curve1, curve2]]
#will leave on the first curve in the curves list
points =   {'A': ['D', ['E', 'F']],
            'B': ['C', ['G', 'H']],
            'C': ['B', ['I', 'J']],
            'D': ['A', ['K', 'L']],
            'E': ['A', ['M', 'N']],
            'F': ['A', ['N', 'O']],
            'G': ['B', ['O', 'P']],
            'H': ['B', ['P', 'Q']],
            'I': ['C', ['Q', 'R']],
            'J': ['C', ['R', 'S']],
            'K': ['D', ['S', 'T']],
            'L': ['D', ['T', 'M']],
            'M': ['U', ['L', 'E']],
            'N': ['U', ['E', 'F']],
            'O': ['V', ['F', 'G']],
            'P': ['V', ['G', 'H']],
            'Q': ['W', ['H', 'I']],
            'R': ['W', ['I', 'J']],
            'S': ['X', ['J', 'K']],
            'T': ['X', ['K', 'L']],
            'U': ['V', ['M', 'N']],
            'V': ['U', ['O', 'P']],
            'W': ['X', ['Q', 'R']],
            'X': ['W', ['S', 'T']]}

flip_flops = input()
last, cur = input()
steps = int(input())

for _ in range(steps):
    straight, curves = points[cur]
    #entering from a straight
    if last == straight:
        next = curves[0]
        if cur in flip_flops:
            points[cur][1] = points[cur][1][::-1]
        last = cur
        cur = next
    else: #entering from a curved
        next = straight
        if cur not in flip_flops and points[cur][1][0] != last:
            points[cur][1] = points[cur][1][::-1]
        last = cur
        cur = next
        
print(last + cur)
input()