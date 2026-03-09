
# ============= Importing packages ====================
import matplotlib.pyplot as plt
import math

# ============= Importing our nmm package =================
from nmm import *

# ================== Defining simulation ==============
# Simulation parameters: ==============================
# =====================================================

step_size = 0.01 # in 'milliseconds' (technically dimensionless)
sim_length = 40 # in 'seconds'

# default Montbrio parameters from paper:
default_montbrio_params = {
    'J': 15,
    'eta': -5,
    'delta': 1,
    'a': 1,
    'b': 1,
    'c': 1
}

# initial conditions also from paper:
initial_conditions = {
    'r': 0,
    'v': -2
}

# ============= Creating objects ======================
# ====== Model object: ================================
model_montbrio = Montbrio_original(default_montbrio_params)

# ====== Integrator object: ===========================
integrator_euler = EulerIntegrator(h = step_size)

# ====== Current driver object:  ======================
blockcurrentdriver = DrivingCurrentBlock(0, 30, 3)

# ====== Defining simulations: ========================
new_sim = Simulator(model_object = model_montbrio,
                    integrator = integrator_euler,
                    driving_current=blockcurrentdriver)

# # ====== Calling simulator object to generate timeseries:
sim_timeseries = new_sim.simulate(simulation_length=sim_length,
                                  step_size = step_size,
                                  initial_conditions=initial_conditions
                                  )
# ====== Visualizing results ============================
print(type(sim_timeseries))
print(sim_timeseries.keys())
print(sim_timeseries['state_vector'].keys())

time = sim_timeseries['time']
r = sim_timeseries['state_vector']['r']
v = sim_timeseries['state_vector']['v']

plt.subplot(3, 1, 1)
ax = plt.gca()
ax.set_xlim([-10, sim_length])
plt.plot(time, r)

plt.subplot(3, 1, 2)
ax = plt.gca()
ax.set_xlim([-10, sim_length])
plt.plot(time, v)

plt.subplot(3, 1, 3)


timeseries_y = {'time': {},
                'y_val': []
                }

timeseries_y['time'] = [x/100 for x in range(20000)]

for x in range(20000):
    true_x = x/100
    timeseries_y['y_val'].append(blockcurrentdriver.get_current(true_x))

plt.plot(timeseries_y['time'], timeseries_y['y_val'])
ax = plt.gca()
ax.set_xlim([-10, sim_length])

plt.show()

# ====== Creating seconds simulation: =================
# ====== Model object: ================================

initial_conditions = {
    'r': 0,
    'v': -2
}

sim_length = 80

sine_driver = DrivingCurrentSinusoid(timestart = 5,
                                     initial_current = 3,
                                     time_multiplier = (math.pi/20)
                                     )

new_sim_sine = Simulator(model_object = model_montbrio,
                         integrator = integrator_euler,
                         driving_current=sine_driver)

sine_driven_timeseries = new_sim_sine.simulate(simulation_length=sim_length,
                                               step_size = step_size,
                                               initial_conditions=initial_conditions
                                               )


# ====== Analyzing results: ===========================
# =====================================================

time = sine_driven_timeseries['time']
r = sine_driven_timeseries['state_vector']['r']
v = sine_driven_timeseries['state_vector']['v']

plt.subplot(3,1,1)
plt.plot(time, r)

plt.subplot(3,1,2)
plt.plot(time, v)

plt.subplot(3, 1, 3)

timeseries_y = {'time': {},
                'y_val': []
                }

timeseries_y['time'] = [x/100 for x in range(20000)]

for x in range(20000):
    true_x = x/100
    timeseries_y['y_val'].append(sine_driver.get_current(true_x))

plt.plot(timeseries_y['time'], timeseries_y['y_val'])

plt.show()