import random

def generate_population(size, chromosome_length):
    """Genera una población inicial de cromosomas binarios aleatorios.
    
    Args:
        size (int): El tamaño de la población.
        chromosome_length (int): La longitud de cada cromosoma.
        
    Returns:
        list: Lista de cromosomas aleatorios.
    """
    return [[random.randint(0, 1) for _ in range(chromosome_length)] for _ in range(size)]

def calculate_average_fitness(population, fitness_function):
    """Calcula la aptitud promedio de la población.
    
    Args:
        population (list): Lista de cromosomas.
        fitness_function (function): La función de aptitud utilizada.
        
    Returns:
        float: La aptitud promedio de la población.
    """
    total_fitness = sum(fitness_function(individual) for individual in population)
    return total_fitness / len(population)

def validate_population(population):
    """Valida que todos los cromosomas en la población tengan la misma longitud.
    
    Args:
        population (list): Lista de cromosomas.
    
    Returns:
        bool: True si todos los cromosomas tienen la misma longitud, False en caso contrario.
    """
    chromosome_length = len(population[0])
    for individual in population:
        if len(individual) != chromosome_length:
            return False
    return True
