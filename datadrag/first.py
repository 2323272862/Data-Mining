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

# 第一问 加载数据集
df = pd.read_csv("car_sales_data.csv")

# 检查各特征的数值缺失情况
missing_values = df.isnull().sum()
missing_percentage = (missing_values / len(df)) * 100
missing_info = pd.DataFrame({
    '缺失值数量': missing_values,
    '缺失比例(%)': missing_percentage.round(2)
})
print("各特征数值缺失情况：")
print(missing_info)

# 创建新特征Age（车龄），公式为Age = 2025 - Year of manufacture
df['Age'] = 2025 - df['Year of manufacture']

# 移除原有的Year of manufacture列
df = df.drop('Year of manufacture', axis=1)

print("\n数据加载与预处理完成，新增车龄特征并移除制造年份列！")

# 恢复原始的stdout
sys.stdout = original_stdout
# 获取缓冲区中的内容
output_content = output_buffer.getvalue()
# 写入到文件
output_file.write(output_content)
# 关闭文件
output_file.close()

print(f"\n终端输出已保存到answer.txt文件中")