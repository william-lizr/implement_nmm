
from nmm import EulerIntegrator

# =========== Testing ==============
# === Essentially a simulator loop =========

# initialize with starting values
current_state = {'v': 1.2,
                 'r': 1.5}

timeseries_state = {}

for key, value in current_state.items():
    timeseries_state[key] = [value]

print(f'initial_state: {current_state}')
print(f'timeseries_state: {timeseries_state}')

state_timeseries = {'time':[0],
                    'state_vector': timeseries_state}

step_size = 0.01

new_Euler = EulerIntegrator(h = step_size)

# Essentially the simulator
for x in range(50):

    integrated = new_Euler.integrate(derivation_equation = Derivation_eq,
                                     state = current_state,
                                     time = x*step_size,
                                     driving_current = 0)
    print(integrated)

    state_timeseries['time'].append(integrated['time'])

    for key, value in state_timeseries['state_vector'].items():
        state_timeseries['state_vector'][key].append(integrated['state_vector'][key])

v_state = state_timeseries['state_vector']['v']
r_state = state_timeseries['state_vector']['r']
time = state_timeseries['time']

plt.plot(time, v_state)
plt.plot(time, r_state)
plt.show()

plt.subplot(1, 2, 1)
plt.plot(time, v_state)
plt.title(f'membrane voltage')

plt.subplot(1, 2, 2)
plt.plot(time, r_state)
plt.title(f'mean firing rate')

plt.show()