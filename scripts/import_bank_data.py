import pandas as pd
import sqlite3
import os

# 获取当前脚本所在目录的父目录（即项目根目录）
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 构建数据文件和数据库文件的绝对路径
csv_path = os.path.join(BASE_DIR, 'data', 'Customer-Churn-Records.csv')
db_path = os.path.join(BASE_DIR, 'my_first_bank.db')

# 1. 读取真实CSV文件
df = pd.read_csv(csv_path)

# 2. 连接数据库（同一个db文件）
conn = sqlite3.connect(db_path)

# 3. 把整个表格存入数据库，表名叫做 'bank_churn'
df.to_sql('Bank_Churn', conn, if_exists='replace', index=False)

# 4. 简单验证：看看有多少行数据
count=pd.read_sql_query("SELECT COUNT(*) as 总行数 FROM Bank_Churn", conn)
print("真实数据导入成功！总共有：")
print(count)

conn.close()