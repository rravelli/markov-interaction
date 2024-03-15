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

    def simulate(self, max_iter: int = None):
        if max_iter is None:
            while True:
                val = self.iterate()
                if val:
                    return val
        else:
            for _ in range(max_iter):
                val = self.iterate()
                if val:
                    return val


def monte_carlo(delta: float, epsilon: float, val=1):
    sum = 0
    N = int((log(2) - log(delta)) / (2 * epsilon) ** 2) + 1
    for _ in range(N):
        sum += Simulation().simulate(max_iter=5) == val

    return sum / N, N


def sprt(
    theta: float,
    alpha: float = 0.01,
    beta: float = 0.01,
    epsilon: float = 0.01,
):
    i = 1
    k = 5
    gamma1 = theta - epsilon
    gamma0 = theta + epsilon
    A = (1 - beta) / alpha
    B = beta / (1 - alpha)

    done = False
    m = 0
    Rm = 1

    while not done:
        val = Simulation().simulate(max_iter=k)
        m += 1
        if val == i:
            Rm *= gamma1 / gamma0
        else:
            Rm *= (1 - gamma1) / (1 - gamma0)
        if Rm >= A:
            print(f"gamma<{gamma1}")
            print(m)
            return gamma1
        if Rm <= B:
            print(f"gamma>={gamma0}")
            print(m)
            return gamma0


sprt(theta=0.1)
print(monte_carlo(0.05, 0.01, 1), 1 / 6)
