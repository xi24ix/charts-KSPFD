import matplotlib.pyplot as plt
import numpy as np

# Data from the provided snippets
children_numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
divorced_children = np.array([10281, 8206, 6652, 5144, 3617, 2119, 1222, 659, 337, 375])
widowed_children = np.array([1383, 2094, 3043, 4104, 4474, 3931, 3026, 2409, 1837, 2774])

# Color theme
colors = {
    "cardinal": "#AF333E",
    "russian_violet_1": "#402C57",
    "puce": "#D39197",
    "russian_violet_2": "#3B2552",
    "slate_blue": "#6161AB"
}

# Bar chart for children living with divorced and widowed parents
plt.figure(figsize=(10, 6))
bar_width = 0.35
index = np.arange(len(children_numbers))

plt.bar(index, divorced_children, bar_width, label='Divorced', color=colors["cardinal"])
plt.bar(index + bar_width, widowed_children, bar_width, label='Widowed', color=colors["russian_violet_1"])

plt.xlabel('Number of Children in Home')
plt.ylabel('Number of Children')
plt.title('Children Living with One Parent (Divorced and Widowed)')
plt.xticks(index + bar_width / 2, children_numbers)
plt.legend()

plt.tight_layout()
plt.show()

# Pie chart for the proportion of children living with divorced vs widowed parents
total_divorced = np.sum(divorced_children)
total_widowed = np.sum(widowed_children)
sizes = [total_divorced, total_widowed]
labels = ['Divorced', 'Widowed']
colors_pie = [colors["cardinal"], colors["russian_violet_1"]]

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors_pie, autopct='%1.1f%%', startangle=140)
plt.title('Proportion of Children Living with Divorced vs Widowed Parents')
plt.axis('equal')

plt.show()

# Line chart for trend of children living with divorced and widowed parents
plt.figure(figsize=(10, 6))
plt.plot(children_numbers, divorced_children, marker='o', color=colors["cardinal"], label='Divorced')
plt.plot(children_numbers, widowed_children, marker='o', color=colors["russian_violet_1"], label='Widowed')

plt.xlabel('Number of Children in Home')
plt.ylabel('Number of Children')
plt.title('Trend of Children Living with One Parent (Divorced and Widowed)')
plt.legend()

plt.tight_layout()
plt.show()