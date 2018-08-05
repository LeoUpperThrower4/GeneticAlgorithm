# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 02:02:42 2018

@author: Leo
"""

import numpy as np
import operator
import matplotlib.pyplot as plt

#GA variables
generations = 100
pop_size = 100
target = 10
mutate_prob = 0.1

best_of_each_gen = []

class Individual:
    gene = []
    fitness = None


class Population:
    members = []
    fitness_history = []


def Initialization(size):

    initial_population = []

    for _ in range(size):
        ind = Individual()
        ind.gene = np.random.randint(0, 101, 10)
        ind.fitness = np.sum(ind.gene)
        initial_population.append(ind)

    initial_population = sorted(initial_population, key=operator.attrgetter('fitness'))
    return initial_population


def Evaluation(pop):
    #individual's fitness
    for i in pop:
        i.fitness = (sum(i.gene))
    return pop


def Selection(pop):
    #Sorting by fitness
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

def Visualization(x, y):
    plt.scatter(x,y)
    plt.show()

if __name__ == "__main__":

    population = Population()
    population.members = Initialization(pop_size)

    for _ in range(generations):
        
        population.members = Evaluation(population.members)
        population.members = Selection(population.members)
        population.members = TPCrossover(population.members)
        best_of_each_gen.append(population.members[-1])
    
    
    #Visualization
    population.fitness_history = []
    for ind in population.members:
        population.fitness_history.append(ind.fitness)    
    x = np.arange(0, len(population.members), 1, dtype=int)
    Visualization(x, population.fitness_history)
    
    
    beg = []
    for i in sorted(best_of_each_gen, key=operator.attrgetter('fitness')):
        beg.append(i.fitness)
    
    x = np.arange(0, generations, 1, dtype=int)
    Visualization(x, beg)
