import random

class Individual(object):
    def __init__(self, chromosome, target, genes, lookup):
        self.chromosome = chromosome
        self.target = target
        self.genes = genes
        self.lookup = lookup
        self.fitness = self.cal_fitness()  # Calculate fitness 

    def mutated_genes(self):
        gene = random.choice(self.genes)
        return gene

    @classmethod
    def create_gnome(cls, size):
        gnome = []
        for _ in range(size):
            gnome.append(random.choice('01'))  # Randomly assign 0 or 1
        return gnome

    def mate(self, par2):
        child_chromosome = []
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):
            prob = random.random()
            if prob < 0.45:
                child_chromosome.append(gp1)
            elif prob < 0.90:
                child_chromosome.append(gp2)
            else:
                child_chromosome.append(self.mutated_genes())
        return Individual(child_chromosome, self.target, self.genes, self.lookup)

    def cal_fitness(self):
        weight = 0
        score = 0
        for i in range(len(self.chromosome)):
            if self.chromosome[i] == '1': 
                option_label = list(self.lookup.keys())[i]
                obj = self.lookup[option_label]
                weight += obj[0]  # Add the weight of the item
                score += obj[1]   # Add the value of the item

        if weight > self.target:  
            return -1
        return score  
