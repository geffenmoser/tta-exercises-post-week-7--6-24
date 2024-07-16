import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

temperatures = np.random.uniform(-5, 35, size=(10, 12))

cities = ['Jerusalem', 'NY', 'Madrid', 'Mexico City', 'Rome', 'Dubai', 'Beijing', 'Sydney', 'Capetown', 'Amsterdam']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
df = pd.DataFrame(temperatures, index=cities, columns=months)
print(df)

annual_avg_temp = df.mean(axis=1)
print(annual_avg_temp)

highest_temp_city = annual_avg_temp.idxmax()
lowest_temp_city = annual_avg_temp.idxmin()

print("City with highest average temperature:", highest_temp_city)
print("City with lowest average temperature:", lowest_temp_city)

for city in df.index:
    plt.plot(df.columns, df.loc[city], label=city)

plt.xlabel('Month')
plt.ylabel('Average Temperature (°C)')
plt.title('Monthly Average Temperatures for 10 Cities')
plt.legend()
plt.grid(True)
plt.show()
