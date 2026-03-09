import math
from collections.abc import Callable

# Define some template classes: ==============================

class NeuralMassModel:
    def __init__(self):
        pass

# =============== Single node =============================

class SingleNodeModel(NeuralMassModel):
    def __init__(self):
        pass

class Montbrio_original(SingleNodeModel):

    def __init__(self,
                 params: dict
                 ):

        self.a = params['a']
        self.b = params['b']
        self.c = params['c']
        self.delta = params['delta']
        self.eta = params['eta']
        self.J = params['J']

        self.initialize = True

        # Brief Description from Montbrio-Pazo-Roxin 2015
        self.description = 'Heterogeneous all-to-all coupled population of N QIF neurons.'

    def step_equation(self,
                      state: dict,
                      driving_current: Callable[[int], int], time: int
                      ) -> dict[str, int]:
        a = self.a
        b = self.b
        c = self.c
        eta = self.eta
        delta = self.delta
        r = state['r']
        v = state['v']

        I = driving_current.get_current(time)
        J = self.J

        rate = delta/math.pi + 2*r*v
        voltage = v**2 + eta + J*r + I - math.pi**2*r**2

        return {'r': rate, 'v': voltage}

# ================= Basic function for testing, returns the square of values ======================

# Just a sample function to pass
def Derivation_eq(x:int, driving_current):
    x_copy = x.copy()

    for key, value in x_copy.items():
        x_copy[key] = value**2

    return x_copy

# ============= Single node with connectivity =======================

# NOT FINISHED:

class SingleNodeModelWithConnectivity(NeuralMassModel):
    def __init__(self):
        pass

class Montbrio_depanemaecker(SingleNodeModel):
    def __init__(self, params: dict):
        self.a = params['a']
        self.b = params['b']
        self.c = params['c']
        self.delta = params['delta']
        self.eta = params['eta']

        pass
        # add parameters here

    def step_equation(self, voltage, rate, driving_current):
        a = self.a
        b = self.b
        c = self.c
        eta = self.eta
        delta = self.delta
        v = voltage
        r = rate
        I = driving_current

        rate = 2*a*r*v + b*r + a*delta/math.pi
        voltage = a*v^2 + b*v + c + eta - (math.pi^2)*(r^2) + I

        return [rate, voltage]
