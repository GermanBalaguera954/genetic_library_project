# Genetic Library

Esta es una librería de Python para implementar **algoritmos genéticos**.

## Instalación

```bash
pip install genetic_library

# Ejemplo de cómo usar esta librería

from genetic_library.genetic_algorithm import GeneticAlgorithm
import random

# Definir una función de aptitud
def fitness_function(chromosome):
    return sum(chromosome)

# Crear una población inicial
initial_population = [[random.randint(0, 1) for _ in range(6)] for _ in range(10)]

# Configurar el algoritmo genético
ga = GeneticAlgorithm(
    population=initial_population,
    fitness_function=fitness_function,
    crossover_type="two_point",
    mutation_type="swap",
    selection_type="roulette",
    elitism=True
)

# Ejecutar el algoritmo
ga.run(10)
