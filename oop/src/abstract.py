from abc import ABC, abstractmethod

class SelectionStrategy(ABC):
    @abstractmethod
    def select(self, population):
        pass



class CrossoverStrategy(ABC):
    @abstractmethod
    def crossover(self, p1, p2):
        pass


class MutationStrategy(ABC):
    @abstractmethod
    def mutate(self, chromosome):
        pass