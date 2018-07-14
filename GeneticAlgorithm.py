# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 02:02:42 2018

@author: Leo
"""

import numpy as np
import operator
#GA variables
generations = 100
pop_size = 10
target = 900
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
        ind.fitness = abs(target - sum(ind.gene))
        initial_population.append(ind)

    initial_population = sorted(initial_population, key=operator.attrgetter('fitness'))
    return initial_population


def Evaluation(pop):
    #Here I set the individual's fitness
    for i in pop:
        i.fitness = abs(target - sum(i.gene))
        population.fitness_history.append(i.fitness)
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


if __name__ == "__main__":

    population = Population()
    population.members = Initialization(pop_size)

    for _ in range(generations):
        population.members = Evaluation(population.members)
        population.members = Selection(population.members)
        population.members = TPCrossover(population.members)
        best_of_each_gen.append(population.members[0])

    population_visualize = sorted(population.members, key=operator.attrgetter('fitness'))
