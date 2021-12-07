from .core import Gene
import math


class Check:
    def __init__(self, state: Gene) -> None:
        self.state = state.state
        self.env_n = len(state.state)

    def max(self):
        return int(self.env_n * (self.env_n-1) /2)
    def occures(self):
        is_safe = False
        max = self.max() 
        occures = 0
        for index in range(0, len(self.state)):
            item = self.state[index]
            for i in range(index + 1, len(self.state)):
                occures = (
                    occures + 1
                    if item == self.state[i] or abs(item - self.state[i]) == i - index
                    else occures
                )
        return occures
