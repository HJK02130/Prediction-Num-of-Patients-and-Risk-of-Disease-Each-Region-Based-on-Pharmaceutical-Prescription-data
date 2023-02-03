
### 2010년 의약품 처방데이터_part1을 전처리 ###

import pandas as pd

df = pd.read_csv('2010_part1.csv')

# 데이터 파악
# print(df.info())
# print(df.isnull().sum())

# 결측치 제거
# 한 개 이상의 att에 해당되는 value가 결측치일 경우 제거
df = df.dropna()
print(df.head(10), "\n")

# 중복데이터 제거
df = df.drop_duplicates(["MEM_NUM","PRSC_DATE","ATC_CODE"],keep="first")
print(df.head(10))
