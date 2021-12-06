


from lib.check import Check
from lib.core import Gene
from lib.visual import Display

state0 = Gene([2,5,3,1,4,6,8,7])

if __name__ == "__main__":
    print(state0)
    print()
    print( Check(state0).proc() )
    Display(state0, len(state0.state)).show()
    