# 银行客户画像分析

这是我的第一个金融数据练习。用 Python 和 pandas 将 Kaggle 的银行客户数据导入 SQLite，再用 SQL 练习条件筛选、分组和汇总。

[打开 Jupyter Notebook](bank_churn_analysis.ipynb) · **状态：进行中，已完成国家和产品数的样本流失率对比。**

## 已完成

使用 `Customer-Churn-Records.csv` 中的 10,000 条客户记录，完成了三个查询。

| 查询 | 样本结果 |
| --- | --- |
| 年龄大于 40 岁的女性客户 | 1,704 人 |
| 按国家计算平均信用分 | 法国 649.67，德国 651.45，西班牙 651.33 |
| 余额大于 100,000，且使用产品不超过 2 个的客户 | 4,631 人 |

这些结果描述的是样本。平均信用分接近只说明均值接近。筛选人数用于回答有多少客户符合条件。判断信用风险、活跃度或营销需求需要相应的指标。

## 样本流失分析

- 按国家分组后，德国的样本流失率为 **32.44%**（814 / 2,509），西班牙为 **16.67%**（413 / 2,477），法国为 **16.17%**（811 / 5,014）。德国和法国的流失人数接近，客户总人数差异解释了两组比例的差距。
- 在产品数分组中，持有 4 个产品的客户有 **60** 人，60 人均流失，样本流失率为 **100%**。这个组的样本量比持有 1 个或 2 个产品的组小得多。仅凭这组统计无法确定产品数是否导致流失。
- 两种分组都用 SQLite 计算，再用 pandas 逐值核对。各组客户数分别加总为 **10,000**。

## 本地运行

1. 从 [Kaggle Bank Customer Churn](https://www.kaggle.com/datasets/radheshyamkollipara/bank-customer-churn) 下载 `Customer-Churn-Records.csv`，放进仓库根目录的 `data/`。
2. 在仓库根目录安装依赖并启动 JupyterLab。本次用 Python 3.13 验证。

   ```bash
   python -m pip install -r requirements.txt
   python -m jupyterlab
   ```

3. 打开 `bank_churn_analysis.ipynb`，选择 Python 3 内核，从上到下运行。Notebook 使用内存 SQLite，打开 GitHub 页面也可以预览已保存的汇总结果。

需要使用原有命令行流程时，可运行：

   ```bash
   python scripts/import_bank_data.py
   python scripts/query_bank.py
   ```

第一份脚本在本地生成 `my_first_bank.db` 并加载 `Bank_Churn` 表。再次运行导入会替换该表。第二份脚本读取数据库，并打印三项查询的汇总结果。原始 CSV 和本地数据库由 Git 忽略。

## 项目文件

| 文件 | 用途 |
| --- | --- |
| [bank_churn_analysis.ipynb](bank_churn_analysis.ipynb) | 数据检查、客户画像、两种流失率分组及 pandas 核对 |
| [scripts/import_bank_data.py](scripts/import_bank_data.py) | 读取 CSV 并导入 SQLite |
| [scripts/query_bank.py](scripts/query_bank.py) | 运行原有的三项查询 |
| [requirements.txt](requirements.txt) | pandas 和 JupyterLab 依赖 |

## 下一步

下一步复习样本量与因果结论的区别，再尝试用图表同时展示每组流失率和客户人数。
