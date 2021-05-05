import pygad
import numpy as np
import sys

function_inputs = [2.5, 1.4, -5.3, -10.8, 7.5]

desired_output = 26.7

print_flag = False
def fitness_func(solution, solution_idx):
    output = np.sum(solution * function_inputs)
    fitness = 1.0 / np.abs(output - desired_output)
    return fitness


# some params
num_generations = 200
num_parents_mating = 4
sol_per_pop = 40
num_genes = len(function_inputs)
init_range_low = -2
init_range_high = 5
mutation_percent_genes = 1

ga_instance = pygad.GA(
    num_generations=200,
    num_parents_mating=num_parents_mating,
    fitness_func=fitness_func,
    sol_per_pop=sol_per_pop,
    num_genes=num_genes,
    init_range_low=init_range_low,
    init_range_high=init_range_high,
    mutation_percent_genes=mutation_percent_genes,
)

ga_instance.run()
#ga_instance.plot_result()

# get the best solution
solution, solution_fitness, solution_idx = ga_instance.best_solution()
if print_flag:
    ga_instance.plot_result()
    print("Parameters of the best solution : {solution}".format(solution=solution))
    print(
        "Fitness value of the best solution = {solution_fitness}".format(
            solution_fitness=solution_fitness
        )
    )
    print("Index of the best solution : {solution_idx}".format(solution_idx=solution_idx))


f = open("w_fitted.txt", "r+")
f.read()
for i in range(len(function_inputs)):
    f.write(str(solution[i]) + " ")
f.write("\n")
f.close()