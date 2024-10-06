from genetic_library.genetic_algorithm import GeneticAlgorithm
from genetic_library.utils import generate_population, calculate_average_fitness
import random

# Generar una población inicial usando la función del archivo utils.py
initial_population = generate_population(10, 6)  # Población de 10 individuos con cromosomas de longitud 6

# Función de aptitud: cuenta cuántos 1s hay en el cromosoma
def fitness_function(chromosome):
    return sum(chromosome)

# Calcular la aptitud promedio de la población inicial
average_fitness = calculate_average_fitness(initial_population, fitness_function)
print(f"Aptitud promedio de la población inicial: {average_fitness}")

# Inicializar el algoritmo genético
ga = GeneticAlgorithm(
    initial_population, 
    fitness_function,
    crossover_type="two_point",  # Usar cruce de dos puntos
    mutation_type="swap",        # Usar mutación de intercambio
    selection_type="roulette",   # Usar selección por ruleta
    elitism=True                 # Activar elitismo (el mejor pasa directamente)
)

# Ejecutar el algoritmo por 10 generaciones
ga.run(10)
