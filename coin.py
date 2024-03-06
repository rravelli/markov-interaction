from random import random
from math import log


class Simulation:

    def __init__(self) -> None:
        self.state = "s0"
        self.graph = {"s0": []}

    def iterate(self):
        r = random()
        match self.state:
            case "s0":
                if r > 1 / 2:
                    self.state = "s1"
                else:
                    self.state = "s2"
            case "s1":
                if r > 1 / 2:
                    self.state = "s3"
                else:
                    self.state = "s4"
            case "s2":
                if r > 1 / 2:
                    self.state = "s5"
                else:
                    self.state = "s6"
            case "s3":
                if r > 1 / 2:
                    self.state = "s1"
                else:
                    return 1
            case "s4":
                if r > 1 / 2:
                    return 2
                else:
                    return 3
            case "s5":
                if r > 1 / 2:
                    return 4
                else:
                    return 5
            case "s6":
                if r > 1 / 2:
                    self.state = "s2"
                else:
                    return 6

    def simulate(self):
        while True:
            val = self.iterate()
            if val:
                return val


def bernoulli(delta: float, epsilon: float, val=1):
    sum = 0
    N = int((log(2) - log(delta)) / (2 * epsilon) ** 2) + 1
    for _ in range(N):
        sum += Simulation().simulate() == val

    return sum / N


print(bernoulli(0.05, 0.01, 2), 1 / 6)
