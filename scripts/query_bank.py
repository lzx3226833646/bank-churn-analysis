import pandas as pd
import sqlite3  
import os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path=os.path.join(BASE_DIR,'my_first_bank.db')
conn = sqlite3.connect(db_path)

# 查询1（修正版）：年龄大于40岁的女性客户有多少人？
query1 = """
SELECT COUNT(*) as 女性中年客户数 
FROM bank_churn 
WHERE CAST(REPLACE(Age, '%', '') AS INTEGER) > 40 
  AND Gender = 'Female'
"""
result1=pd.read_sql_query(query1, conn)
print("查询1结果:",result1)


# 查询2（重写）：按国家（Geography）分组，统计每个国家的平均信用评分（CreditScore）
query2 = """
SELECT Geography, AVG(CreditScore) as 平均信用评分  
FROM bank_churn 
GROUP BY Geography
"""
result2=pd.read_sql_query(query2, conn)
print("查询2结果:",result2)

# 查询3（重写）：筛选出高余额（Balance>100000）且产品使用少（NumOfProducts<=2）的“高价值沉睡潜力客户”
query3 = """
SELECT COUNT(*) as 高价值沉睡潜力客户数
FROM bank_churn
WHERE Balance > 100000
  AND NumOfProducts <= 2
"""
result3=pd.read_sql_query(query3, conn)
print("查询3结果:",result3)

conn.close()
