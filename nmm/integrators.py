import matplotlib.pyplot as plt
from collections.abc import Callable

# Parent class for Integrator, so far not in use
class Integrator:
    def __init__(self):
        pass

class EulerIntegrator(Integrator):
    def __init__(self, h: int):
        # this is the only common variable because it is for the entire simulation
        self.h = h

    def integrate(self,
                  derivation_equation,
                  state: dict[str, int],
                  time: float,
                  driving_current: Callable([])
                  ) -> dict[str, int]:

        # for each variable in the state vector - use Euler to change value
        for key, value in state.items():
            state[key] = value + self.h * derivation_equation(state, driving_current, time)[key]

            print(f'Key = {key}, Value = {value}')

        # Increment time after integrating all variables
        time = time + self.h

        return {'state_vector': state, 'time': time}


class RungeKuttaFourthOrder(Integrator):
    def __init__(self, h: int):
        self.h = h

    def integrate(self,
                  derivation_equation: Callable[[dict, Callable[[int], int], int], dict[str, int]],
                  state: dict[str: list],
                  time: int,
                  driving_current: Callable[[int], int]) -> list:

        dvs = derivation_equation(state, driving_current, time)
        print(f'dvs = {dvs}')

        for key, value in state.items():

            k1 = derivation_equation(time = time,
                                     state = state[key],
                                     driving_current = driving_current
                                     )[key]

            k2 = derivation_equation(time = time+self.h/2,
                                     state = k1[key]*(self.h/2),
                                     driving_current = driving_current
                                     )[key]

            k3 = derivation_equation(time = time+(self.h/2),
                                     state = k2[key]*(self.h/2),
                                     driving_current = driving_current
                                     )[key]

            k4 = derivation_equation(time = time + self.h,
                                     state = state[key]+self.h*k3[key],
                                     driving_current = driving_current
                                     )[key]

            state[key] = state[key] + ((self.h/6) * (k1 + 2*k2 + 2*k3 + k4))

            print(f'Key = {key}, Value = {value}')

        time = time + self.h

        return {'state_vector': state, 'time': time}



# Just a sample function to pass
def Derivation_eq(x:int, driving_current):
    x_copy = x.copy()

    for key, value in x_copy.items():
        x_copy[key] = value**2

    return x_copy




