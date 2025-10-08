import pandas as pd
import matplotlib.pyplot as plt
import sys
import io

# 设置中文字体，避免图表中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 创建answer1.txt文件，用于保存终端输出
output_file = open('answer1.txt', 'w', encoding='utf-8')
original_stdout = sys.stdout
output_buffer = io.StringIO()
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

#将终端输出保存到answer1.txt文件中
sys.stdout = original_stdout
output_content = output_buffer.getvalue()
output_file.write(output_content)
output_file.close()

print(f"\n终端输出已保存到answer1.txt文件中")