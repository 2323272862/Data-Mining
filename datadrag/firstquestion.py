import pandas as pd                               # 导入 pandas，常用别名 pd，用于数据读取与处理
import numpy as np                                # 导入 numpy（别名 np），用于数值计算；本脚本中未使用到
import matplotlib.pyplot as plt                   # 导入 matplotlib.pyplot（别名 plt），用于绘图/配置图形
import seaborn as sns                              # 导入 seaborn（别名 sns），用于更高级的可视化（本脚本未使用具体函数）
import sys
import io

# 设置中文字体，避免图表中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']  # 配置无衬线字体为“SimHei”（若系统无该字体则会回退到默认）
plt.rcParams['axes.unicode_minus'] = False              # 确保坐标轴上的负号正常显示（防止被字体替换成方块）

# 创建answer.txt文件，用于保存终端输出
output_file = open('answer.txt', 'w', encoding='utf-8')
# 保存原始的stdout
original_stdout = sys.stdout
# 创建一个字符串IO对象来捕获输出
output_buffer = io.StringIO()
# 将stdout重定向到缓冲区
sys.stdout = output_buffer

# 第一问 加载数据集
df = pd.read_csv("car_sales_data.csv")                  # 从当前工作目录读取名为 car_sales_data.csv 的 CSV 文件为 DataFrame df

# 检查各特征的数值缺失情况
missing_values = df.isnull().sum()                      # 计算每一列的缺失值数量（NaN 的个数）
missing_percentage = (missing_values / len(df)) * 100   # 计算每列缺失值占总体行数的百分比
missing_info = pd.DataFrame({                            # 将缺失数量和缺失百分比组成一个新的 DataFrame，便于显示
    '缺失值数量': missing_values,
    '缺失比例(%)': missing_percentage.round(2)          # 对缺失百分比进行四舍五入到小数点后2位
})
print("各特征数值缺失情况：")                             # 打印标题
print(missing_info)                                      # 打印缺失信息表（每列的缺失数量与比例）

# 创建新特征Age（车龄），公式为Age = 2025 - Year of manufacture
df['Age'] = 2025 - df['Year of manufacture']            # 新增列 'Age'，用固定年份 2025 减去制造年份得到车龄（注意：硬编码当前年份）

# 移除原有的Year of manufacture列
df = df.drop('Year of manufacture', axis=1)             # 删除名为 'Year of manufacture' 的列；axis=1 表示按列删除

print("\n数据加载与预处理完成，新增车龄特征并移除制造年份列！")  # 打印处理完成提示

# 第二问展示处理后数据集的总体信息（前五行）
print("处理后数据集的前五行：")
print(df.head())

# 计算所有数值型特征（Engine size, Mileage, Price, Age）的描述性统计量
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
# 获取绘图对象的Axes实例
ax = top5_manufacturers.plot(kind='bar', color='skyblue')
plt.title('最常见的前5个汽车制造商及其数量', fontsize=14)
plt.xlabel('汽车制造商', fontsize=12)
plt.ylabel('车辆数量', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 在每个柱状上添加具体数值标签
for p in ax.patches:
    # 获取柱状的高度（即数值）
    height = p.get_height()
    # 在柱状上方添加文本标签，显示具体数值
    ax.text(p.get_x() + p.get_width() / 2., height + 5, 
           f'{int(height)}', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.savefig('top5_manufacturers.png', dpi=300)
plt.show()

# 恢复原始的stdout
sys.stdout = original_stdout
# 获取缓冲区中的内容
output_content = output_buffer.getvalue()
# 写入到文件
output_file.write(output_content)
# 关闭文件
output_file.close()

print(f"\n终端输出已保存到answer.txt文件中")

# 第三问使用直方图对 Price 的分布情况进行可视化展示
plt.figure(figsize=(12, 6))
counts, bins, patches = plt.hist(df['Price'], bins=30, alpha=0.7, color='skyblue', edgecolor='black')
plt.title('汽车价格分布直方图', fontsize=16)
plt.xlabel('价格', fontsize=14)
plt.ylabel('频率', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 在每个柱状上标明具体的数量
for count, patch, bin_edge in zip(counts, patches, bins):
    if count > 0:  # 只在有数据的柱状上显示标签
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

# 第五问计算相关系数并且进行热力图呈现
import seaborn as sns
import numpy as np

# 选择数值型特征
numeric_features = ['Engine size', 'Mileage', 'Price', 'Age']
numeric_df = df[numeric_features]

# 计算spearman相关系数
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
