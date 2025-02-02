import numpy as np
import multiprocessing as mp
from typing import List, Tuple
import random

class TSPGeneticSolver:
    def __init__(self, distance_matrix: np.ndarray, population_size: int = 100, 
                 generations: int = 500, mutation_rate: float = 0.01):
        """
        Initialize TSP Genetic Algorithm solver
        
        :param distance_matrix: 2D numpy array of distances between cities
        :param population_size: Number of routes in each generation
        :param generations: Number of evolutionary generations
        :param mutation_rate: Probability of mutation for each gene
        """
        self.distance_matrix = distance_matrix
        self.num_cities = distance_matrix.shape[0]
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate

    def create_initial_population(self) -> List[List[int]]:
        """Create initial population of random routes"""
        population = []
        for _ in range(self.population_size):
            route = list(range(self.num_cities))
            random.shuffle(route)
            population.append(route)
        return population

    def calculate_route_distance(self, route: List[int]) -> float:
        """Calculate total distance of a route"""
        total_distance = sum(
            self.distance_matrix[route[i]][route[i+1]] 
            for i in range(len(route)-1)
        )
        total_distance += self.distance_matrix[route[-1]][route[0]]  # Return to start
        return total_distance

    def crossover(self, parent1: List[int], parent2: List[int]) -> List[int]:
        """Ordered crossover (OX) for generating offspring"""
        start, end = sorted(random.sample(range(self.num_cities), 2))
        child = [None] * self.num_cities
        child[start:end+1] = parent1[start:end+1]
        
        remaining = [city for city in parent2 if city not in child[start:end+1]]
        j = 0
        for i in range(self.num_cities):
            if child[i] is None:
                child[i] = remaining[j]
                j += 1
        
        return child

    def mutate(self, route: List[int]) -> List[int]:
        """Swap mutation"""
        if random.random() < self.mutation_rate:
            i, j = random.sample(range(self.num_cities), 2)
            route[i], route[j] = route[j], route[i]
        return route

    def tournament_selection(self, population: List[List[int]], fitness_scores: List[float]) -> List[int]:
        """Tournament selection for parent selection"""
        tournament_size = 5
        tournament = random.sample(list(zip(population, fitness_scores)), tournament_size)
        return min(tournament, key=lambda x: x[1])[0]

    def solve_parallel(self) -> Tuple[List[int], float]:
        """Solve TSP using parallel genetic algorithm"""
        population = self.create_initial_population()
        
        for generation in range(self.generations):
            # Parallel fitness calculation
            with mp.Pool() as pool:
                fitness_scores = pool.map(self.calculate_route_distance, population)
            
            # Create next generation
            new_population = []
            
            while len(new_population) < self.population_size:
                parent1 = self.tournament_selection(population, fitness_scores)
                parent2 = self.tournament_selection(population, fitness_scores)
                
                child = self.crossover(parent1, parent2)
                child = self.mutate(child)
                
                new_population.append(child)
            
            population = new_population
        
        # Find best route
        fitness_scores = [self.calculate_route_distance(route) for route in population]
        best_route_index = fitness_scores.index(min(fitness_scores))
        
        return population[best_route_index], min(fitness_scores)

def generate_random_distance_matrix(num_cities: int, max_distance: int = 100) -> np.ndarray:
    """Generate a symmetric random distance matrix"""
    matrix = np.random.randint(1, max_distance, size=(num_cities, num_cities))
    matrix = (matrix + matrix.T) // 2
    np.fill_diagonal(matrix, 0)
    return matrix

def main():
    # Example usage
    num_cities = 20
    distance_matrix = generate_random_distance_matrix(num_cities)
    
    solver = TSPGeneticSolver(
        distance_matrix, 
        population_size=200, 
        generations=500, 
        mutation_rate=0.02
    )
    
    best_route, best_distance = solver.solve_parallel()
    
    print(f"Best Route: {best_route}")
    print(f"Total Distance: {best_distance}")

if __name__ == "__main__":
    main()