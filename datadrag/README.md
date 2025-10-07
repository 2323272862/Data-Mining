# 汽车销售数据分析项目

## 项目概述

本项目基于汽车销售数据集，进行了数据加载、预处理、统计分析和可视化展示，旨在探索汽车销售数据中的各项特征关系和分布规律。项目包含五个主要分析任务，已拆分为独立的Python文件，方便单独运行和理解。

## 目录结构

```
├── first.py          # 第一问：数据加载与预处理
├── second.py         # 第二问：数据集总体信息展示与基本统计分析
├── third.py          # 第三问：价格分布直方图可视化
├── fourth.py         # 第四问：车龄与价格关系散点图分析
├── fifth.py          # 第五问：相关系数计算与热力图呈现
├── firstquestion.py  # 原始完整代码文件
├── car_sales_data.csv # 数据集文件
├── requirements.txt  # 项目依赖库列表
└── README.md         # 项目说明文档
```

## 环境要求

运行本项目需要安装以下Python库：
- pandas
- matplotlib
- seaborn
- numpy

可以使用以下命令安装所有依赖：
```bash
pip install -r requirements.txt
```

## 如何运行

1. 确保已安装所有必要的依赖库
2. 确保`car_sales_data.csv`文件与Python文件在同一目录下
3. 单独运行每个Python文件,或者直接运行总文件firstquestion.py：

若直接运行总文件
```bash
python firstquestion.py
```
若单独运行每个Python文件
```bash
# 运行第一问
python first.py
```
```bash
# 运行第二问
python second.py
```
```bash
# 运行第三问
python third.py
```
```bash
# 运行第四问
python fourth.py
```
```bash
# 运行第五问
python fifth.py
```

## 项目功能说明

### 第一问（first.py）
- 加载汽车销售数据集
- 检查各特征的数值缺失情况
- 创建新特征Age（车龄）：Age = 2025 - Year of manufacture
- 移除原有的Year of manufacture列
- 输出预处理结果到answer.txt文件

### 第二问（second.py）
- 展示处理后数据集的前五行
- 计算所有数值型特征（Engine size, Mileage, Price, Age）的描述性统计量
- 统计并展示最常见的前5个汽车制造商及其数量
- 可视化前5个常见汽车制造商的数量柱状图，并保存为top5_manufacturers.png

### 第三问（third.py）
- 使用直方图对汽车价格分布情况进行可视化展示
- 在直方图上标注每个区间的具体数量
- 保存图表为price_distribution.png

### 第四问（fourth.py）
- 使用散点图探索车龄（Age）与价格（Price）之间的关系
- 保存散点图为age_price_scatter.png

### 第五问（fifth.py）
- 计算数值型特征（Engine size, Mileage, Price, Age）之间的Spearman相关系数
- 在终端输出相关系数矩阵
- 将相关系数保存到spearman.txt文件
- 使用热力图可视化相关系数矩阵，颜色方案为从橙到红
- 保存热力图为correlation_heatmap.png

## 输出文件

运行代码后，会生成以下输出文件：
- `answer.txt`：包含各问的终端输出结果
- `top5_manufacturers.png`：前5个汽车制造商数量柱状图
- `price_distribution.png`：汽车价格分布直方图
- `age_price_scatter.png`：车龄与价格关系散点图
- `correlation_heatmap.png`：相关系数热力图
- `spearman.txt`：Spearman相关系数矩阵

## 注意事项
1. 确保你的Python环境中已安装中文字体支持，以避免图表中文显示乱码
2. 代码中使用了2025作为基准年来计算车龄，根据实际需求可能需要调整
3. 所有图表都设置了适当的标题、坐标轴标签和网格线，以提高可读性
4. 相关系数热力图使用了从橙到红的颜色方案，便于观察相关性强弱

## License

本项目为学习目的创建，可自由使用和修改。
