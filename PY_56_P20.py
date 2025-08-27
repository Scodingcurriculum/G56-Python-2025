# Practice code for data visualization.
import matplotlib.pyplot as plt

# Hypothetical data for appliance energy consumption (kWh)
appliances = ['Air Conditioner', 'Refrigerator', 'Washing Machine', 'Television', 'Lights']
energy_consumption = [200, 150, 100, 80, 50]  # kWh

# Cost per kWh for electricity and solar energy
electricity_cost_per_kWh = 0.12  # USD/kWh
solar_energy_cost_per_kWh = 0.02  # USD/kWh
solar_installation_cost = 500  # One-time cost in USD

# Calculate the monthly costs for electricity and solar energy (excluding installation for solar)
electricity_cost = [consumption * electricity_cost_per_kWh for consumption in energy_consumption]
solar_cost = [consumption * solar_energy_cost_per_kWh for consumption in energy_consumption]
solar_total_cost = [solar_installation_cost if i == 0 else 0 for i in range(len(appliances))]  # Installation cost added only for the first appliance

# Add solar total cost (installation + monthly cost) for solar energy
solar_total_cost = [total_cost + monthly_cost for total_cost, monthly_cost in zip(solar_total_cost, solar_cost)]

# Plot Bar Graph
plt.figure(figsize=(12, 6))

# Bar plot for electricity vs solar monthly cost
plt.subplot(1, 2, 1)
bar_width = 0.35
index = range(len(appliances))

plt.bar(index, electricity_cost, bar_width, label='Electricity', color='blue')
plt.bar([i + bar_width for i in index], solar_cost, bar_width, label='Solar', color='green')

plt.xlabel('Appliance')
plt.ylabel('Cost (USD)')
plt.title('Monthly Cost of Energy (Electricity vs Solar)')
plt.xticks([i + bar_width / 2 for i in index], appliances, rotation=45)
plt.legend()

# Plot Line Graph
plt.subplot(1, 2, 2)
plt.plot(appliances, electricity_cost, label='Electricity', color='blue', marker='o')
plt.plot(appliances, solar_cost, label='Solar', color='green', marker='o')

plt.xlabel('Appliance')
plt.ylabel('Cost (USD)')
plt.title('Energy Cost Comparison (Electricity vs Solar)')
plt.legend()

# Adjust layout
plt.tight_layout()
plt.show()
