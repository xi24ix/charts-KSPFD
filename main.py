import matplotlib.pyplot as plt
import numpy as np

# Data for Bar Chart
children = ['طفل واحد', 'طفلين', 'ثلاثة أطفال', 'أربعة أطفال', 'خمسة أطفال', 'ستة أطفال', 'سبعة أطفال', 'ثمانية أطفال', 'تسعة أطفال', '9+ أطفال']
divorced_women = [10281, 8206, 6652, 5144, 3617, 2119, 1222, 659, 337, 375]

# Bar Chart
plt.figure(figsize=(10, 6))
plt.bar(children, divorced_women, color='skyblue')
plt.xlabel('عدد الأطفال', fontsize=14)
plt.ylabel('عدد النساء المطلقات', fontsize=14)
plt.title('عدد الأطفال حسب النساء المطلقات', fontsize=16)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Data for Pie Chart
total_divorced_women = sum(divorced_women)
percentages = [(num / total_divorced_women) * 100 for num in divorced_women]

# Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(percentages, labels=children, autopct='%1.1f%%', startangle=140)
plt.title('توزيع الأطفال بين النساء المطلقات', fontsize=16)
plt.axis('equal')
plt.show()

# Data for Line Chart
cumulative_children = np.cumsum([num * (i + 1) for i, num in enumerate(divorced_women)])

# Line Chart
plt.figure(figsize=(10, 6))
plt.plot(children, cumulative_children, marker='o', color='orange')
plt.xlabel('عدد الأطفال', fontsize=14)
plt.ylabel('عدد الأطفال التراكمي', fontsize=14)
plt.title('عدد الأطفال التراكمي من النساء المطلقات', fontsize=16)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Data for Stacked Bar Chart
widowed_women = [1383, 4188, 9129, 16416, 22370, 23586, 21182, 19272, 16533, 24966]

# Stacked Bar Chart
plt.figure(figsize=(10, 6))
bar_width = 0.35
index = np.arange(len(children))

plt.bar(index, divorced_women, bar_width, label='نساء مطلقات', color='skyblue')
plt.bar(index, widowed_women, bar_width, bottom=divorced_women, label='نساء أرامل', color='salmon')
plt.xlabel('عدد الأطفال', fontsize=14)
plt.ylabel('عدد النساء', fontsize=14)
plt.title('مقارنة عدد الأطفال بين النساء المطلقات والأرامل', fontsize=16)
plt.xticks(index, children, rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
