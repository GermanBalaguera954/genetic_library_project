import random

class GeneticAlgorithm:
    def __init__(self, population, fitness_function, crossover_prob=0.8, mutation_prob=0.01, crossover_type="single_point", mutation_type="flip", selection_type="tournament", elitism=False):
        self.population = population
        self.fitness_function = fitness_function
        self.crossover_prob = crossover_prob
        self.mutation_prob = mutation_prob
        self.crossover_type = crossover_type  # Tipo de cruce: single_point, two_point
        self.mutation_type = mutation_type    # Tipo de mutación: flip, swap
        self.selection_type = selection_type  # Tipo de selección: tournament, roulette
        self.elitism = elitism  # Si True, conserva el mejor individuo

    def select(self):
        if self.selection_type == "tournament":
            # Selección por torneo simple
            selected = random.sample(self.population, 2)
            selected.sort(key=self.fitness_function, reverse=True)
            return selected[0]
        elif self.selection_type == "roulette":
            # Selección por ruleta
            max_fitness = sum(self.fitness_function(ind) for ind in self.population)
            pick = random.uniform(0, max_fitness)
            current = 0
            for individual in self.population:
                current += self.fitness_function(individual)
                if current > pick:
                    return individual

    def crossover(self, parent1, parent2):
        if random.random() < self.crossover_prob:
            if self.crossover_type == "single_point":
                # Cruce de un solo punto
                crossover_point = random.randint(1, len(parent1) - 1)
                child1 = parent1[:crossover_point] + parent2[crossover_point:]
                child2 = parent2[:crossover_point] + parent1[crossover_point:]
            elif self.crossover_type == "two_point":
                # Cruce de dos puntos
                point1 = random.randint(1, len(parent1) - 2)
                point2 = random.randint(point1, len(parent1) - 1)
                child1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
                child2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]
            return child1, child2
        else:
            return parent1, parent2

    def mutate(self, individual):
        if self.mutation_type == "flip":
            # Mutación por voltear (cambiar de 0 a 1 o viceversa)
            mutated = []
            for gene in individual:
                if random.random() < self.mutation_prob:
                    mutated.append(1 - gene)  # Cambia 0 a 1 y viceversa
                else:
                    mutated.append(gene)
            return mutated
        elif self.mutation_type == "swap":
            # Mutación de intercambio (intercambia dos posiciones)
            if random.random() < self.mutation_prob:
                pos1 = random.randint(0, len(individual) - 1)
                pos2 = random.randint(0, len(individual) - 1)
                individual[pos1], individual[pos2] = individual[pos2], individual[pos1]
            return individual

    def run(self, generations):
        for _ in range(generations):
            new_population = []
            if self.elitism:
                # Mantiene al mejor individuo sin cambios
                best = max(self.population, key=self.fitness_function)
                new_population.append(best)

            while len(new_population) < len(self.population):
                parent1 = self.select()
                parent2 = self.select()
                child1, child2 = self.crossover(parent1, parent2)
                child1 = self.mutate(child1)
                child2 = self.mutate(child2)
                new_population.extend([child1, child2])

            self.population = new_population[:len(self.population)]
            best = max(self.population, key=self.fitness_function)
            print(f"Mejor solución: {best} con aptitud: {self.fitness_function(best)}")