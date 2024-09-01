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

# Stacked Bar Chart
plt.figure(figsize=(10, 6))
plt.bar(children_numbers, divorced_children, label='Divorced', color=colors["cardinal"])
plt.bar(children_numbers, widowed_children, bottom=divorced_children, label='Widowed', color=colors["russian_violet_1"])

plt.xlabel('Number of Children in Home')
plt.ylabel('Number of Children')
plt.title('Stacked Bar Chart: Children Living with One Parent (Divorced and Widowed)')
plt.legend()

plt.tight_layout()
plt.show()

# Histogram
plt.figure(figsize=(10, 6))
plt.hist([divorced_children, widowed_children], bins=range(1, 12), label=['Divorced', 'Widowed'], color=[colors["cardinal"], colors["russian_violet_1"]], rwidth=0.8)

plt.xlabel('Number of Children')
plt.ylabel('Frequency')
plt.title('Histogram: Frequency Distribution of Children Living with One Parent')
plt.legend()

plt.tight_layout()
plt.show()

# Heatmap
heatmap_data = np.array([divorced_children, widowed_children])
plt.figure(figsize=(10, 6))
plt.imshow(heatmap_data, cmap='coolwarm', aspect='auto')

plt.colorbar(label='Number of Children')
plt.xticks(ticks=np.arange(len(children_numbers)), labels=children_numbers)
plt.yticks(ticks=[0, 1], labels=['Divorced', 'Widowed'])
plt.xlabel('Number of Children in Home')
plt.ylabel('Parent Status')
plt.title('Heatmap: Density of Children Living with One Parent')

plt.tight_layout()
plt.show()

# Box Plot
plt.figure(figsize=(10, 6))
plt.boxplot([divorced_children, widowed_children], labels=['Divorced', 'Widowed'], patch_artist=True,
            boxprops=dict(facecolor=colors["cardinal"], color=colors["cardinal"]),
            medianprops=dict(color=colors["russian_violet_1"]),
            whiskerprops=dict(color=colors["cardinal"]),
            capprops=dict(color=colors["cardinal"]),
            flierprops=dict(markerfacecolor=colors["puce"], markeredgecolor=colors["puce"]))

plt.ylabel('Number of Children')
plt.title('Box Plot: Distribution of Children Living with One Parent')

plt.tight_layout()
plt.show()