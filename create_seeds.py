import random
import json

class UniformGenerator:
    def __init__(self, seed):
        random.seed(seed)  

    def uniform_generator(self):
        return random.uniform(1, 2147483647)
    
uniformGenerator = UniformGenerator(seed = 2256)
no_simulations = 10
no_vars = 4
no_of_rands = 100000
file_name = "seeds.json"
seeds = []
seed_set = []

for no_simulation in range(no_simulations):
    for no_var in range(no_vars):
        for no_of_rand in range(no_of_rands):
            uniformGenerator.uniform_generator()
        seed_set.append(int(uniformGenerator.uniform_generator()))
    seeds.append(seed_set)
    seed_set = []


with open(file_name, 'w') as file_json:
    json.dump(seeds, file_json)