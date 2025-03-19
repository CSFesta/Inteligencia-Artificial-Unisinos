import random

def hill_climbing(init_state, fn_neighbours, fn_evaluate, possible_values, iterations=10000):
    current = init_state
    while iterations:
        neighbors = fn_neighbours(current, possible_values)
        if not neighbors:
            break
        neighbor = argmax_random_tie(neighbors, key=lambda node: fn_evaluate(node))
        if fn_evaluate(neighbor) > fn_evaluate(current):
            current = neighbor
        iterations -= 1
    return current

def argmax_random_tie(seq, key=lambda x: x):
    items = list(seq)
    random.shuffle(items)
    return max(items, key=key)

def find_neighbours_GC(state, possible_values):
    neighbours = []
    for i in range(len(state)):
        for v in possible_values:
            if state[i] != v:
                neighbour = state[:]
                neighbour[i] = v
                neighbours.append(neighbour)
    return neighbours

class EvaluateGC:
    def __init__(self, problem_instance):
        self.problem_instance = problem_instance

    def __call__(self, solution):
        value = 0
        for node, neighbors in self.problem_instance.items():
            for neighbor in neighbors:
                if node < neighbor:  # evita contar a mesma aresta duas vezes
                    if solution[node] != solution[neighbor]:
                        value += 1
        return value

# Petersen graph
petersen = {
    0: [1, 4, 5],
    1: [0, 2, 6],
    2: [1, 3, 7],
    3: [2, 4, 8],
    4: [0, 3, 9],
    5: [0, 7, 8],
    6: [1, 8, 9],
    7: [2, 5, 9],
    8: [3, 5, 6],
    9: [4, 6, 7]
}

fn_evaluate = EvaluateGC(petersen)
possible_values = ['R', 'G', 'B']
init_state = ['R' for _ in range(10)]

best = hill_climbing(init_state, find_neighbours_GC, fn_evaluate, possible_values)

print('Resulting solution: %s' % best)
print('Value of resulting solution: %d' % fn_evaluate(best))
