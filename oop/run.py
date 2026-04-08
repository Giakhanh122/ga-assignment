from src.onemax import *

pop = Population(size=50, length=100)

ga = GeneticAlgorithm(
    population=pop,
    selection=TournamentSelection(),
    crossover=OnePointCrossover(length=100),
    mutation=BitFlipMutation(prob=0.01),
    generations=80
)

best = ga.run()

print("Best:", best)
print("Fitness:", best.fitness())

