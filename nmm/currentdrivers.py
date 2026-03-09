import math
import numpy as np

# Parent class for currentdriver, so far not in use
class DrivingCurrent:
    def __init__(self):
        pass

# Simple block current used in Montbrio 2015
class DrivingCurrentBlock(DrivingCurrent):
    def __init__(self, timestart, timeend, amplitude):
        self.timestart = timestart
        self.timeend = timeend
        self.amplitude = amplitude

    # get_current is the function which will be pulled from our current_
    # driver object which we supplied to the simulator object.
    # !! current function must be named get_current as this is hardcoded.
    def get_current(self,
                    time: int
                    ) -> int:

        # Timestart, timeend logic
        if self.timeend > time and time > self.timestart:
            return self.amplitude
        else:
            return 0

# Sine current used in Montbrio 2015
class DrivingCurrentSinusoid(DrivingCurrent):
    def __init__(self,
                 timestart: int,
                 initial_current: int,
                 time_multiplier: float
                 ):

        self.timestart = timestart
        self.initial_current = initial_current
        self.time_multiplier = time_multiplier

    def get_current(self,
                    time: int
                    ) -> float:

        # From Montbrio 2015:
        # I(t) = I_0 * sin(ω*t)

        if time > self.timestart:
            return self.initial_current*(math.sin(self.time_multiplier*time))
        else:
            return 0


