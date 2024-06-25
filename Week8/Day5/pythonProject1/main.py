#Exercise 1: Data visualization is very important in being able to share the
# information with people who are otherwise unfamiliar with statistical
# language and helps percieve a sense of scale and change. A line graph is
# specifically meant to show change over time in the same continuous variable.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# #exercise 2
# week_temps = {
#     'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
#     'Temperature (F)': [72, 74, 76, 80, 82, 78, 75]}
# wt = pd.DataFrame(week_temps)
# plt.plot(wt['Day'], wt['Temperature (F)'], color='green', marker='o', linestyle='dashed', linewidth=2, markersize=12)
# plt.xlabel('Day')
# plt.ylabel('Temperature (F)')
# plt.title('Weekly Temperatures')
# plt.show()
#
# #exercise 3
# month_sales = {
#     "Month":["Jan", "Feb", "Mar", "Apr", "May"],
#     "Sales":[5000, 5500, 6200, 7000, 7500]}
# ms = pd.DataFrame(month_sales)
# plt.bar(ms['Month'], ms['Sales'], width=0.8, bottom=None, align='center')
# plt.show()

#exercise 4
sales_data = pd.read_csv("sales_data.csv")
print(sales_data['quantity'].sum())

sales_data = sales_data.dropna(subset=['revenue'])
category_revenue = sales_data.groupby('category')['revenue'].sum()
highest_revenue_category = category_revenue.idxmax()
highest_revenue = category_revenue.max()
print(category_revenue, highest_revenue_category, highest_revenue)

sales_data['date'] = pd.to_datetime(sales_data['date'])
sales_data['quarter'] = sales_data['date'].dt.to_period('Q')
quarter_revenue = sales_data.groupby('quarter')['revenue'].sum()
quarter_revenue.plot(kind='bar', color='b')
plt.title('Total Revenue Generated in Each Quarter')
plt.xlabel('Quarter')
plt.ylabel('Total Revenue')
plt.show()

#exercise 5
x = np.arange(-10, 11, 1)
y = x**2

plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y = x^2')
plt.title('Plot of y = x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

products = ['A', 'B', 'C', 'D']
sales = [15, 30, 45, 20]
plt.figure(figsize=(8, 6))
plt.bar(products, sales, color=['blue', 'orange', 'green', 'red'])
plt.title('Weekly Sales of Products')
plt.xlabel('Products')
plt.ylabel('Sales')
plt.show()

fruits = ['Apples', 'Bananas', 'Cherries', 'Dates']
percentages = [40, 30, 20, 10]
colors = ['red', 'yellow', 'pink', 'brown']
plt.figure(figsize=(8, 6))
plt.pie(percentages, labels=fruits, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Favorite Fruits')
plt.legend(fruits, loc="best")
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()