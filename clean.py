import numpy as np
import pandas as pd
import re

# 文件读取
def open_file(file_location, mode='r'):
        # 自动根据文件扩展名推断文件类型
     if file_location.endswith('.csv'):
         return pd.read_csv(file_location)
     elif file_location.endswith('.xlsx') or file_location.endswith('.xls'):
         return pd.read_excel(file_location)
     else:
         raise ValueError('Unsupported file type.')

# 如果数据中已经有省份信息，对省份格式进行统一
def clean_province_name(name):
    if isinstance(name, str):  # 检查是否为字符串类型
        pattern = re.compile(r'(省|自治区|市|维吾尔|回族)$')
        return re.sub(pattern, '', name)
    else:
        return name  # 如果不是字符串类型，则返回原值

# 不同时间格式提取年份
def extract_year(date_str):
    # 定义日期格式的正则表达式
    match = re.search(r'\b(\d{4})\b', date_str)
    if match:
        return match.group()
    # else:print('ValueError')
    else:
        print('ValueError')
        return None


data = {
    'date': ["25-12-2020", "2020-12-25", "2020.12.25", "31-01-2021", "2021-01-31", "2021.01.31", "2342343","2024.01.31"]
}
df = pd.DataFrame(data)
df['year'] = df['date'].apply(extract_year)
print(df)