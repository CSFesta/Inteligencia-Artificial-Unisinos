import random
import bisect

# Genetic Algorithm Implementation
def genetic_algorithm(population, fn_fitness, gene_pool, fn_thres=None, ngen=1000, pmut=0.1):
    for _ in range(ngen):
        new_population = []
        
        for _ in range(len(population)):
            p1, p2 = select(2, population, fn_fitness)
            child = recombine(p1, p2)
            child = mutate(child, gene_pool, pmut)
            new_population.append(child)
        
        population = new_population
        
        fittest_individual = fitness_threshold(fn_fitness, fn_thres, population)
        if fittest_individual:
            return fittest_individual
    
    return max(population, key=fn_fitness)

# Check if any individual meets the fitness threshold
def fitness_threshold(fn_fitness, fn_thres, population):
    if not fn_thres:
        return None
    
    fittest_individual = max(population, key=fn_fitness)
    if fn_fitness(fittest_individual) >= fn_thres:
        return fittest_individual
    
    return None

# Selection of individuals based on fitness
def select(r, population, fn_fitness):
    fitnesses = map(fn_fitness, population)
    sampler = weighted_sampler(population, fitnesses)
    return [sampler() for _ in range(r)]

# Create a weighted sampler based on fitness
def weighted_sampler(seq, weights):
    totals = []
    for w in weights:
        totals.append(w + totals[-1] if totals else w)
    return lambda: seq[bisect.bisect(totals, random.uniform(0, totals[-1]))]

# Recombination of two individuals
def recombine(x, y):
    n = len(x)
    c = random.randrange(0, n)
    return x[:c] + y[c:]

# Mutation process
def mutate(x, gene_pool, pmut):
    if random.uniform(0, 1) >= pmut:
        return x
    
    c = random.randrange(0, len(x))
    r = random.randrange(0, len(gene_pool))
    new_gene = gene_pool[r]
    return x[:c] + [new_gene] + x[c+1:]

# Initialize population
def init_population(pop_number, gene_pool, state_length):
    g = len(gene_pool)
    return [[gene_pool[random.randrange(0, g)] for _ in range(state_length)] for _ in range(pop_number)]

# Evaluation class for N-Queens Problem
class EvaluateNQueens:
    def __init__(self, n):
        self.n = n

    def __call__(self, solution):
        conflicts = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if solution[i] == solution[j] or \
                   abs(solution[i] - solution[j]) == abs(i - j):
                    conflicts += 1
        max_conflicts = self.n * (self.n - 1) // 2
        fitness = max_conflicts - conflicts
        return fitness

# Instance of the N-Queens problem
n = 8

# Create an instance of the evaluation class for the considered problem instance
fn_fitness = EvaluateNQueens(n)

# Set of possible values (each queen in a row, column defined by index)
possible_values = list(range(n))

# Initial population
population_size = 8
population = init_population(population_size, possible_values, n)

# Run the genetic algorithm
solution = genetic_algorithm(population, fn_fitness, gene_pool=possible_values, fn_thres=28, ngen=1000)

# Print the results
print(f'Resulting solution: {solution}')
print(f'Value of resulting solution (the higher the better): {fn_fitness(solution)}')
