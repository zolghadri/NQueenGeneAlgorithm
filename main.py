import random
from lib.check import Check
from lib.core import Gene
from lib.visual import Display

random_init = [i for i in range(1, 9)]

random.shuffle(random_init)
gene1 = Gene(random_init.copy())

random.shuffle(random_init)
gene2 = Gene(random_init.copy())

random.shuffle(random_init)
gene3 = Gene(random_init.copy())

random.shuffle(random_init)
gene4 = Gene(random_init.copy())


def mutation(gene1: Gene, gene2: Gene):
    random_selection = random.randint(0, min(len(gene1.state),len(gene2.state) ))
    return (
        Gene(gene1.state[0:random_selection] + gene2.state[random_selection:]),
        Gene(gene1.state[random_selection:] + gene2.state[:random_selection]),
    )


def generator(max_generate: int, genes: list) -> Gene:
    genes_count = len(genes)
    goal = None
    max_fitness = 0
    for generation in range(1, max_generate + 1):
        print(f"generations {generation}:")
        for gene in genes:
            fitness = gene.fitness()
            # print(f"{gene} : {gene.fitness()}")
            goal, max_fitness = (
                (gene, fitness) if fitness > max_fitness else (goal, max_fitness)
            )
        for gene_index in range(0, len(genes) )[::2]:
            genes[gene_index], genes[gene_index + 1] = mutation(
                genes[gene_index], genes[gene_index + 1]
            )
    return goal


if __name__ == "__main__":
    goal = generator(
        100,
        genes=[
            gene1,
            gene2,
            gene3,
            gene4,
        ],
    )

    print(f"\n{goal} {goal.fitness()}")
    #     print()
    #     check  = Check(state0)
    #     print(f"max: : {check.max()}")
    #     print(f"total occures: {check.occures()}")
    Display(goal, len(goal.state)).show()
