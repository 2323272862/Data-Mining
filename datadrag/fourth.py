import pandas as pd
import matplotlib.pyplot as plt
import sys
import io

# 设置中文字体，避免图表中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 创建answer.txt文件，用于保存终端输出
output_file = open('answer.txt', 'w', encoding='utf-8')
# 保存原始的stdout
original_stdout = sys.stdout
# 创建一个字符串IO对象来捕获输出
output_buffer = io.StringIO()
# 将stdout重定向到缓冲区
sys.stdout = output_buffer

# 加载数据集
df = pd.read_csv("car_sales_data.csv")

# 创建新特征Age（车龄）
df['Age'] = 2025 - df['Year of manufacture']

# 移除原有的Year of manufacture列
df = df.drop('Year of manufacture', axis=1)

# 第四问 使用散点图探索 Age（车龄）与 Price 之间的关系
plt.figure(figsize=(10, 6))
plt.scatter(df['Age'], df['Price'], alpha=0.5, color='purple')
plt.title('车龄与价格关系散点图', fontsize=16)
plt.xlabel('车龄（年）', fontsize=14)
plt.ylabel('价格', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('age_price_scatter.png', dpi=300)
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