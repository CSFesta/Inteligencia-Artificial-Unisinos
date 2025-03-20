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

class EvaluateGC:
    def __init__(self, graph):
        self.graph = graph

    def __call__(self, individual):
        score = 0
        for node, neighbors in self.graph.items():
            for neighbor in neighbors:
                if individual[node] != individual[neighbor]:
                    score += 1
        return score // 2  # Each edge counted twice

# Petersen Graph Definition
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

# Set of possible colors
possible_values = ['R', 'G', 'B']

# Length of an individual
individual_length = len(petersen)

# Fitness function instance
fn_fitness = EvaluateGC(petersen)

# Population size
population_size = 8

# Initial population
population = init_population(population_size, possible_values, individual_length)

# Run the genetic algorithm
solution = genetic_algorithm(population, fn_fitness, gene_pool=possible_values, fn_thres=10)

# Print the results
print(f'Resulting solution: {solution}')
print(f'Value of resulting solution: {fn_fitness(solution)}')
