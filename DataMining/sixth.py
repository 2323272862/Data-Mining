import pandas as pd  
import matplotlib.pyplot as plt  
import seaborn as sns  
import sys
import io
from datetime import datetime

# 设置中文字体，避免图表中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 创建answer6.txt文件，用于保存终端输出
output_file = open('answer6.txt', 'w', encoding='utf-8')
original_stdout = sys.stdout
output_buffer = io.StringIO()
sys.stdout = output_buffer

csv_path = 'car_sales_data.csv'

# 加载数据集并进行预处理
df = pd.read_csv("car_sales_data.csv")
df['Age'] = 2025 - df['Year of manufacture']
df = df.drop('Year of manufacture', axis=1)


# 统计不同燃料类型的车辆数量与占比
fuel_counts = df['Fuel type'].value_counts(dropna=False)
fuel_props = (fuel_counts / fuel_counts.sum()) * 100

print("\n=== 燃料类型车辆数量 ===")
print(fuel_counts)
print("\n=== 燃料类型占比 (%) ===")
print(fuel_props.round(2))

# 绘制饼图展示燃料类型占比
plt.figure(figsize=(8, 8))
labels = [str(i) if pd.notna(i) else 'Unknown' for i in fuel_counts.index]
sizes = fuel_counts.values
colors = sns.color_palette('pastel', len(fuel_counts))

fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=None,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    pctdistance=0.75,  
    labeldistance=1.05,
    wedgeprops={'linewidth': 0.8, 'edgecolor': 'white'}
)

# 增大百分比文本字号并设置颜色
for at in autotexts:
    at.set_fontsize(13)
    at.set_color('black')

# 使用图例显示标签
ax.legend(wedges, labels, title='Fuel type', loc='center left', bbox_to_anchor=(1, 0, 0.4, 1), fontsize=12, title_fontsize=13)

ax.set_title('燃料类型车辆数量占比', fontsize=16)
ax.axis('equal')  
plt.tight_layout()
try:
    fig.savefig('fuel_type_pie.png', dpi=300, bbox_inches='tight')
    print("已保存饼图：fuel_type_pie.png")
except Exception as e:
    print(f"保存饼图时出错：{e}")
plt.show()
plt.close()
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

# 打印每类燃料的价格描述性统计量
price_stats = df.groupby('Fuel type')['Price'].describe()
print("\n=== 按燃料类型分组的价格描述性统计（部分） ===")
print(price_stats[['count', 'mean', '50%', 'std']].rename(columns={'50%': 'median'}).round(2))

# 绘制箱线图对比不同燃料类型的价格分布
plt.figure(figsize=(10, 6))
order = fuel_counts.index.tolist()
sns.boxplot(x='Fuel type', y='Price', data=df, order=order, palette='Set3')
plt.title('不同燃料类型的价格分布（箱线图）', fontsize=14)
plt.xlabel('燃料类型', fontsize=12)
plt.ylabel('价格', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
try:
    plt.savefig('price_by_fuel_boxplot.png', dpi=300)
    print("已保存箱线图：price_by_fuel_boxplot.png")
except Exception as e:
    print(f"保存箱线图时出错：{e}")
plt.show()
plt.close()

# 恢复 stdout 并写入捕获到的输出
sys.stdout = original_stdout
output_content = output_buffer.getvalue()
output_file.write(output_content)
output_file.close()

print("分析完成，结果已保存到 answer6.txt。")
