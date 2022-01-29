
############################# (1) 2010년 의약품 처방데이터_part1을 연월별/지역별로 변환 ################################

import pandas as pd
from collections import Counter

# csv_test에 test파일 저장
df = pd.read_csv('2010_part1.csv')

# 결측치 제거
# 한 개 이상의 att에 해당되는 value가 결측치일 경우 제거
df = df.dropna()
# print(df)
# print(df.head(10))

# 중복데이터 제거
df = df.drop_duplicates(["MEM_NUM", "PRSC_DATE", "ATC_CODE"], keep="first")
# print(df.head(10))

# 최빈값 구하는 함수 (변수형태)
def mostCommon(lst):
    assert isinstance(lst, list)
    if len(lst) == 0:
        return None
    return Counter(lst).most_common(n=1)[0][0]

# 최빈값 구하는 함수 (리스트형태)
def modeFinder(lst):
    c = Counter(lst)
    order = c.most_common()
    maximum = order[0][1]

    modes = []
    for num in order:
        if num[1] == maximum:
            modes.append(num[0])
        return modes

# 지역별, 연월별로 순서대로 나열된 새로운 dataframe 만드는 함수
areaList = [11, 26, 27, 28, 29, 30, 31, 36, 41, 42, 43, 44, 45, 46, 47, 48, 50]
dateList = ["201001", "201002", "201003", "201004", "201005", "201006",
            "201007", "201008", "201009", "201010", "201011", "201012"]
dateList1 = ["201801", "201802", "201803", "201804", "201805", "201806",
            "201807", "201808", "201809", "201810", "201811", "201812"]

def city_date_code(codelst, area, date):
    lstFirst = pd.DataFrame(columns=["MEM_NUM", "PRSC_NUM", "MED_NUM", "CITY_NUM", "PRSC_DATE", "ATC_CODE"])
    for i in area:
        for j in date:
            lstAdd = codelst.loc[(codelst['CITY_NUM'] == i)]
            lstAdd = lstAdd.loc[(lstAdd['PRSC_DATE'].str.contains(j, na=False))]
            lstFirst = pd.concat([lstFirst, lstAdd], ignore_index=True)
    return lstFirst



# 1. 총 처방건수를 추출할 의약품 선정 (최다처방건수 top10), 의약품코드 활용
# 의약품 코드 데이터들을 data frame --> 리스트로 변환
code = df['ATC_CODE']
codeValue = code.values
codeList = codeValue.tolist()

# 의약품코드 df에서 순서대로 10개 출력
# print(codeList[0:10])
# print()

# 최다빈도의약품 top10 (의약품코드, 빈도수)
codeCnt = Counter(codeList)
print(codeCnt.most_common(10))
print()

# 2. 해당 의약품이 처방된 모든 데이터 추출, 조건활용
# 각 codeLine : 해당 의약품의 처방 데이터 모음
code1 = df.loc[df['ATC_CODE'].str.contains('438901ATB', na=False)]
code2 = df.loc[df['ATC_CODE'].str.contains('220902ATB', na=False)]
code3 = df.loc[df['ATC_CODE'].str.contains('186101ATB', na=False)]
code4 = df.loc[df['ATC_CODE'].str.contains('421001ATB', na=False)]
code5 = df.loc[df['ATC_CODE'].str.contains('222901ATB', na=False)]
code6 = df.loc[df['ATC_CODE'].str.contains('268000ATB', na=False)]
code7 = df.loc[df['ATC_CODE'].str.contains('101804ACH', na=False)]
code8 = df.loc[df['ATC_CODE'].str.contains('133301ATB', na=False)]
code9 = df.loc[df['ATC_CODE'].str.contains('271800ATB', na=False)]
# ex) 의약품코드 '438901ATB'의 총 처방건수 출력
print(code1.head(5), "\n")

# 3. 해당 의약품들을 지역별 + 연월별로 순서대로 나눔, 시도코드 및 처방개시일자 활용
# 처방개시일자의 dtype을 문자열(str)로 바꿈
code1 = code1.astype({'PRSC_DATE': 'str'})
code2 = code2.astype({'PRSC_DATE': 'str'})
code3 = code3.astype({'PRSC_DATE': 'str'})
code4 = code4.astype({'PRSC_DATE': 'str'})
code5 = code5.astype({'PRSC_DATE': 'str'})
code6 = code6.astype({'PRSC_DATE': 'str'})
code7 = code7.astype({'PRSC_DATE': 'str'})
code8 = code8.astype({'PRSC_DATE': 'str'})
code9 = code9.astype({'PRSC_DATE': 'str'})
# ex) code1의 data frame dype전체출력
# print(code1.dtypes)

# 의약품별-지역별-연월별                =>            # 같은연월 같은지역 같은의약품
code1 = city_date_code(code1, areaList, dateList)   #         같은지역 같은의약품
code2 = city_date_code(code2, areaList, dateList)   #                 같은의약품
code3 = city_date_code(code3, areaList, dateList)
code4 = city_date_code(code4, areaList, dateList)
code5 = city_date_code(code5, areaList, dateList)
code6 = city_date_code(code6, areaList, dateList)
code7 = city_date_code(code7, areaList, dateList)
code8 = city_date_code(code8, areaList, dateList)
code9 = city_date_code(code9, areaList, dateList)
# ex) code1의 지역별, 연월별(일은 무시) 처방건수 출력
print(code1.head(5))
# print(len(code1))       # dateList에 존재하지 않는 시도코드는 무시


############################################## (2) 지역별 데이터 추출 ####################################################
def prdct(lst, code, list):
    for i in lst:
        print("총 처방건수", len(i))
        for j in code:
            a = i['CITY_NUM'] == j
            area = i[a]
            print(j, "의 총 처방건수", len(area))
            list.append(len(area))
        print(list)
        list = []


codelist = [code1, code2, code3, code4, code5, code6, code7, code8, code9]
citycodelist = [11, 26, 27, 28, 29, 30, 31, 36, 41, 42, 43, 44, 45, 46, 47, 48, 50]
codenamelist = ['428901ATB', '220902ATB', '186101ATB', '421001ATB', '222901ATB',
                '268000ATB', '101804ACH', '133301ATB', '271800ATB']
a = []
prdct(codelist, citycodelist, a)