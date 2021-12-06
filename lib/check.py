from .core import Gene
import math


class Check:
    def __init__(self, state: Gene) -> None:
        self.state = state.state
        self.env_n = len(state.state)

    def proc(self):
        is_safe = False
        for index in range(0, len(self.state)):
            item = self.state[index]


            # if item in tmp:
            #     return  False
            for i in range(index + 1, len(self.state)):
                is_safe = item == self.state[i] or abs(item-self.state[i]) == i-index or is_safe
        return is_safe