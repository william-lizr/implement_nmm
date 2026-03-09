import math
import numpy as np

import matplotlib.pyplot as plt
from nmm import DrivingCurrentBlock, DrivingCurrentSinusoid

# =========== block driver =================

driver_1 = DrivingCurrentBlock(timestart = 0.5, timeend = 5, amplitude = 5)

# state = np.array([[],[]], ndmin = 2)
state = [[], []]

step = 0.01
start = 0
end = 1
steps = int((end-start)/step)

print('Steps:')
print(steps)

for x in np.linspace(start, end, steps):
    print('state[0]')
    print(state[0])
    print('state[1]')
    print(state[1])
    print('driver current')
    print(driver_1.get_current(x))

    state[0].append(float(x))
    state[1].append(driver_1.get_current(x) )

print(state[1][1:10])

plt.plot(state[0], state[1])
plt.show()

# ======== sinusoid driver =================

driver_2 = DrivingCurrentSinusoid(timestart = 2, multiplier = 5)

state_vars = {'time': [], 'current':[]}

start = 1.5
end = 6
increment = 0.01
steps = int((end-start)/increment)

for x in np.linspace(start, end, steps):
    state_vars['time'].append(float(x))
    state_vars['current'].append(driver_2.get_current(x))

plt.plot(state_vars['time'], state_vars['current'])
plt.show()


sine_driver = DrivingCurrentSinusoid(timestart = 5,
                                     initial_current = 3,
                                     time_multiplier = (math.pi/20)
                                     )

timeseries_y = {'time': {},
                'y_val': []
                }

timeseries_y['time'] = [x/100 for x in range(20000)]

for x in range(20000):
    true_x = x/100
    timeseries_y['y_val'].append(sine_driver.get_current(true_x))

plt.plot(timeseries_y['time'], timeseries_y['y_val'])
plt.show()