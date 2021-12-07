



class Gene:
    def __init__(self, state: list) -> None:
        self.state = state

    def __str__(self) -> str:
        return str(self.state)
    def fitness(self)->int:
        from lib.check import Check
        check = Check(self)
        return check.max() - check.occures()