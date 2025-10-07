# Data-Mining
Introduction to Data Mining Midterm Project
This project is the midterm assignment for the Introduction to Data Mining course of the Information Engineering major at Xidian University.
作业的要求如下
  1. 加载数据集，检查并报告各特征的数值缺失情况。然后，通过 Age = 2025-Year of manufacture 计算创建一个新的特征 Age（车龄），并移除原有的 Year of manufacture 列；
  2. 简要展示处理后数据集的总体信息（前五行）。计算所有数值型特征（包括Age）的描述性统计量（均值、中位数、标准差、最大/最小值等）。同时，统计并展示数据集中最常见的前 5 个汽车制造商（Manufacturer）及其数量；
  3. 使用直方图对 Price 的分布情况进行可视化展示，并简要描述其分布特点（例如，分布是左偏还是右偏？是否存在多个峰值）；
  4. 使用散点图探索 Age（车龄）与 Price 之间的关系，并简要分析观察到的趋势；
  5. 计算所有数值型特征（Engine size，Mileage，Price，Age）之间的相关系数，并使用热力图进行可视化呈现，指出哪两个特征与 Price 的相关性最强；
  6. 其他数据分析思路（可选）。
本次作业没有标准答案，鼓励尝试从不同的方向探索数据的相关性，以不同形式可视化展示数据，并进行结论分析。
数据说明：
  本数据集为一个模拟的二手车销售记录数据集，包含了 5 万条车辆的交易信息。分析本数据集的核心目标是探索影响二手车价格的关键因素。
  数据集包含以下 7 个特征：
    Manufacturer：汽车制造商（例如：Toyota，Ford）
    Model：车辆型号（例如：Camry，Focus）
    Engine size：发动机排量（单位：升）
    Fuel type：燃料类型（例如：Gasoline，Diesel）
    Year of manufacture：制造年份
    Mileage：行驶里程（单位：公里）
    Price：价格（单位：美元）
