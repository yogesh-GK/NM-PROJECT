import matplotlib.pyplot as plt

# Simulated time (hours in a day)
time = list(range(0, 24))

# Simulated sensor data
temperature = [22, 21, 20, 20, 21, 23, 25, 28, 30, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 21, 22, 23]
occupancy = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
energy_usage = [0.2, 0.2, 0.2, 0.3, 1.5, 2.0, 2.3, 3.0, 3.5, 3.8, 3.7, 3.6, 3.4, 3.3, 3.2, 3.0, 2.8, 2.5, 2.3, 2.0, 1.0, 0.8, 0.6, 0.4, 0.3]

# Plotting the data
plt.figure(figsize=(10, 6))

# Plot temperature
plt.plot(time, temperature, label='Temperature (°C)', color='orange', marker='o')

# Plot occupancy
plt.plot(time, occupancy, label='Occupancy (0/1)', color='green', linestyle='--')

# Plot energy usage
plt.plot(time, energy_usage, label='Energy Usage (kWh)', color='blue', marker='s')

# Formatting the graph
plt.title('Energy Efficiency Data Visualization')
plt.xlabel('Time (Hour of Day)')
plt.ylabel('Values')
plt.legend()
plt.grid(True)
plt.xticks(time)

# Show the plot
plt.tight_layout()
plt.show()
