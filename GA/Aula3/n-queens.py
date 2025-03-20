import random

def hill_climbing(init_state, fn_neighbours, fn_evaluate, possible_values, iterations=10000):

    current = init_state

    while iterations:

        # explore the neighbourhood
        neighbors = fn_neighbours(current, possible_values)
        if not neighbors:
            break

        # select the best neighbour
        neighbor = argmax_random_tie(neighbors, key=lambda node: fn_evaluate(node))

        # store the neighbour only if it is better than the current solution
        if fn_evaluate(neighbor) > fn_evaluate(current):
           current = neighbor
        iterations -= 1

    return current

# return the best element from the received list; ties are break uniformly at random
def argmax_random_tie(seq, key=lambda x: x):
    items = list(seq)
    random.shuffle(items)
    return max(items, key=key)

def find_neighbours_NQueens(state, possible_values):
    neighbours = []
    n = len(state)

    for col in range(n):
        current_row = state[col]
        for row in possible_values:
            if row != current_row:
                new_state = state.copy()
                new_state[col] = row
                neighbours.append(new_state)

    return neighbours


# evaluation class for the n-Queens problem
class EvaluateNQueens:
    def __init__(self, n):
        self.n = n

    def __call__(self, solution):
        conflicts = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if solution[i] == solution[j]:
                    conflicts += 1
                if abs(solution[i] - solution[j]) == abs(i - j):
                    conflicts += 1

        return -conflicts

# instance of the N-Queens problem
n = 8

# create an instance of the evaluation class for the considered problem instance
fn_evaluate = EvaluateNQueens(n)

# set of possible values
possible_values = [x for x in range(n)]

# initial state (we begin with a solution where all queens are on the same row)
init_state = [0 for _ in range(n)]

# run the algoritm
best = hill_climbing(init_state, find_neighbours_NQueens, fn_evaluate, possible_values)

# print the results
print('Resulting solution: %s' % best)
print('Value of resulting solution (the closer to zero the best): %d' % fn_evaluate(best))