import pandas as pd                               
import numpy as np                                
import matplotlib.pyplot as plt                  
import seaborn as sns                              
import sys
import io

# 设置中文字体，避免图表中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']            # 指定字体为黑体
plt.rcParams['axes.unicode_minus'] = False              # 确保坐标轴上的负号正常显示

# 创建answer.txt文件，用于保存终端输出
output_file = open('answer.txt', 'w', encoding='utf-8')
original_stdout = sys.stdout
output_buffer = io.StringIO()
sys.stdout = output_buffer

# 第一问 加载数据集
df = pd.read_csv("car_sales_data.csv")                  # 读取数据集

# 检查各特征的数值缺失情况
missing_values = df.isnull().sum()                      # 计算每一列的缺失值数量
missing_percentage = (missing_values / len(df)) * 100   # 计算每列缺失值占总体行数的百分比
missing_info = pd.DataFrame({                           
    '缺失值数量': missing_values,
    '缺失比例(%)': missing_percentage.round(2)          # 对缺失百分比进行四舍五入到小数点后2位
})
print("各特征数值缺失情况：")                             
print(missing_info)                                     

# 创建新特征Age，Age = 2025 - Year of manufacture
df['Age'] = 2025 - df['Year of manufacture']            

# 移除原有的Year of manufacture列
df = df.drop('Year of manufacture', axis=1)             



# 第二问
print("处理后数据集的前五行：")  #展示处理后数据集的总体信息（前五行）
print(df.head())

# 计算所有数值型特征的描述性统计量
numeric_features = ['Engine size', 'Mileage', 'Price', 'Age']  
descriptive_stats = df[numeric_features].describe()

# 将描述性统计量的英文表头替换为中文
descriptive_stats.columns = descriptive_stats.columns
chinese_labels = {
    'count': '计数',
    'mean': '均值',
    'std': '标准差', 
    'min': '最小值',
    '25%': '25%',
    '50%': '中位数',
    '75%': '75%',
    'max': '最大值'
}
descriptive_stats_zh = descriptive_stats.rename(index=chinese_labels)

print("\n所有数值型特征的描述性统计量：")
print(descriptive_stats_zh.round(2))

# 统计数据集中最常见的前5个汽车制造商及其数量
top5_manufacturers = df['Manufacturer'].value_counts().head(5)
print("\n最常见的前5个汽车制造商及其数量：")
print(top5_manufacturers)

# 可视化前5个常见汽车制造商的数量
plt.figure(figsize=(10, 6))
ax = top5_manufacturers.plot(kind='bar', color='skyblue')
plt.title('最常见的前5个汽车制造商及其数量', fontsize=14)
plt.xlabel('汽车制造商', fontsize=12)
plt.ylabel('车辆数量', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width() / 2., height + 5, 
           f'{int(height)}', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.savefig('top5_manufacturers.png', dpi=300)
plt.show()

# 将终端输出保存到answer.txt文件中
sys.stdout = original_stdout
output_content = output_buffer.getvalue()
output_file.write(output_content)
output_file.close()

print(f"\n终端输出已保存到answer.txt文件中")

# 第三问使用直方图对 Price 的分布情况进行可视化展示
plt.figure(figsize=(12, 6))
counts, bins, patches = plt.hist(df['Price'], bins=30, alpha=0.7, color='skyblue', edgecolor='black')
plt.title('汽车价格分布直方图', fontsize=16)
plt.xlabel('价格', fontsize=14)
plt.ylabel('频率', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)

for count, patch, bin_edge in zip(counts, patches, bins):
    if count > 0:  
        plt.text(bin_edge + (bins[1] - bins[0])/2, count, int(count),
                 ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.savefig('price_distribution.png', dpi=300)
plt.show()

#第四问 使用散点图探索 Age（车龄）与 Price 之间的关系
plt.figure(figsize=(10, 6))
plt.scatter(df['Age'], df['Price'], alpha=0.5, color='purple')
plt.title('车龄与价格关系散点图', fontsize=16)
plt.xlabel('车龄（年）', fontsize=14)
plt.ylabel('价格', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('age_price_scatter.png', dpi=300)
plt.show()

# 第五问计算spearman相关系数并且进行热力图呈现
import seaborn as sns
import numpy as np

numeric_features = ['Engine size', 'Mileage', 'Price', 'Age']
numeric_df = df[numeric_features]

corr_matrix = numeric_df.corr(method='spearman')

# 在终端输出相关系数
print("\n===== 数值型特征Spearman相关系数 =====")
print(corr_matrix.round(4))

# 将相关系数保存到spearman.txt文件中
with open('spearman.txt', 'w', encoding='utf-8') as f:
    f.write("===== 数值型特征Spearman相关系数 =====\n")
    f.write(f"{corr_matrix.round(4)}")

# 绘制热力图
plt.figure(figsize=(10, 8))
heatmap = sns.heatmap(corr_matrix, annot=True, cmap='YlOrRd', vmin=-1, vmax=1, 
                      linewidths=0.5, linecolor='white', fmt='.2f')
plt.title('数值型特征Spearman相关系数热力图', fontsize=16)
plt.tight_layout()
plt.savefig('correlation_heatmap.png', dpi=300)
plt.show()

#  第六问：燃料类型对价格的差异化影响分析 

sixth_buffer = io.StringIO()
sixth_saved_stdout = sys.stdout
sys.stdout = sixth_buffer

# 检查所需列是否存在
if 'Fuel type' not in df.columns or 'Price' not in df.columns:
    print("\n跳过第六问：数据中缺少 'Fuel type' 或 'Price' 列，无法进行燃料类型分析。")
else:
    # 统计不同燃料类型的车辆数量与占比
    fuel_counts = df['Fuel type'].value_counts(dropna=False)
    fuel_props = (fuel_counts / fuel_counts.sum()) * 100

    print("\n=== 燃料类型车辆数量 ===")
    print(fuel_counts)
    print("\n=== 燃料类型占比 (%) ===")
    print(fuel_props.round(2))

    # 绘制饼图展示燃料类型占比
    import seaborn as sns

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

    for at in autotexts:
        at.set_fontsize(13)
        at.set_color('black')

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
    sys.stdout = sixth_saved_stdout
    sixth_output = sixth_buffer.getvalue()
    with open('answer.txt', 'a', encoding='utf-8') as f:
        f.write('\n')
        f.write(sixth_output)

    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

    price_stats = df.groupby('Fuel type')['Price'].describe()
    print("\n=== 按燃料类型分组的价格描述性统计（部分） ===")
    if '50%' in price_stats.columns:
        display_stats = price_stats[['count', 'mean', '50%', 'std']].rename(columns={'50%': 'median'})
    else:
        display_stats = price_stats[['count', 'mean', 'std']]
    print(display_stats.round(2))

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
    plt.savefig('price_by_fuel_boxplot.png', dpi=300)
    print("已保存箱线图：price_by_fuel_boxplot.png")
    plt.show()
    plt.close()
sys.stdout = original_stdout
print("分析完成，结果已保存到 answer.txt。")