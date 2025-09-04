# Practice code for data visualization.
import matplotlib.pyplot as plt

# Hypothetical data for appliance energy consumption (kWh)
appliances = ['Air Conditioner', 'Refrigerator', 'Washing Machine', 'Television', 'Lights']
energy_consumption = [200, 150, 100, 80, 50]  # kWh

# Cost per kWh for electricity and solar energy
electricity_cost_per_kWh = 0.12  # USD/kWh
solar_energy_cost_per_kWh = 0.02  # USD/kWh
solar_installation_cost = 500  # One-time cost in USD

# Add code to calculate the monthly costs for electricity and solar energy (excluding installation for solar)
electricity_cost = []
solar_cost = []
solar_total_cost = []  # Installation cost added only for the first appliance

# Add solar total cost (installation + monthly cost) for solar energy
solar_total_cost = [total_cost + monthly_cost for total_cost, monthly_cost in zip(solar_total_cost, solar_cost)]

# Plot Bar Graph


# Bar plot for electricity vs solar monthly cost




