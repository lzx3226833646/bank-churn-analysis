# 银行客户画像分析

这是我的第一个金融数据练习。用 Python 和 pandas 将 Kaggle 的银行客户数据导入 SQLite，再用 SQL 练习条件筛选、分组和汇总。

## 已完成

使用 `Customer-Churn-Records.csv` 中的 10,000 条客户记录，完成了三个查询。

| 查询 | 样本结果 |
| --- | --- |
| 年龄大于 40 岁的女性客户 | 1,704 人 |
| 按国家计算平均信用分 | 法国 649.67，德国 651.45，西班牙 651.33 |
| 余额大于 100,000，且使用产品不超过 2 个的客户 | 4,631 人 |

这些结果描述的是样本。平均信用分接近只说明均值接近。筛选人数用于回答有多少客户符合条件。判断信用风险、活跃度或营销需求需要相应的指标。

## 本地运行

1. 从 [Kaggle Bank Customer Churn](https://www.kaggle.com/datasets/radheshyamkollipara/bank-customer-churn) 下载 `Customer-Churn-Records.csv`，放进仓库根目录的 `data/`。
2. 在仓库根目录运行以下命令。本次用 Python 3.13 验证。

   ```bash
   python -m pip install -r requirements.txt
   python scripts/import_bank_data.py
   python scripts/query_bank.py
   ```

第一份脚本在本地生成 `my_first_bank.db` 并加载 `Bank_Churn` 表。再次运行导入会替换该表。第二份脚本读取数据库，并打印三项查询的汇总结果。原始 CSV 和本地数据库由 Git 忽略。

## 项目文件

| 文件 | 用途 |
| --- | --- |
| [scripts/import_bank_data.py](scripts/import_bank_data.py) | 读取 CSV 并导入 SQLite |
| [scripts/query_bank.py](scripts/query_bank.py) | 运行原有的三项查询 |
| [requirements.txt](requirements.txt) | pandas 依赖 |

## 下一步

用 `Exited` 统计各组的流失人数和流失率，再挑一个对比结果做可视化。现阶段保留初版客户画像练习的范围。
