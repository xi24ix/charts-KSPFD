import matplotlib.pyplot as plt
import numpy as np

# Color theme
colors = ['#362D5F', '#FAF8FB', '#26214F', '#271F54', '#DED8EE']

# Data
children = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '9+']
divorced_women = [10281, 8206, 6652, 5144, 3617, 2119, 1222, 659, 337, 375]
widowed_women = [1383, 4188, 9129, 16416, 22370, 23586, 21182, 19272, 16533, 24966]

# Set the style
plt.style.use('ggplot')

# 1. Bar Chart: Number of Children by Divorced Women
plt.figure(figsize=(12, 6))
plt.bar(children, divorced_women, color=colors[0])
plt.title('Number of Children by Divorced Women', color=colors[2])
plt.xlabel('Number of Children', color=colors[2])
plt.ylabel('Number of Divorced Women', color=colors[2])
plt.xticks(children, color=colors[2])
plt.yticks(color=colors[2])
for i, v in enumerate(divorced_women):
    plt.text(i, v + 100, str(v), ha='center', color=colors[4])
plt.tight_layout()
plt.savefig('bar_chart.png')
plt.close()

# 2. Pie Chart: Distribution of Children Among Divorced Women
total = sum(divorced_women)
percentages = [count / total * 100 for count in divorced_women]
plt.figure(figsize=(10, 10))
plt.pie(percentages, labels=children, autopct='%1.1f%%', startangle=90, colors=colors)
plt.title('Distribution of Children Among Divorced Women', color=colors[2])
plt.axis('equal')
plt.tight_layout()
plt.savefig('pie_chart.png')
plt.close()

# 3. Line Chart: Cumulative Number of Children from Divorced Women
cumulative = np.cumsum([divorced_women[0]] + [divorced_women[i] * (i + 1) for i in range(1, len(divorced_women))])
plt.figure(figsize=(12, 6))
plt.plot(children, cumulative, marker='o', color=colors[0])
plt.title('Cumulative Number of Children from Divorced Women', color=colors[2])
plt.xlabel('Number of Children', color=colors[2])
plt.ylabel('Cumulative Number of Children', color=colors[2])
plt.xticks(children, color=colors[2])
plt.yticks(color=colors[2])
plt.grid(True, linestyle='--', alpha=0.7, color=colors[4])
for i, v in enumerate(cumulative):
    plt.text(i, v, f'{v:,}', ha='center', va='bottom', color=colors[3])
plt.tight_layout()
plt.savefig('line_chart.png')
plt.close()

# 4. Stacked Bar Chart: Comparison of Children from Divorced and Widowed Women
plt.figure(figsize=(12, 6))
plt.bar(children, divorced_women, label='Divorced Women', color=colors[0])
plt.bar(children, widowed_women, bottom=divorced_women, label='Widowed Women', color=colors[1])
plt.title('Comparison of Children from Divorced and Widowed Women', color=colors[2])
plt.xlabel('Number of Children', color=colors[2])
plt.ylabel('Number of Women', color=colors[2])
plt.xticks(children, color=colors[2])
plt.yticks(color=colors[2])
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('stacked_bar_chart.png')
plt.close()

# 5. Heatmap: Distribution of Children by Number of Divorced Women
plt.figure(figsize=(10, 6))
plt.imshow([divorced_women], cmap='YlOrRd')
plt.colorbar(label='Number of Divorced Women')
plt.title('Distribution of Children by Number of Divorced Women', color=colors[2])
plt.xlabel('Number of Children', color=colors[2])
plt.yticks([])
plt.xticks(range(len(children)), children, color=colors[2])
for i, v in enumerate(divorced_women):
    plt.text(i, 0, str(v), ha='center', va='center', color='black')
plt.tight_layout()
plt.savefig('heatmap.png')
plt.close()

# 6. Histogram: Frequency Distribution of Children Among Divorced Women
plt.figure(figsize=(12, 6))
plt.hist(np.repeat(range(1, 11), divorced_women), bins=10, range=(0.5, 10.5), color=colors[0], edgecolor='black')
plt.title('Frequency Distribution of Children Among Divorced Women', color=colors[2])
plt.xlabel('Number of Children', color=colors[2])
plt.ylabel('Frequency', color=colors[2])
plt.xticks(range(1, 11), children, color=colors[2])
plt.yticks(color=colors[2])
plt.tight_layout()
plt.savefig('histogram.png')
plt.close()

# 7. Box Plot: Distribution of Children Among Divorced Women
plt.figure(figsize=(10, 6))
plt.boxplot(np.repeat(range(1, 11), divorced_women), vert=False)
plt.title('Distribution of Children Among Divorced Women', color=colors[2])
plt.xlabel('Number of Children', color=colors[2])
plt.yticks([1], ['Divorced Women'], color=colors[2])
plt.xticks(range(1, 11), children, color=colors[2])
plt.tight_layout()
plt.savefig('box_plot.png')
plt.close()

print("All charts have been generated and saved as PNG files.")