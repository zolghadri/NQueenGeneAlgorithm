from .core import Gene

def prt(*args):
    for arg in args:
        print(arg,end='')

class Display:
    def __init__(self, goal: Gene, n: int) -> None:
        self.items = goal.state
        self.env_n = n
    def show(self):
        for i in range(1,self.env_n+1)[::-1]:
            prt(f"{i}|")
            for j in self.items:
                if i == j:
                    prt(f"*")
                else:
                    prt(f" ")
                prt('|')
            print()
        print(2*' ',end='')
        for i in range(1,self.env_n+1):
            print(i,end=' ')
        print()
