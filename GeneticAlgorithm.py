# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 02:02:42 2018

@author: Leo
"""

#I'm basically trying to follow the following image: 
#https://www.google.com.br/url?sa=i&source=imgres&cd=&cad=rja&uact=8&ved=2ahUKEwid0KSf9p7cAhWBxFkKHR6MAFIQjRx6BAgBEAU&url=https%3A%2F%2Fwww.neuraldesigner.com%2Fblog%2Fgenetic_algorithms_for_feature_selection&psig=AOvVaw3hjdIumyKaR7iMozVfbBDr&ust=1531669117546438

import numpy as np
import operator
#GA variables
generations = 1000
pop_size = 100
target = 900
mutate_prob = 0.1

class Individual:
    gene = []
    fitness = None

class Population:
    members = []
    fitness_history = []

population = Population()
 
def Initialization(size):
    
    initial_population = []
    
    for _ in range(size):
        ind = Individual()
        ind.gene = np.random.randint(0, 101, 10)
        ind.fitness = (target - sum(ind.gene))
        initial_population.append(ind)
        print(ind.gene)

    initial_population = sorted(initial_population, key=operator.attrgetter('fitness'))
    return initial_population
        
    
def EvaluationSelection(pop):
    #Here I sort all population and set the individual's fitness
    for i in pop:
        i.fitness = abs(target - sum(i.gene))
        population.fitness_history.append(i.fitness)
        pop = sorted(pop, key=operator.attrgetter('fitness'))
    return pop

def TPCrossover(pop):
    #Two-Point Crossover
    offspring = []
    #Mutation
    if ((mutate_prob * np.random.randint(0, 101, 1)[0]) == 1):
        offspring = Initialization(pop_size)
    else:
        for i in range(int(len(pop)/2)):
            p1 = np.random.randint(0, len(pop[0].gene))
            p2 = np.random.randint(0, len(pop[0].gene))
        
            if p1 > p2:
                holder = p1
                p1 = p2
                p2 = holder
        
            top = pop[i]
            worst = pop[-i-1]
            top.gene[p1:p2] = worst.gene[p1:p2]
            offspring.append(top)
            offspring.append(worst)
        
    pop = offspring
    return pop

if __name__ == "__main__":
    
    population.members = Initialization(pop_size)
    
    
    for _ in range(generations):
        population.members = EvaluationSelection(population.members)
        population.members = TPCrossover(population.members)
    
    
    population_visualize = sorted(population.members, key=operator.attrgetter('fitness'))

        