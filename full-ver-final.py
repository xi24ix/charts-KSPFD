import matplotlib.pyplot as plt
import numpy as np

# Data from the report
divorced_women = {
    '1 Child': 10281,
    '2 Children': 8206,
    '3 Children': 6652,
    '4 Children': 5144,
    '5 Children': 3617,
    '6 Children': 2119,
    '7 Children': 1222,
    '8 Children': 659,
    '9 Children': 337,
    '9+ Children': 375
}

# Calculate total number of children for each category
total_children_divorced = {
    '1 Child': 10281 * 1,
    '2 Children': 8206 * 2,
    '3 Children': 6652 * 3,
    '4 Children': 5144 * 4,
    '5 Children': 3617 * 5,
    '6 Children': 2119 * 6,
    '7 Children': 1222 * 7,
    '8 Children': 659 * 8,
    '9 Children': 337 * 9,
    '9+ Children': 375 * 11  # Assuming average 11 children for 9+
}

# Data for widowed women (for comparison)
widowed_women = {
    '1 Child': 1383,
    '2 Children': 2094,
    '3 Children': 3043,
    '4 Children': 4104,
    '5 Children': 4474,
    '6 Children': 3931,
    '7 Children': 3026,
    '8 Children': 2409,
    '9 Children': 1837,
    '9+ Children': 2774
}

# Calculate total number of children for each category for widowed women
total_children_widowed = {
    '1 Child': 1383 * 1,
    '2 Children': 2094 * 2,
    '3 Children': 3043 * 3,
    '4 Children': 4104 * 4,
    '5 Children': 4474 * 5,
    '6 Children': 3931 * 6,
    '7 Children': 3026 * 7,
    '8 Children': 2409 * 8,
    '9 Children': 1837 * 9,
 '9+ Children': 2774 * 11  # Assuming average 11 children for 9+
}

# Bar Chart: Number of Children by Divorced Women
plt.figure(figsize=(10, 6))
plt.bar(divorced_women.keys(), divorced_women.values(), color='blue')
plt.title('Number of Children by Divorced Women')
plt.xlabel('Number of Children')
plt.ylabel('Number of Divorced Women')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Pie Chart: Distribution of Children Among Divorced Women
plt.figure(figsize=(8, 8))
plt.pie(divorced_women.values(), labels=divorced_women.keys(), autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Children Among Divorced Women')
plt.show()

# Line Chart: Cumulative Number of Children from Divorced Women
cumulative_children = np.cumsum(list(total_children_divorced.values()))
plt.figure(figsize=(10, 6))
plt.plot(list(total_children_divorced.keys()), cumulative_children, marker='o', linestyle='-', color='green')
plt.title('Cumulative Number of Children from Divorced Women')
plt.xlabel('Number of Children')
plt.ylabel('Cumulative Number of Children')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Stacked Bar Chart: Comparison of Children from Divorced and Widowed Women
labels = list(divorced_women.keys())
divorced_values = list(total_children_divorced.values())
widowed_values = list(total_children_widowed.values())

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize=(12, 8))
rects1 = ax.bar(x - width/2, divorced_values, width, label='Divorced')
rects2 = ax.bar(x + width/2, widowed_values, width, label='Widowed')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Number of Children')
ax.set_ylabel('Total Number of Children')
ax.set_title('Comparison of Children from Divorced and Widowed Women')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

fig.tight_layout()
plt.xticks(rotation=45)
plt.show()

# Heatmap: Distribution of Children by Number of Divorced Women
plt.figure(figsize=(10, 6))
heatmap_data = np.array(list(divorced_women.values())).reshape(1, -1)
plt.imshow(heatmap_data, cmap='hot', interpolation='nearest', aspect='auto')
plt.colorbar()
plt.title('Heatmap: Distribution of Children by Number of Divorced Women')
plt.xlabel('Number of Children')
plt.ylabel('Divorced Women')
plt.xticks(ticks=np.arange(len(labels)), labels=labels, rotation=45)
plt.yticks([])
plt.tight_layout()
plt.show()

# Histogram: Frequency Distribution of Children Among Divorced Women
plt.figure(figsize=(10, 6))
plt.hist(list(divorced_women.values()), bins=len(divorced_women), color='purple', edgecolor='black')
plt.title('Frequency Distribution of Children Among Divorced Women')
plt.xlabel('Number of Divorced Women')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Box Plot: Distribution of Children Among Divorced Women
plt.figure(figsize=(10, 6))
plt.boxplot(list(divorced_women.values()), vert=False)
plt.title('Box Plot: Distribution of Children Among Divorced Women')
plt.xlabel('Number of Divorced Women')
plt.tight_layout()
plt.show()