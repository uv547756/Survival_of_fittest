import random
import re
POPULATION = 100
GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''
TARGET = "Utkarsh"

class Individual(object):

    def __init__(self):
        self.chromosome = chromosome
        self.fitness = calc_fitness()

    @classmethod
    def calc_fitness(self):
        global TARGET
        fitness = 0
        for gene_s, gene_t in zip(self.chromosome, chromosome)
            if gene_s != gene_t: fitness += 1
        return fitness

    def mutated_genes(self):
        global GENES
        gene = random.choice(GENES)
        return gene

    @classmethod
    def genome_creation(self):
        global TARGET
        genome_len = len(TARGET)
        return [self.mutated_genes() for _ in range(genome_len)]
    
    def mate(self):
        child = []
        for gparent1, gparent2 in zip(self.chromosome, par2.chromosome):
            prob = random.random()
            if prob < 0.4:
                child.append(gparent1)
            elif prob < 0.9:
                child.append(gparent2)
            else:
                child.append(self.mutated_genes())
        return Individual(child)
def main():
    global pop_size
    generation = 1
    found = False
    pop = []

    for _ in range(pop_size):
        genome = Individual.genome_creation()
        pop.append(Individual(genome))

    while not found:
        pop = sorted(pop, key = lambda x:x.calc_fitness)


