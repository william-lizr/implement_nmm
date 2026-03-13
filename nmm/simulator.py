

# === Essentially a simulator loop ====================
# =====================================================

class Simulator:

    def __init__(self,
                 model_object,
                 integrator,
                 driving_current):

        self.model_object = model_object
        self.integrator_object = integrator
        self.driving_current = driving_current

    # Instantiating simulator loop using the objects passed in constructor.
    # all changing parameters are passed to simulate() function - simulation_length, step_size, initial_conditions
    # simulate() is the function invoked to actually generate a simualted timeseries

    def simulate(self,
                 simulation_length: int,
                 step_size: float,
                 initial_conditions: dict[str, int]
                 ) -> dict:

        self.simulation_length: float = simulation_length
        self.step_size: float = step_size
        self.state_current = initial_conditions
        self.simulation_steps: int = int(self.simulation_length/self.step_size)

        # Creating the timeseries we will use to track all values of the state vector
        self.state_vectors = {}

        # Changing the values of all state vector values to list so we can append later
        for key, value in self.state_current.items():
            self.state_vectors[key] = [value]

        print(f'initial_conditions: {self.state_current}')
        print(f'state_vectors: {self.state_vectors}')

        self.state_timeseries = {'time': [0], 'state_vector': self.state_vectors}

        print('Initiating simulation')

        # Main simulation loop
        # Calls the integrate() function from our integrator object
        # => integrate() calls the get_current() function from the driving_current object we pass down
        # get_current() takes the timepoint from the time parameter to accurately return the driving current
        for x in range(self.simulation_steps):
            integrated = self.integrator_object.integrate(
                                            derivation_equation=self.model_object.step_equation,
                                            state=self.state_current,
                                            time=x * self.step_size,
                                            driving_current=self.driving_current)

            print(f'Step: {x}, time: {integrated["time"]}, state vector: {integrated["state_vector"]}')

            self.state_timeseries['time'].append(integrated['time'])

            # Generated values (dictionary) are appended to state vector dictionary
            # Structure:
            # state_timeseries:
            # time: [list of timepoints]
            # state_vector: {dictionary of state variable timeseries}
            #           state_variable_1: [list of values at each timepoint]
            #           ...other state variables...

            for key, value in self.state_timeseries['state_vector'].items():
                self.state_timeseries['state_vector'][key].append(integrated['state_vector'][key])

        return self.state_timeseries
