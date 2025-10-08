# 汽车销售数据分析项目


## 目录结构（主要文件）

```
├── first.py                # 第一问：数据加载与预处理
├── second.py               # 第二问：数据集总体信息展示与基本统计分析
├── third.py                # 第三问：价格分布直方图可视化
├── fourth.py               # 第四问：车龄与价格关系散点图分析
├── fifth.py                # 第五问：相关系数计算与热力图呈现
├── sixth.py                # 第六问：燃料类型对价格影响（饼图 + 箱线图）
├── question.py             # 整合版完整代码文件
├── car_sales_data.csv      # 数据集文件
├── requirements.txt        # 项目依赖库列表
└── README.md               # 项目说明文档
```

## 环境要求



> 创建并激活虚拟环境示例：
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
运行本项目需要安装以下 Python 库：
- pandas
- matplotlib
- seaborn
- numpy
可使用如下命令完成
```bash
pip install -r requirements.txt
```

## 如何运行

1. 确保已安装所有必要的依赖库
2. 确保`car_sales_data.csv`文件与Python文件在同一目录下
3. 单独运行每个Python文件：

```bash
# 运行第一问
python first.py

# 运行第二问
python second.py

# 运行第三问
python third.py

# 运行第四问
python fourth.py

# 运行第五问
python fifth.py

# 运行第六问
python sixth.py
```

或者运行 `question.py`,直接运行整合版代码

```bash
python question.py
```

## 项目功能说明

### 第一问（first.py）
- 加载汽车销售数据集，检查各特征的数值缺失情况
- 创建新特征Age（车龄）：Age = 2025 - Year of manufacture
- 移除原有的Year of manufacture列
- 输出处理结果到answer1.txt文件

### 第二问（second.py）
- 展示处理后数据集的前五行和描述性统计量
- 统计并展示最常见的前 5 个汽车制造商及其数量
- 可视化前 5 个常见汽车制造商的数量柱状图，并保存为 `top5_manufacturers.png`
- 输出处理结果到answer2.txt文件

### 第三问（third.py）
- 使用直方图对汽车价格分布情况进行可视化展示
- 保存图表为 `price_distribution.png`

### 第四问（fourth.py）
- 使用散点图探索车龄（Age）与价格（Price）之间的关系
- 保存散点图为 `age_price_scatter.png`

### 第五问（fifth.py）
- 计算数值型特征（Engine size, Mileage, Price, Age）之间的 Spearman 相关系数
- 在终端输出相关系数矩阵并保存到 `spearman.txt`
- 使用热力图可视化相关系数矩阵并保存为 `correlation_heatmap.png`

### 第六问（sixth.py） — 燃料类型对价格的差异化影响
- 统计并打印不同燃料类型（`Fuel type`）的车辆数量与占比（%）
- 绘制燃料类型占比的饼图，并将百分比文本字体放大、标签通过图例显示以提高可读性；保存为 `fuel_type_pie.png`
- 绘制按燃料类型的价格箱线图以比较分布差异，保存为 `price_by_fuel_boxplot.png`


## 输出文件

运行代码后，输出文件如下：
- `answer.txt`：运行'question.py'文件后，终端输出捕获并写入该文件
- `answer1.txt`：`first.py` 的终端输出保存文件
- `answer2.txt`：`second.py` 的终端输出保存文件
- `answer6.txt`：`sixth.py` 的终端输出保存文件
- `top5_manufacturers.png`：前 5 个汽车制造商数量柱状图
- `price_distribution.png`：汽车价格分布直方图
- `age_price_scatter.png`：车龄与价格关系散点图
- `correlation_heatmap.png`：相关系数热力图
- `spearman.txt`：Spearman 相关系数矩阵
- `fuel_type_pie.png`：燃料类型占比饼图
- `price_by_fuel_boxplot.png`：按燃料类型的价格箱线图


