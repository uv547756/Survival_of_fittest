import random
POPULATION = 100
GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''
TARGET = "Utkarsh"

class Individual(object):

    def __init__(self,chromosome):
        self.chromosome = chromosome
        self.fitness = self.calc_fitness()

    def calc_fitness(self):
        global TARGET
        fitness = 0
        for gene_s, gene_t in zip(self.chromosome, TARGET):
            return sum(1 for gene_s, gene_t in zip(self.chromosome, TARGET) if gene_s != gene_t)
        return fitness

    @classmethod
    def mutated_genes(self):
        global GENES
        gene = random.choice(GENES)
        return gene

    @classmethod
    def genome_creation(self):
        global TARGET
        genome_len = len(TARGET)
        return [self.mutated_genes() for _ in range(genome_len)]
    
    def mate(self,partner):
        child = []
        for gparent1, gparent2 in zip(self.chromosome, partner.chromosome):
            prob = random.random()
            if prob < 0.45:
                child.append(gparent1)
            elif prob < 0.90:
                child.append(gparent2)
            else:
                child.append(self.mutated_genes())
        return Individual(child)
def main():
    global POPULATION
    generation = 1
    found = False
    # pop = []
    population = [Individual(Individual.genome_creation()) for _ in range(POPULATION)]

    while not found:
        population = sorted(population, key = lambda x:x.fitness)
        if population[0].fitness == 0:
            found = True
            break

        new_gen = []
        top_10 = int(0.10*POPULATION)
        new_gen.extend(population[:top_10])
        # only 10% shall survive

        for _ in range(POPULATION - top_10):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            child = parent1.mate(parent2)
            new_gen.append(child)

        population = new_gen
        
        print(f"Generation: {generation}\tString: {''.join(population[0].chromosome)}\tFitness: {population[0].fitness}")      
        generation += 1
    
    print(f"Generation: {generation}\tString: {''.join(population[0].chromosome)}\tFitness: {population[0].fitness}")

if __name__ == "__main__":
    main()
    



