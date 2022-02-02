# <div align=center> 의약품 처방데이터 기반 환자 수 및 지역별 위험도 예측 </div>
#### <div align=center> Predicting The Number Of Patients And Risk Of Each Korea Region Based On Drug Prescription Data </div>

<br />
<br />

### <div align=center> :computer: Language & Development Environment :computer: </div>
<br />
<div align=center>
	<img src="https://img.shields.io/badge/Python-3766AB?style=flat-square&logo=Python&logoColor=white"/> 
	<img src="https://img.shields.io/badge/Visual Studio-5C2D91?style=flat-square&logo=Visual Studio&logoColor=white"/> </div>

<br />
<br />

### <div align=center> :cactus: Me :cactus: </div>
<br />
<div align=center>
	<a href = "https://github.com/HJK02130"><img src ="https://img.shields.io/badge/GitHub-181717.svg?&style=flat-square&logo=GitHub&logoColor=white"/> </a> 
	<a href = hjk02130@gmail.com> <img src ="https://img.shields.io/badge/Gmail-EA4335.svg?&style=flat-squar&logo=Gmail&logoColor=white"/></a>

# 개요


 뉴스 및 각종 자료의 지역별 특정 질병의 환자 수는 국민건강검진자료로부터 통계된
자료로, 온 국민이 참여하지 않을 뿐더러 특정 연령 이상만 정기적으로 참여하기
때문에 정확한 자료가 아니다. 또한, 연령, 성별 등을 기준으로 나뉘어진 환자 수
통계는 많이 있지만, 지역을 기준으로 나뉘어진 환자 수 통계는 흔한 질병의 자료만
찾아볼 수 있다.

 본 데이터분석 캡스톤디자인 연구에서는 2010년에서 2017년까지의 전국 각지의 의약품 처방 데이터를 기반으로 상관분석과 회귀분석을 통해 가장 최근 데이터인 2018년 의약품 처방 데이터를 적용시켜 특정 질병들의 2018년 지역별 환자 수를 분석하고 분석한 환자 수를 바탕으로 해당 질병에 대한 발생 위험도를 지역별로 예측하여 지역별로 질병에 대한 위험도의 시사점을 도출한다.

상관분석과 회귀분석을 이용하여 결과를 도출하는 방법은 다음과 같다.
먼저, Pearson 상관계수를 이용한 상관분석을 통해 특정 의약품과 해당 의약품이 효과를 발휘하는 여러가지 질병들과의 연관된 정도(r)를 파악한다. 이후 연관된 정도가 높게 대응되는 의약품과 질병끼리의 선형회귀분석을 통해 의약품 처방건수를 바탕으로 해당 의약품과 연관성이 높은 질병의 예상 총 환자수를 산출하는 선형회귀식을 얻는다. 선형회귀식에 가장 최근 데이터인 2018년도 의약품 처방건수 데이터를 대입하고 가중치 개념을 도입하여 2018년 지역별 특정 질병들의 환자수를 예측하고 마지막으로 다른지역과 비교하여 얻어진 질병 발생 위험도를 산출한다.


# **데이터 수집**

## 1. 2010-2018 의약품 처방 데이터 (출처 : 공공데이터포털)

    

![](https://lh3.googleusercontent.com/ChBZYAxNmhX5VzUE6gG_BtNKOIVTcTWF0bN1N4q8vbsBANOqo-jd3wIjMmcZtnJPLQtFS89cSnpMASdK-VGVlQTunTQ1m973zCxqyma_fWC_pwthtBwie-7q5bG3RegyXfTGpVR3)

다빈도 처방 의약품을 선정하고, 연월별 및 지역별로 의약품을 분류하고 실제 의약품이 처방되는 관련 질병과의 상관분석을 위해 수집한 데이터로, 처방 건에 대한 여러가지 속성이 포함되어있는 엑셀 형식의 데이터이다.

  

## 2. 2010-2018 다빈도 500가지 질병별 환자 수 (출처 : 보건의료빅데이터개방시스템)

    

![](https://lh4.googleusercontent.com/8MCwPQp1kytMG2u-PyFcIYFWjY4pod1k_kBMGA9QbdTin4g5bLRdQwLk1D9me7vTSJ8yqc5-Q8t6y_xiQsi5KDj0AzWHwUGVOYfGyLQe88cp_gji-tepji6yQ7Zj7iRoU877W5_L)

![](https://lh3.googleusercontent.com/taYOkBySPUOa_p26xIb5ZtGtq_kI_3eta7oYV7Sr1xuv2RDTsLyzjorw0ep18IYYNbBdk5KKhRTDskK-UWqqKxEE-E2SA6cKWj7PNhooxs7gN2tyf8lxRbY4mxfv87gTKRwmkjLu)![](https://lh6.googleusercontent.com/k9E6qISi-0PaKH2glz3t5qsN-wYmxX7ziruCPnJCB2jiNbeSI3q3hcjCQA8thR0skVicn9fQmQi5zHKiKIe9eB1RbBFCz9cP4LBrytOmvRUSNhCzIOI0yzeg3e0Dc39vqDzCrTuG)

a의 2010-2018 의약품 처방 데이터로부터 선정된 다빈도 질병에 대한 9년간의 연도별 환자 수를 산출하기 위해 수집한 데이터로, 엑셀 형식이다.

  

## 3. 2010-2018 지역별 총 인구 수 (출처 : 통계청)

    

![](https://lh4.googleusercontent.com/BiYPJ-3e5JtrFIiSof2LmIrUZsWVsTKjMYRHiuV4DsGfW_Sw07eZ_wvzSKM0kGdccmh4Fhn_QLbGMkUv3SMOzHLfjiBdDf904j7pSjjsAGi4tWGZH1CkenrKb7NzQEPnwuAZCjOV)

회귀분석에서 가중치 계산을 위해 수집한 데이터이다.

  

## 4. 의약품 검색 시스템, 지역코드, 생활 속 질병통계 100선

    

## 5. 의약품 검색 시스템

    

![](https://lh4.googleusercontent.com/5lx5_dTa4rY3GZ8FgvrzRFBYlvM8wKvmpO2jz5C636Bk9wJdY1okVMfesAdJxnOHKLMXWC2n8oQGYIv7wkhUeN-tG2qNd5-3dGI-u7pTKbxiRG54xIAn1KDLOC9N66kslCX5sivA)

의약품 코드를 검색하여 해당 의약품의 효능 정보, 즉 해당 의약품이 작용하는 질병들의 목록을 수집하기 위한 시스템이다.

## 6. 지역코드

    

국내 시/도별로 제공된 코드로, 지역별 특정 질병의 환자 수 분석 및 예측을 위해 필요한 데이터이다.

  

## 7. 생활 속 질병통계 100선

![](https://lh5.googleusercontent.com/HMep0KYJmuUvNkltpBkRFl9EREg9tlViGAejC98hdzgMbWBcofH6m0ow1Ulrhd1q9eGXjgfmd34qNg6tKQYarrJAIebCdUl94HOy25MYArR6vAxy7iEdl_3IOfF1HzjdlnoDz0zq)

질병마다 존재하는 통일된 공식적인 명칭을 파악하기 위해 수집한 데이터로, 의약품 검색 시스템을 통해 얻은 의약품별 관련 질병에 대한 실제 환자 수를 파악할 때 필요한 데이터이다.

# **데이터 전처리**

## 1.  의약품 처방 데이터 (csv파일)

**1) 불필요 att 제거**

    

	a.  attribute (14개)

		기준년도, 환자일련번호, 성별코드, 연령대코드, 처방내역 일련번호, 의약품 일련번호, 시도코드, 처방개시일자, 의약품 일련코드, 1회투약량, 1일 투약량, 총투여일수, 단가, 금액
    

	b.  제거한 attribute (8개)
	
		기준년도, 성별코드, 연령대코드, 1회투약량, 1일 투약량, 총투여일수, 단가, 금액
    
    c. 남은 attribute와 언어 전처리 (6개)
    
	    MEM_NUM : 가입자 번호, PRSC_NUM : 처방내역일련번호, MED_NUM : 일련번호(대부분 1-4), CITY_NUM : 시도코드, PRSC_DATE : 처방(요양)개시일자, ATC_CODE : 의약품코드
    

![](https://lh3.googleusercontent.com/Pz-9RTmULBfSNo95LZNVpYWJW2zLDOHYxO1FoLo7GoRS21mbtOkilzx8bfS494441QIPIV_hOrjjYDZAGUVfxVTEwL3gSdH9I0aCJkdVSfKvwcAafX016jygsxHYADZmtuc1yDvu)

  

**2) 결측치 제거**

한 요소의 결측치라도 포함된다면 행 전체 삭제

  

 **3) 중복데이터**

기준년도, 처방개시일자(년,월,일 중 년,월만 겹칠 경우), 의약품 일련번호가 동시에 같은 데이터일 경우, 분석 시 중복데이터로 여겨 하나만 남기고 삭제

## 2. 시도코드 및 총 인구 수 엑셀파일로 정리

통계청의 ‘전국기준 연월별, 지역별 총 인구 수’ 정보를 바탕으로 17개의 시도코드와 시도별 총

인구수(ex)2016년)를 엑셀파일에 정리

![](https://lh5.googleusercontent.com/RMAts5zuH-Vh9hlT5SdfAQPLXcqjYM-arP5ldPc2i1SwPMwSchc9CZt3lxnoEDX2xq_DxyDZYSnzM_fuI3ozQi1TvxODeDWI_8ziNW5DHiDgx_mpI5wezw3kcv7KZS46j9BfJnAI)

# **데이터 변환**

## 1.  의약품 처방 데이터 데이터 변환
**의약품 처방 데이터 → 연월별 지역별 특정 의약품의 총 처방건수**

**1)  총 처방건수 추출할 의약품 선정**
가장 처방 횟수가 많은 의약품 top10 (의약품코드 이용)

![](https://lh5.googleusercontent.com/edKRoyg1pVx_l5IjkO62o3A1yOGgj195RRvKVa1zkLmRZCXWFjXZppwVOpqiYbmRQ48NIMSXoipOYwgs-MWHsV5TCun-AI_3AAPbDO8x0L4SI6NHplmOGQzPdeY6S1-PfEOfmjKd)

▲ 가장 많이 처방된 의약품 TOP10을 추출

  
  

![](https://lh5.googleusercontent.com/gDADdh_xkL6-x2Qw6U9ZLR8khBKyA-EzJwOGd0jBBLqUoIaWrxvrltijOhI5lvji-ljnXfxbo4R43Ne8YPUBqRGE3aptNRMkO4v2NS9Eqofiy2kk4wz32qvjTXW0i2ZTlzJPrl38)

![](https://lh3.googleusercontent.com/22WY3rd7h0lpde1JEZLNOfNuUrSAQ3zvURN-gTpuCJqCa2WC2UsIRF-a_yw7m0OWQ-hWYH16dCIPJliEulG6Kl05d-5ytPzI1mLxMKRUojIif-zD_0eyxZyrjYz-rsBrGHE2GbU1)

▲ (예 : 2018년) 해당 의약품코드와 빈도수

**2)  해당 의약품이 처방된 모든 데이터 산출 (의약품코드 이용)**
    

![](https://lh6.googleusercontent.com/mmg_OQbRVMhZEtd_g4EYyzJGWmqwlhnLI0ZptxuI2ae7Lmn-ixGDTws00_4MrMsHYdg12DJoyNkSjuC7DPeCqPbvgQlM3eOoSQh45wVjiDkbnYBFeXkWzgh6-ngE4lsu-YwEUepf)

▲ TOP10 의약품별로 데이터프레임에추가

  

![](https://lh4.googleusercontent.com/2j6cgX70207_jx-T3MHuVdKsPSXycJ6QFsihlnwDKgeUFE0sexHg52Y3VDGzpDcAh2TZgFmsE-je3lrqdzI__u1mS6Pfgu9JALqa_dIR7kkozWeeSgK8BR_6hHwow81ctMYWB331)

▲ (예 : 2018년) 의약품 코드 ‘438901ATB’의 데이터프레임 출력

  

**3) 데이터 프레임에 지역별 및 연월별로 나눠 저장 (시도코드, 처방개시일자 이용)**
    

![](https://lh5.googleusercontent.com/xGIvQkdonm4T31JQ1s_kVnScRaQuBqYPVWQ8CLssKOWd1zb47OXX7VlVGqH3SXa3cACzcBnalzRmf1iPyyrZEOHhjTFUByVNIAdSbulD2hmedDOkoZ6Wyyq8kzRew7mRJ9h-0efT)

▲ 지역별, 연월별로 나누는 함수 정의

  

![](https://lh3.googleusercontent.com/HBU7BerUDHcruGwRFT3Omv4tn7XHmmXx1tEK_y3I0FDiD1OXGDTowSGOfHgtuO6RSmruwtjpsSFs1TAp_l8E1fE8WOOwpLYxXz3AyCVRdfpCpY_L-yHvJrj2Hn0o6wWI-ZKYXj8c)

![](https://lh5.googleusercontent.com/rn_-86WZ5_uSbn0XRG4eobzFOKVEsv7eafAyYEX4FGy-Eg1i70yJDFJ0zNLO3Ftuer1ym3Fr9_rqD5D233t-twnNgcAgn8L1o91UjOs-u2MO_eucqPTC4DH0H6IASLAqdRbkqG_W)

▲ (예 : 2018년) 각 의약품별로 지역별, 연월별로 나눠 순서대로 배치 후 데이터프레임화

 - (순서 : 의약품 > 지역 > 연월)
지역 순서 : 11, 26, 27, 28, 29, 30, 31, 36, 41, 42, 43, 44, 45, 46, 47, 48, 50
연월 순서 : 201801, 201802, … , 201812

![](https://lh3.googleusercontent.com/BR4OrbU7x1M7k8tKrPt7i-EO9wjPc-YwYzsUaYf3JLlZa2L5o4t1PL9qZAN5Iwj5ToPZ9jHflgq9ICCrxOtG1yTiihgSctvLSmN9toEcxP04VTESNZ0tx_-13vnr7iW1aV8Ugk28)
▲ (예 : 2018년) 의약품코드 ‘438901ATB’의 지역별, 연월별 데이터프레임 출력

 - 지역 : 11(서울특별시), 연월 : 201801(2018년 1월)이 가장 앞에 와있는 것을 확인 가능

  

**2)  통계청 전국기준 인구 데이터 변환**
통계청 데이터 → 지역코드 포함한 지역별 연월별 총 인구 엑셀 파일에 정리

![](https://lh4.googleusercontent.com/Rennjuc2rvdP4--8SdRl5ublzt6kIRKkibPcabgQ34FJJgGVn3WopKvm3FoCOM9HMXYjABPSsqvAz0xMHM0N2GCDtAnesA6Sklgiz2tf7qicSGP1hH07DO-gMYiBPhbC0Sd1mQkT)

# 상관분석

## 1. 목적

 1. **빈도수 Top10 의약품 중 실제 관련 질병에 주요하게 작용하는 의약품 선별**
 2. **실제 해당 의약품의 관련 질병 중 가장 관련도가 높은 질병 선별**
		

	

## 2. 상관분석을 위한 각 데이터의 연도별 수치 합산

 - **9년간 빈도수 Top10 의약품의 처방건수 합산** 
	  데이터 전처리, 변환을 거쳐 각 의약품별 9년간 총 처방건수 합산

  ![](https://lh4.googleusercontent.com/RKogjXR7kjxkol4ItqA1uxzjkOdAoNApIqet0xOExmzWew8R7oGOWhL0bI15yiY-sKQpEZIQiMvmvqyteGjjy5Be83yx9dGvOAd-5pNxCHLFA0R8TCV47BfKMwtSr986Uf49zZ-F)

 -  **연도별 질병별 실제 총 환자 수 데이터로부터 얻은 각 의약품의 관련 질병을 진단받은 환자 수**
 
 - **Top 1. '438901ATB'**
    -  
   	- 관련 질병 : 발목수술 또는 발목의 외상에 의한 급성 염증성 부종의 완화, 담객출 곤란 (기관지염, 기관지천식, 폐결핵 등)(2010-2017년 순서대로)
	- 발목을 포함한 아래다리의 골절 : 209268 220137 220465 244468 238839 241165 246036 253083 266803
	- 급성 기관지염 : 12252290 13119352 14306530 14932206 15170159 15084909 15896661 16293934 
	- 만성 기관지염 : 376103 384904 417476 373778 378288 371427 387661 421147
	- 천식 : 2221218 2224166 2095986 1872656 1730686 1629665 1631587 1497417
	- 천식 지속상태 : 52573 66509 109524 118616 112264 105113 66946 48833
	- 의학적으로 확인되지 않은 호흡기결핵(2010-2015) : 62230 57319 55124 51915 48191 45716
	- 의학적으로 확인된 호흡기결핵(2010-2015) : 55412 53770 54669 52657 49553 46898

 - **Top 2. '220902ATB'**
    - 
     - 관련 질병 : 감기, 부비동염, 상기도알레르기
   	- 감기 : 5025136 4835957 5095481 5067950 4918726 4698713 4595608 4525661
   	- 만성 부비동염 : 1970019 2018695 2115655 2123180 2141145 2091318 2121735 2207931
   	- 급성 부비동염 : 4327992 4063857 4134305 4159578 4016005 4007711 4168561 4116088 3985401
   	- 상기도의 기타질환 380363 424935 444896 448824 469745 447441 439766 451570 479660
   	- 급성 상기도 감염 7014043 6677425 6840598 6603249 6585501 6277081 6152058 5976475 6087367
   	- 알러지성 비염 5569432 5557107 5984984 6091834 6301156 6237961 6682306 6841314 713510

 - **Top 3. '186101ATB'**
    - 
   	- 관련 질병 : 류마티스 관절염, 퇴행성 관절염, 전립선암, 오십견, 폐암
   	- 양성 류마티스 관절염 : 75642 80862 87799 93359 98330 104724 109123 113419 122226
	- 기타 류마티스 관절염 : 227607 225419 214412 198439 184226 172030 160903 147487 141190
	-  (퇴행성 관절염)기타 관절염 1060604 1067716 1095776 1083168 1081663 1059957 1080615 1085882 1099412
	- (전립선암) 전립선증식증 787803 842069 917599 989478 1040086 1073147 1152399 1213324 1293990
	-  (전립선암) 전립선의 악성 신생물 43678 50390 56798 63127 67934 72054 81701 89843 94507
	-  (오십견) 어깨병변:  1642494 1791644 1916479 1978070 2041201 2094985 2190208 2271751 2359527
	-  (오십견) 어깨 및 위팔의 골절 114016 117041 121420 128160 131673 134060 134776 136452 137275
	- (오십견) 어깨 및 위팔 부위의 근육 및 힘줄의 손실 117208 135922 155348 172945 176709 181801 187569 190171 186665
	- (폐암) 기관지 및 폐의 악성 신생물 81723 86124 94831 100580 102568 105990 114808 120079 133522
   

 - Top 4. '101430ATR'
	 - 
	 - 관련 질병 : 해열 및 감기에 의한 동통(통증)과 두통, 치통 ,근육통, 허리동통(통증), 생리통, 관절통의 완화
	 - 기타 및 원인 미상의 열 624209 563276 686389 664440 685500 719637 764413 730988 780826
	 - 감기 : 위 데이터 참조
	 - 두통 674064 678702 742903 753462 766194 798949 882947 909421 933490
    

  

-   Top 5. '421001ATB'
	-
	-  관련 질병 : 기능성 소화불량으로 인한 소화기증상 (속쓰림,구역,구토)
	- 구역 및 구토 357640 357096 404948 414297 420288 595762 654669 633645 619325
	- 기능성 소화불량 611654 637203 673649 664637 621705 630072 603623 612385 693890
    

  

-   Top 6. '222901ATB'
	- 
	- 관련 질병 : 위궤양, 급성위염, 만성위염의 급성악화
	-  위궤양 : 1388929 1353374 1279644 1183751 1102193 1044235 1020855 954402 926158
	-  위염 및 십이지장염 5443938 5571478 5796726 5642399 5375714 5584384 5393505 5306707 5360959
    
-   Top 7. '268000ATB'
	- 
	- 관련 질병 : 기침, 가래
	- 감기 : 위 데이터 참조
	- 폐 : 위 데이터 참조

-   Top 8. '101804ACH'
	- 
	- 관련 질병 : 급ㆍ만성기관지염, 기관지천식, 후두염, 부비동염, 낭성섬유증
	-  급성 기관지염 : 위 데이터 참조
	- 상세불명의 만성 기관지염 : 위 데이터 참조
	- 단순성 및 점액화농성 만성 기관지염 : 위 데이터 참조
	- 급성인지 만성인지 명시되지 않은 기관지염 1726675 1873035 2264090 2155665 2322925 2363825 2487776 2537636 2636084
	- 급성 후두염 및 기관염 3573202 3442803 3510619 3896099 3360783 3186320 3339400 3377432 3450449
	- 급성 폐색성 후두염 및 후두개염 149405 127415 151834 144862 136906 129864 141005 134568 140006
	- ‘간’의 섬유증 및 경변증 76921 79635 84726 87565 85097 87123 90883 90088 96366
    
-   Top 9. '133301ATB'
	- 
	- 관련 질병 : 위·십이지장궤양, 역류성식도염, 재발성궤양, 문합부궤양, 졸링거-엘리슨증후군, 급성위염, 만성위염의 급성악화기
	- 위궤양 : 위 데이터 참조
	- 십이지장궤양 : 위 데이터 참조
	- 위-식도역류병 2847763 3107033 3378715 3533638 3635931 3873549 4179510 4287987 4452764
	- 위염 : 위 데이터 참조
-   Top 10. '271800ATB'
	- 
	- 위·십이지장궤양, 위염, 졸링거-엘리슨증후군, 역류성식도염, 마취전투약(멘델슨증후군예방), 수술후궤양, 비스테로이드소염진통제(NSAID)로 인한 위·십이지장궤양
	- 위궤양 : 위 데이터 참조
	- 십이지장궤양 : 위 데이터 참조
	- 위-식도역류병 : 위 데이터 참조
    

  

## 2. 연도별 의약품별 처방건수 합산
※ 의약품 코드 ‘101405ATR’은 2010년대 후반 ‘101430ATR’로 바뀌었으므로, 두 의약품 코드는 제외하고 분석할 예정이다.

![](https://lh3.googleusercontent.com/w-aJS3dvZyWiUi2ji6YLL0Qjsq56IPmwErY8jdIq9SnEGRcIeDGshD39J2zKaZCdLIP2oJuE42gX0oO8QqCcVrcpu41ji0j1usOD5jorR7bdeE5hod7qb_aKO3eCnA5aKiqVY-b8)
▲ 의약품별 처방건수 합산 예시) 2010년

  

위와 같이 python 코딩을 통해 2010년 의약품별 처방건수를 합산하였다.

(데이터양이 너무 많아 엑셀이 한번에 읽어내지 못하여 part를 나눠 데이터 추출 후 결과 합산)

  

-   2010년
    

![](https://lh4.googleusercontent.com/lj7Xx8YYe0Nv79qPkYAy8OVcbPRAMPLjcyVdtTXpPO_Vu4rOn8YKth7_sCDNqNzRFmTpuClSZ3wcY3FalxY1XtraCotHMFRL94NjcBb-WdwsImL-a8et6q_RdvZbpH-EQACFxOz9)  ![](https://lh3.googleusercontent.com/3BmxbWOcJKeHDb0kz_VNYQAgZ13RdExui7BEk9AmioSimyB1aiih18hfjd7lONUR7RfHVus_xYUrz3_Mw1TBlDn0dLMDhoeBjS7Bqt6DgI_ZodU3WG6OSQbFYstnE3UuPXtBOnpk)

▲ 연도별 처방건수 예) 2010년 part1 ▲ 2010년 part2

1.  '438901ATB' : 62242 건
    
2.  '220902ATB' : 40117 건
    
3.  '186101ATB' : 39458 건
    
4.  '421001ATB' : 6601 건
    
5.  '222901ATB' : 25421 건
    
6.  '268000ATB' : 36920 건
    
7.  '101804ACH' : 35940 건
    
8.  '133301ATB' : 36219 건
    
9.  '271800ATB' : 5829 건
    

  

-   2011년
    

1.  '438901ATB' : 70687 건
    
2.  '220902ATB' : 39934 건
    
3.  '186101ATB' : 39303 건
    
4.  '421001ATB' : 25296 건
    
5.  '222901ATB' : 139437 건
    
6.  '268000ATB' : 36370 건
    
7.  '101804ACH' : 37201 건
    
8.  '133301ATB' : 35475 건
    
9.  '271800ATB' : 7190 건
    

  

-   2012년
    

1.  '438901ATB' : 84741 건
    
2.  '220902ATB' : 42563 건
    
3.  '186101ATB' : 41805 건
    
4.  '421001ATB' : 38716 건
    
5.  '222901ATB' : 36103 건
    
6.  '268000ATB' : 39736 건
    
7.  '101804ACH' : 40063 건
    
8.  '133301ATB' : 36917 건
    
9.  '271800ATB' : 13719 건
    

  

-   2013년
    

1.  '438901ATB' : 86010 건
    
2.  '220902ATB' : 51464 건
    
3.  '186101ATB' : 45874 건
    
4.  '421001ATB' : 40532 건
    
5.  '222901ATB' : 37181 건
    
6.  '268000ATB' : 38427 건
    
7.  '101804ACH' : 42328 건
    
8.  '133301ATB' : 36053 건
    
9.  '271800ATB' : 15174 건
    

  

-   2014년
    

1.  '438901ATB' : 86524 건
    
2.  '220902ATB' : 54299 건
    
3.  '186101ATB' : 48165 건
    
4.  '421001ATB' : 42409 건
    
5.  '222901ATB' : 42517 건
    
6.  '268000ATB' : 41247 건
    
7.  '101804ACH' : 45956 건
    
8.  '133301ATB' : 35151 건
    
9.  '271800ATB' : 17232 건
    

  

-   2015년
    

1.  '438901ATB' : 86566 건
    
2.  '220902ATB' : 50686 건
    
3.  '186101ATB' : 50709 건
    
4.  '421001ATB' : 43600 건
    
5.  '222901ATB' : 40850 건
    
6.  '268000ATB' : 33730 건
    
7.  '101804ACH' : 40706 건
    
8.  '133301ATB' : 30940 건
    
9.  '271800ATB' : 27795 건
    

  

-   2016년
    

1.  '438901ATB' : 81517 건
    
2.  '220902ATB' : 51283 건
    
3.  '186101ATB' : 51603 건
    
4.  '421001ATB' : 45055 건
    
5.  '222901ATB' : 45194 건
    
6.  '268000ATB' : 35345 건
    
7.  '101804ACH' : 29890 건
    
8.  '133301ATB' : 24374 건
    
9.  '271800ATB' : 33590 건
    

  

-   2017년
    

1.  '438901ATB' : 81256
    
2.  '220902ATB' : 52940
    
3.  '186101ATB' : 53381
    
4.  '421001ATB' : 45479
    
5.  '222901ATB' : 47727
    
6.  '268000ATB' :35780
    
7.  '101804ACH' : 28002
    
8.  '133301ATB' : 22377
    
9.  '271800ATB' : 37009
    

  

-   2018년
    

1.  '438901ATB' : 76652
    
2.  '220902ATB' : 62876
    
3.  '186101ATB' : 65422
    
4.  '421001ATB' : 46901
    
5.  '222901ATB' : 48400
    
6.  '268000ATB' : 28267
    
7.  '101804ACH' : 27114
    
8.  '133301ATB' : 19447
    
9.  '271800ATB' : 40911
    

  
  

## 3. Pearson 상관계수

-   r = x(연도별 처방건수)와 y(연도별 실제 환자수)가 함께 변하는 정도
    
-   연도별 처방건수와 연도별 실제 환자수 간의 관련성을 구하기 위해 Pearson 상관계수를 이용한다.
    
-   1에 가까울수록 양의 상관관계, -1에 가까울수록 음의 상관관계
    

  

![](https://lh5.googleusercontent.com/Q-NZTpjSEokxxYwMoyo-Rq0AS2MhBHRszUY5xX5EH8zTRE_rYxLW0WigT0WJCQWjC2PNY8u3D4HvrFNdVpaP1XS2-ks_x1PdNU5TQoKgFrKvec0Rar-EDs5OedMUypSmUkrS8H1P)

▲ 상관분석 예시) '428901ATB'와 '발목을 포함한 아래다리의 골절' 상관분석

  

## 4. 상관분석 결과 ( 80 ≤ r < 100, 60 ≤ r < 80)

 1. '428901ATB'과 관련 질병 간의 상관분석 결과
	
			 
		 발목을 포함한 아래다리의 골절'과의 상관관계
    

![](https://lh6.googleusercontent.com/Umb7aivDTPSXS-noucpLvBtpNA86sOk2LWky-_ugv2JQ_jDRQ49AS3sVC8t-nJ2LY1ZOl0yPogqkm_7t8LIPowzGqO4RMwHvRmffulycYIkO7jcaQURtlDtya-lCUvJDD8n26uFv) 
r = 0.488703

		‘급성 기관지염’과의 상관관계
![](https://lh6.googleusercontent.com/QWUt4cpYGZH04abIyIEVAk8frWsoxNQuy3dlz1Q-h23muyiqWLI_lnlCLi3SbqnX9tOS3v2f8a8xOI3g5YTdkBha1VwEE7SJN5Mhbif4Cpe6huT2MJHxbulP4Oav-Z5SoMuVWiPW) r = 0.61905

  

		‘만성 기관지염’과의 상관관계
    

![](https://lh5.googleusercontent.com/yVojx-FNYucl9UYD7w2GtzV9n96gqSH8HGmrD4fD9hMH9Y7oaMXxwfvscKOg8ToqqbOKcXxKpcke0bSIv3V1abFjvKANtz5Jra8U5h2QpCF7_tEOHksineknBRDCLdv5QqunaIPK) r = 0.040375

  

		‘천식’과의 상관관계
    

![](https://lh3.googleusercontent.com/QNAoboCSq9gBpvVIerKOjVP-PeDeb3G6FuBDbzfwrcjH41dw9GeSM8Mlg-k6-SpH1XdxuVKw5_gaHMbfQdAD2Qo2QZbLccWf3O7Y_Fp8PKRe_q7S1-pwY6l2Fqic8-PhB8slQCYO) r = -0.519755

  

		‘천식 지속상태’와의 상관관계
    

![](https://lh4.googleusercontent.com/4fsoN1j-MNhtn-LMe6FTWpaaW1hviZmeWftRjwxMCWEB51gBwqGLz5wABqq1QAchjxzLXM1H-3iwCmdecT_ao-K_AA3W5s8kjVUFlFGVVowO7De0oGXPpjm9WjDWxBycUMj7ZUCo) r = 0.699196

  

		‘의학적으로 확인되지 않은 호흡기결핵 (2010-2015)’
    

![](https://lh6.googleusercontent.com/IGRKtr7XD8wKPwMMa15bdS9_LbiVWaKlO6YZzFoiCqYlupgIBWD4CYnsCowq1wZxJGVChYQwDke9J6e4Mzxwv9dADsPiMsk1MRijU-Gvazw4Cl1l3Nfwe6xKREwEwO_hSw5xvE4O) r = -0.877957

  

		'의학적으로 확인된 호흡기결핵'(2010-2015)
    

![](https://lh4.googleusercontent.com/CpQ69bhWngKREnLw2VhWZyt2PtQy_Ocu5MZjX68_2mDZ2kqcSHU4SQ6WFTdJSEuyzglSlshPbMKpSB0wsql20F1E-4Zccx0UT3BlryiuKL7e9lYI0_Xl2Gcwgq0dj5zRpQswbo62) r = -0.636903

  

2.  '220902ATB'과 관련 질병 간의 상관분석 결과
		
		알러지성 비염, r = 0.90
		만성 부비동염, r = 0.86
		상기도의 기타질환, r = 0.83
    

3.  '186101ATB'과 관련 질병 간의 상관분석 결과
    
		기관지 및 폐의 악성 신생물(폐암), r = 0.97
		양성 류마티스 관절염, r = 0.96
		전립선의 악성 신생물(전립선암), r = 0.94
		(어깨병변(오십견)), r = 0.93
    

4.  '421001ATB'과 관련 질병 간의 상관분석 결과

		구역 및 구토, r = 0.70
    

5.  '222901ATB'과 관련 질병 간의 상관분석 결과
    
	    위궤양, r = 0.28
    

6.  '268000ATB'과 관련 질병 간의 상관분석 결과
    

		감기, r = 0.70
    

7.  '101804ATB'과 관련 질병 간의 상관분석 결과
    
		단순성 및 점액화농성 만성 기관지염, r = 0.53
    

8.  '133301ATB'과 관련 질병 간의 상관분석 결과
	
		위궤양, r = 0.85
		십이지장궤양, r = 0.85
		위염, r = 0.67
    

9.  '271800ATB'과 관련 질병 간의 상관분석 결과

		 위-식도 역류병, r = 0.98
    

  

## 5. 음의 상관관계에 관한 견해

1.  **이유**
	a. 의약품 검색 시스템으로부터 얻은 각 의약품들이 효능을 발휘하는 질병은 한 가지가 아니다.
    

![](https://lh6.googleusercontent.com/TsQnuucerFpSZineHEbs1PQc-HvG27lsgkDRW9hoCkBSV1T9xKHtjuyYry4QWezvXaG8g9s7vQi0JQVfUlvBL9LYlWXvCojEpwS4-FvcWk0KgaDJR3gu4FU2sLnTFBvB9q0l5pr9)

▲ 의약품 ‘220902ATB’가 효능을 발휘하는 질병과의 상관분석 결과

-   위와 같이, 한 의약품이 한 가지 질병만을 위해 만들어진 것이 아님을 알 수 있다.
    

  

	b.  특정 질병을 치료할 수 있는 의약품이 한 가지가 아니다. 즉, 특정 질병에 대해 의사들이 처방하거나 약국에서 제공하는 의약품이 1대1로 정해져있지 않다.
    

![](https://lh5.googleusercontent.com/Seb-pcatKnxM9SJ3iRkQ4LqGsRdRW8kn18obwLQdEG9caAGYEIyrgAf_6BGVjuUyitxVxT0VPV_tGiRorAFtTJTr5RPNpJFdqVojZ3Mk9H84Z-OfJyC1bfl0bTjwPYt3uV4ydyGx)  ![](https://lh4.googleusercontent.com/WMMr2djvEZxohiLQSfnrHvt2rKBz3fWe8x_q8t_1CC5anys0U_NWNdCsy-HUweBCyi2qOnagnK60-uG1Pqrw-zCxyzNomup-mLiVs6z4s9UfRkcjp2VhDGFY2jyXWlEJclPgNNFN)

-   위 상관분석 결과 두 개를 비교해보면, 위궤양은 의약품 ‘222901ATB’와 ‘133301ATB’ 둘 다 치료가 가능한 질병이며, 따라서 의사들이 해당 질병에 대해 처방하는 의약품이 한가지로 정해져 있는 것이 아님을 알 수 있다.
    
2.  **결론**
    

위 두 이유로인해 한 의약품의 처방건수와 관련 질병의 실제 환자수의 상관분석 결과로 나온 Pearson계수가 1로부터 멀어질 확률이 더 커지게 되며, 특정 질병에 대해 처방되는 의약품들 중 상관성이 현저하게 떨어지는 의약품이 존재하는 것으로 파악된다.

# **회귀분석**


## 목적

회귀분석을 통해 얻은 선형회귀식을 바탕으로 이후 해당 식에 연도별 의약품 총 처방건수를 대입하여 예상 총 환자수를 산출하기 위함이다.

## **방법**

1.  상관분석 결과로 나온 각 질병과 실제 관련이 깊은 의약품의 총 처방 건수와 연도별 실제 총 환자수 데이터를 바탕으로 단순 선형회귀분석을 실시한다.
    
2.  연도별 의약품 총 처방 건수를 바탕으로 예상 총 환자수를 산출하는 선형회귀식을 얻는다.

## **데이터학습을 통한 선형회귀식 산출**

    

1.  **데이터 생성**
    

![](https://lh4.googleusercontent.com/a6qs2WMoq2JcQ38IQ-3VWIyrWBnZ66-I2_I0uccHm0XDzlbLD3RE1syhOK17rubzHUnh07H8ydcKetWGaTMXHRsUyWM9WZtv6OE4c4pzus-U5EFl1sykrkHwZFIaeawcBR4zHSeo)

▲ ex) 의약품 '271800ATB' 처방건수와 위-식도 역류병 실제 환자수를 데이터프레임화

  

![](https://lh5.googleusercontent.com/ht610aCwS26X7hhsDsxxUzLAoz-UON9Cu8Clggq5R69tHeizw9waVbu-KCKJg967QIpjmKe8s9n0JKQbwBygx3a594o-giDPzAcZ9kd5HRTihgkfl8_7TKIIMEMiyAQwOqvlNhEO)

▲ 데이터프레임 출력

  

2.  **산점도 표현**
    

![](https://lh6.googleusercontent.com/xiUvjgj2RUbp7QebEzwBZ0-ehCyXqoGbtXDVC-EE7yS2xAX9nvOovmJn1z3L0beo22pHADHgxP0DKf5_Sx5DaAWR01WLD6sjerKgxsHUv416iGUXJe3VHJ6jgDeC6GIc4KfLMlfe)

▲ ex) 데이터프레임 속 실제 데이터를 그래프로 표현

  

![](https://lh5.googleusercontent.com/hUtiuwhcWj8Mid6qB4opH9IFGftVFKQDFS4Ta6d19acHL0Ub7ASjU_A6-5nll__Jr0m6sQDHM3mqbXDG-98IPDPk-LvPrQ4OP-m1dc1baELnITuWZRFTMPpDG7gISJ6r4gaNurAE)

▲ 산점도 출력

  

3.  **데이터 학습**
    

![](https://lh6.googleusercontent.com/IVAGtxIdwbgkAPiBezw1VfI0bfk8MbIwcTc5aeo1RefAWsKS_J0r4lgiz1K7QmklRrmeE6AExl6AYmTGzqpbBi4wWIws5EMVamV-dd8MhKWjdyE7gaVq7Ur_mZfWOLti5M1I2fU4)

▲ 선형회귀모델을 만들어 fit을 이용해 모델을 학습시키고 y(환자수)를 prediction하여

선형회귀식 산출

![](https://lh4.googleusercontent.com/bfL2JBxfUVcCZcjTAFV7i-YNQ0w-XgkNs2Yajk2Q17jOpfvKpztIrvOQ32pdbIrOmByw18KHwnVnv_lo4Ech_BHve7Nkntrruda35_fSEc4NN4A8FSKtztTj4H7aGNAz0h2ZSjR9)

▲ ex) 의약품 '271800ATB' 처방건수와 위-식도 역류병의 선형회귀식

  

4.  **선형회귀선**
    

![](https://lh6.googleusercontent.com/oWpxSD4PMY9k6GCcoiIhh7OkbEy4abVP6LRNNNfSnrVrnxX-pXdBZ863lL2YsX2pfJv9A9MW_qShmgHbt_TiLSEzNqiGj6TSRJTkTa2ReB7OJC7dcm3mjf7fbDUQ-s5F9p88eYRM)

▲ 선형회귀선과 산점도를 그래프로 산포도에 표현

![](https://lh5.googleusercontent.com/D1DF8j54Kcg8xPK0g-s9JqJatRkUt_Kb8bih3pUV8TQXYOBPGffTrDf_h3gYyl-WfkTB0JhBQ_LHau7AEh-_r7TxqyNGAIYTj71EMDaU3-MAcE0HL9FJtn_teVR5weG-H6KEJEH5)

▲ ex) 의약품 '271800ATB' 처방건수와 위-식도 역류병의 선형회귀선 그래프

## **의약품별 회귀분석 결과**


1.  **'428901ATB'**
    
천식 지속상태 : y(환자수) = [2.36909858] x(처방건수) + ( -104345.30161650729 )
    

![](https://lh5.googleusercontent.com/waQR-GovIKtwSmBYw2RmuL_1MPPX19cgH5FzhfLljIefTvUStlzIbyvDLlrc6MhKCy_TzSFj5bvd73p_ZREp-EeQWxwJ8OQoKWvHRCwRoo4XieaZMvDU9gA7CNuI8aLWaLaNGQHz)

급성 기관지염 :y(환자수) = [121.95126761] x(처방건수) + ( 4882870.182749957 )
    

![](https://lh3.googleusercontent.com/qEoV4s9B979Pfqpe8Dn7-8xzjNFCL8FU48MqnlyTiDmL7ichVj6QDmvgY0tnAt-_AG3ke0wAAqwgN7tpJcVd7tc2K2vTRNPGr2xOjDG7Gbpn7yyaKhd_eE89nNPRlboFNOthJD1M)

  

2.  **'220902ATB’**
    

알러지성 비염 : y(환자수) = [65.44400978] x(처방건수) + ( 3022790.158642797 )
    

![](https://lh4.googleusercontent.com/mhtIsfy4hMI1sRx-jHWdFNR26aqhZFvYaWz6DsD23Q8LVERw-RyBRrAvnXdPRMA_JcL0GLpQQjZ5NpX1utEHWStwNzRu9PQR6ma6K3oBysrwlIlhqFY1ND22G9cwdwhz25He1hsK)

  

만성 부비동염 : y(환자수) = [10.02938655] x(처방건수) + ( 1618194.3182340097 )
    

![](https://lh6.googleusercontent.com/OCWPY7s9xRcWCPvqkz20gRAh9jEXtjI80qD7jy_jwfNkxIKQCh1aS1qHrxNbr-31O0b50yH2XLavgCYvV9WxxiErxku0Hzsy2lZPAhPs1gKgTBD2nLBmWxTeVFznCQYxS2ThzJXQ)

  

상기도의 기타질환 : y(환자수) = [3.42224977] x(처방건수) + ( 274479.94672942546 )
    

![](https://lh6.googleusercontent.com/LskD72n2f6OOoYOu4FciWwy5A_p6zkcMemtTN4mKEtLAiHkgfbvpd9gcv_6W5QAJ-HzIR82fe4QoLsSVcF_YUaNgYCOZl6QiJomYW53yLuSxc_OeJ0jpMjMTn7d7ZMC42h45efHY)

  

3.  **'186101ATB'**
    

기관지 및 폐의 악성 신생물 : y(환자수) = [2.28733382] x(처방건수) + ( -5036.517556468461 )
    

![](https://lh6.googleusercontent.com/WFGzvvA_wbbVzj-Gw8KQx3SQAdSvCYjsCLlYajK6vBfzMYuiBc8NLs82sQH556zI1KIhT3pkMn55Frxmr4XZhvq4Jn9ISNn02iyjdebcLwkoI9SJFBWnc60MQcEekix2X2bl5YR0)

  

양성 류마티스 관절염 : y(환자수) = [2.38746815] x(처방건수) + ( -15102.08522659626 )
    

![](https://lh4.googleusercontent.com/c0fsCodalA-exasHjf9ygBE9gEV4F3HE3GdiGcddFkHXK1kFnBoQTZO8UgvKKhIU2Og_BevntT-EICz-XE2gOr7yqAAc5Dmc9BQtdo-bBBwUso_I7fIlRS4kju9gIsrJBmofhh9K)

  

전립선의 악성 신생물 : y(환자수) = [2.70042319] x(처방건수) + ( -59304.53822832207 )
    

![](https://lh6.googleusercontent.com/cMJa8ySLj_l5V0LXh9WZO5ecnFy0dnb4oBagg2t-JaS4aox8mAFZ2yw9KbJwNfwhF__OifNbZBFmD7qZDqvP8nYYO5SFulwpumW8HUaRftmmuNmA-8NXlX9Qts7584AT1589OlKu)

  
  (어깨병변) : y(환자수) = [35.50414103] x(처방건수) + ( 347464.9481839002 )
    

![](https://lh4.googleusercontent.com/MOHezZ3rH4VRXsQFwb--OyiDQsXgWTgAs4a6gq6iQiF3olbdYNBS-N5BJycv1I5rnIK4dc6X1YKqShIFXVU8fm2ak4YHDWcE4XeicU3z9rgHK33ipxGqOpcxKujSOpjaem-hEvOR)

4.  **'421001ATB'**
    

구역 및 구토 : y(환자수) = [6.22037446] x(처방건수) + ( 256102.2391965168 )
    

![](https://lh4.googleusercontent.com/lpyC3QA0wCf-V2z0RrnFNYxjrgsaDUwb_SBAW2ipLsBjgt7jiGYz0Rdry98WIcY3ZuN79JP4HWOobSZRXTCewS2DT3TU4wKaMZQbzvB7dwS4U87Eox7-R6IuEaYzejJh5io-sRtG)

  

5.  **'222901ATB'**
    

위궤양 : y(환자수) = [1.34503488] x(처방건수) + ( 1096245.0242143534 )
    

![](https://lh4.googleusercontent.com/GC8M4QEWUsjdwqCTHbZspkeLpU6Jn37bFR0jE7ANMhyKVL45AG_D4BDnDJXt58Yyx2zoADcMKcquNQKObrDram0TsLnK2tDFmF2l3hlU5h2XE6cvXjaGfNhYDI3Jyd5fiv9X7DTA)

  

6.  **'268000ATB’**
    

감기 : y(환자수) = [60.77757492] x(처방건수) + ( 2584820.0870024823 )
    

![](https://lh4.googleusercontent.com/acM7wdzkP_4PVmAjnMNVWa59hEom46lXZFffmwRhfG8uL_csTXrF_9MbicZJaoU-BTRHaymGXTZU92aBIU_WgSCPp9xU5hLW4AA3Uuqb55CUIEwmlsUoid4dDSMnjKBMvWGBzAc0)

7.  **'101804ACH’**
    

단순성 및 점액화농성 만성 기관지염 : y(환자수) = [3.97356378] x(처방건수) + ( 358877.39246102126 )
    

![](https://lh6.googleusercontent.com/PJtPGkXr-f_Bk9iI52-jvPI2mRycueMlmP1b3ssDpgx0DLWQ1LHn_WUiQC0P_JFOI77swRT6WdMf9vlOKxTLmtmzZrAAQcLlM1OmLGS_QZb8GvIrsvKwJ2PghcxMHFtkO6CvnhNr)

  
  

8.  **'133301ATB’**
    

위궤양 : y(환자수) = [22.81667171] x(처방건수) + ( 431494.1418296021 )
    

![](https://lh6.googleusercontent.com/Wohlh_FSPVVZ3iw90nHHeaPR4PUt4i2bsJK0N7ZVp-RNs93j2BPlVOMK5wGxQ3hNe8nR808OfhYgiCCkbOeRuzJYqvjhStjj8aA8gxGCctPzv3yvny-o-zvMgDkZ3pBa1R07ta_Z)

  

십이지장궤양 : y(환자수) = [2.79282607] x(처방건수) + ( 216854.31628917926 )
    

![](https://lh5.googleusercontent.com/guFl8mSd6QU-cmTMh4kKfVMSX_rnDico6ltWDfo5lKHRjplkz8Ji2hUR060IaErhCuwf23bXNIHuXcOrWxgH1GBZlJledOMP6X3C0YXgwrGemSvGIS7kciTLL8MYs85JMLntj7iK)

  

위염 : y(환자수) = [18.17840259] x(처방건수) + ( 4929225.407851748 )
    

![](https://lh6.googleusercontent.com/_j5xcXpiXCvyUvdVpPm2HtWvcxmdTPPlJJAPuKj1IYcfqGvXkdvpFgk_5OOT87cNWg140gJJg4ZmNv1I9AzeILzQR-mmdtMKVnYxwoWNT03mY9nZlkMqkoW0FNJJgT7E9p6g5lc6)

  

9.  **'271800ATB'**
    

위-식도 역류병 : y(환자수) = [41.58499963] x(처방건수) + ( 2786613.541055249 )
    

  

![](https://lh6.googleusercontent.com/dRRrhX0IhWMrtAGvfO8u4yGzlIrhgOdoqbYGDHBX5tLSkVK5ff3N-BH9b4GZSpJCpu48RoN8aZZFp8CTJZmnJjkz3U6nW437CXVGD1_hrukCnfKFF3xGZoWXuGHzxTa1NiZyL71u)


# **지역별 환자수 예측**

## **2018년 지역별 환자수 예측**


회귀식에 처방건수 대입을 통해 얻은 수치는 해당 ‘연도’의 예상 환자수이며, 연구로 하고자하는 것은 가장 최근 자료인 2018년 ‘지역별’ 예상 환자수이기 때문에 보다 정확한 지역별 예상 환자수를 고려하기 위하여 가중치를 사용해야 하는 수식이 존재한다.

 - **산출방법 (ex. ‘428901ATB’ 처방건수로 2018년 서울특별시 ‘급성 기관지염’ 환자수 예측)**
 
	 - **2018년 ‘428901ATB’의 서울특별시 가중치 계산 A**
	 지역별 인구 대비 의약품 처방 건수를 고려한 가중치값
	 ((2018년 서울특별시 ‘428901ATB’ 처방건수) / (2018년 서울특별시 인구 수)) * 100

  

	-   **2018년 ‘428901ATB’의 전국 가중치 계산 B**
	지역별 가중치 값에 따라 분배하기 위해 전체 가중치 값 대비 해당 가중치 값의 비율을 고려해야 함 → 각 지역별 가중치 값의 비율을 구할 수 있음
	(2018년 서울특별시 ‘428901ATB’ 처방건수) / (2018년 서울특별시 인구 수) * 100 + (2018년 부산광역시 ‘428901ATB’ 처방건수) / (2018년 부산광역시 인구 수) * 100 + … + (2018년 경상남도 ‘428901ATB’ 처방건수) / (2018년 경상남도 인구 수) * 100

  

	-   **2018년 전국 ‘428901ATB’ 처방건수로 예측한 ‘급성 기관지염’ 환자수의 1% 계산 C**
	이후 연도별 지역별 가중치 값의 비율에 따른 예상 총 환자수를 구하기 위해 연도별 예상 총 환자 수의 1%를 계산

		(회귀분석식의 x에 전국 ‘428901ATB’ 처방건수를 대입한 y값) / 100 = (64.264080318 * 80418 + 9139314.477) / 100

  

	-   **2018년 서울특별시 급성 기관지염 환자수**
	**= ((A / B) * 100 ) * C**

## **함수**


1.  의약품의 지역별 가중치를 계산하는 함수
    
2.  2018년 의약품의 전국 가중치를 계산하는 함수
    
3.  회귀분석식에 처방건수를 대입하여 계산하는 함수
    
4.  최종 지역별 예상 환자수를 계산하는 함수
    

![](https://lh6.googleusercontent.com/_KHXXmgrtVOxJLva7RbBFpsK13Tr3mZIfheCj-BtCQ9defr0VIMeb5j4fSFtFj40cgQosTAIccVUnCwBiUoxcgn4hi1angABW0ystTT_0vwK0doYdbh08Lii5CbX_fWsCm2o8bKB)

  


## 의약품 처방건수로 관련 질병의 환자수 예측

    

![](https://lh5.googleusercontent.com/fT3ZmWE3IXFn6j4Zz56E8nTeK5efKaysVaQ-pSGwzQ7egHnXt6j3_bo7Rf7s7IfKUR0eUcGOh9iZemBxXLF_7yQUmQXNo1eM81ACIKiePts-TyN-O7W7QoQIa32k-WG6CsvuPODN)

  
  

## 결과
    
	(아래 16지역별 예측결과 순서 : 서울특별시 - 부산광역시 - 대구광역시 - 인천광역시 - 광주광역시 - 대전광역시 - 울산광역시 - 세종특별자치시 - 경기도 - 강원도 - 충청북도 - 충청남도)

1.  **‘428901ATB’ 처방건수로 지역별 급성기관지염 환자수 예측**
    

![](https://lh6.googleusercontent.com/AS6My9Bu7i_3juh8rg8sKSTbHczIBCHmsuL078Q8YQbBCp856B-ALQymLpe0nVXckqghpGhCL3jqi1O3G3QMQvbl6YpQy4W4AzwG49ak89vc5XQos1DRVhfBPU-y9AQjM-zA1-Ct)


![](https://lh3.googleusercontent.com/pQmm_SK9u5Xfsbl2r4YKkPTsuNAS8EZf_Vwp4jcnWh5f-TqgZMqqOAkZj0agJusykkzh-95BPA5RgRwYev2IPg16wyw7ORgwX6f90_Cl5RImxFqS90018vH7Pfyz9bWluxo0eLQ8)


![](https://lh6.googleusercontent.com/22IAc6QjP4miWUJHgPhWQ9BKtoT9f7QKcTzo9GUmtzckAkeUyT5Zrul1teyp91cyfdrMDr2KYmIDBKPDmZtFyjYxTNCH0Yw1snPf6-WSjG99f1ZYOP30ZDzuqzstPDGARMXIJPUA)


![](https://lh5.googleusercontent.com/77BsNzhIGOF113u9Al2JEXJAy7WqbByPKVUtKyxBl9KrjbpaCoTR_8KhLtbTbFVIhQcpZkPBxEYff_yF67dXC8Bb29gIpBfxOVlHnA3afdEMKTOV1zWalFtNIOJjab-DAuGs1Jqq)


  

2.  **‘428901ATB’ 처방건수로 지역별 만성기관지염 환자수 예측**
    

![](https://lh3.googleusercontent.com/jwhWulj-RRplFpOxW70DRF_itf7k3_ZNXMo1Ldn5k8_rLrcg24huXnrMkSUkYpW9Os1spKe1IlX2ocpCNTO3DqpVhiShhjJ4iqYsSCWERgFcFlp905IrsVOwl3MpnLdDoRt5XZAV)


![](https://lh4.googleusercontent.com/lPNMiCoMkyZa4MNHN3eaQT_sQCBkZMcg9GNcanrT1ox6IBCkyEaNYp431Xfp9A4Kavc5mQyJiimDRztEIL2z2YU2RczRc0dfry92yU6KkxlnMo49MM4n87QgOg6kg_Aqf4vnmbV5)


![](https://lh4.googleusercontent.com/AzbhkXdzQMCFbgIi2iF_oKBQEScnMsz0AYDgkR9DmmgZQPOFGrw6ydSMBovPQSlHZEfyonTGB81bULpnMrJmedNhi5qmgbz1PX-H0JwtgEbaQGzvo_NBR7Bf8RTXfGYEIFrNmShs)


![](https://lh5.googleusercontent.com/nSio5dM0OwFckzOQwnDYeqNETVc48DDV3rhljbiKZysMOM_bmw7VjRtrD3mOLvvKlXTlK2bZSYjeB7qP4Ay2R3kOH3AfB1oWgiCNpUdG-7UJw5KWnLyFohYhak6y1Wm2PNBl67zR)


  

3.  **‘220902ATB’ 처방건수로 지역별 만성부비동염 환자수 예측**
    

![](https://lh5.googleusercontent.com/MF9xnl1ZvecDM7XkKWZr0keJBCeJ_zdVqtg1DJ2ddBBWFEMGTBCWgaq8c1EYcOIx4V34fztuT-gt5AUGAWqhXwYFLWoUTlyqpOTEsLyolHLMEJNkPLAMHT09y_2uYizgUwtChV4G)

![](https://lh6.googleusercontent.com/h_MTIjhDUqd3fhj7t6pftx0mJUPI6EkGGtsjAZrECoqOwVLNwke6TQAs64h7iDVqyqDOPF-aF-PrQLYq7b4-wfWt-b0WiLZhJI1YC9CSmODpUqQg6vFBxZ5W7eMPBC2GaFQFdaS0)


![](https://lh6.googleusercontent.com/q-Ce46lkY-ocOJL5d5JwHz0zjCyfJBTLkdHmzIRIkl_TlKzGDbfSoTa_K6XUdf0f3e01H-HFz9w7bxS-JbR_6W-fpewwgdsSCfEnCSv8ekojmXfZolkSWuyqPLdsNY98TvtV0gyC)


![](https://lh6.googleusercontent.com/Y7p5jyjDzoayUDH1nkPlcxrL4ovIZU_y_o9qCcwu0GDqatk2doOyRmqhu4vacqfQ-1D-97HxeuTZ5qK_yDvNERsOSESmJId6aSxBaMjNioWwv3pE0jln94m56W07iQepeaaLNUXl)


4.  **‘220902ATB’ 처방건수로 지역별 알러지성비염 환자수 예측**
    

![](https://lh5.googleusercontent.com/XGurrBWibwIXceGVkF0cBp_VZyD9R4zxd3ZdpZY3v9Zmx8pWf7L37NwcqzlLqd0g_uvgbVZR_CBIca07spA9ypgJ3k_84RcHVpmFE64ERxyRHNB3LOLlvXbFF-bawp7ld0na6_XG)


![](https://lh3.googleusercontent.com/OHeq2cThE-2VB9Hkuw0J_7v-2En6-UxKtpSNbX5weRISY2Nm7nWwYfRMsisvKgvMPGSNXbJgadoNaaUYYFYKUlu7TuyS3CEUch1HGmmB7IiwHQTOHUB_4HBIrRxriDvrFevjmxBe)


![](https://lh6.googleusercontent.com/-1azQr2DX-l_Ctc4fap92-ZXfBbk5tYT5aEr-3-FdPIl8Ak7POQd-KmPSLIMJXHxP5KeHFkdG1BcYWpdmwFDUF4upv5RD_VEAbhJTA_gkTOyLpLokhDMmdeY0hoGnQ7VE3On5iUf)


![](https://lh4.googleusercontent.com/n2G8xkuNuaBBUqtvfmKw-GEJjQhQtFBYrowp9RNeZtqpzDXQX1rVyPFJpUn_sifQ9Lt_EutJNReExsVlOR_FX6dgUfb9CexhYhwPZFdwM50ZvNfyyBQTWGlyamB2mNjSrtmKuqTa)


  

5.  **‘186101ATB’ 처방건수로 지역별 양성 류마티스관절염 환자수 예측**
    

![](https://lh6.googleusercontent.com/iJTXo_vSAgxWVkBVPH18_nig_V6OHwWlAkwMxp8aH9uUm8a8m6sPlGch6gua3lcHcIyJpb9j1CQWRzMTF70PlL4Y-5PflQvksa0ZCR7en05fbhRKG2KgtqMXwqJ3CSUiic1--2cz)


![](https://lh4.googleusercontent.com/PxvrzXLsJte666Re21znAE48CJaf0Jx7KnryFbrEE8zqGtt06YdXeIqTSf1KQubVk-kr7EDkm6Pj8Iz_U6jyEFFKJD64xxWnZFYV2S0ZoV2svv0aMMEZD0mtB_t8ylLqCjrnn2bR)


![](https://lh3.googleusercontent.com/B_rMp3_fiFYcftlJSbyk75R0c7ijtTf4m5G97b9hyDIzlTlYukJiheaSNptql8oa0m_jwAwwFs_MFP8wZwp16GQx-j--fP3P2um99XU7_pk-zNdkYn87VcWb2JFJbVsAfjc6vogQ)


![](https://lh3.googleusercontent.com/Tip1lBnZxR4jBDY1sUI97BZqEP52vbcR__IppaKJQCZj-FAEY4TxvlW8uNtwDmTqMmjKma0HSg0N1ZcWXbt1X67lKbDvBYaiCar6bZ2JtCnOtCkxZQbS-78PG5mjmIbrZfQFH0At)


6.  **‘186101ATB’ 처방건수로 지역별 전립선암(전립선의 악성 신생물) 환자수 예측**
    

![](https://lh5.googleusercontent.com/el5OA_XEtl27D6dQ2ghVMQCq4MLGr95YBPTmENiMSKCYJMqA3tO3qPFcDWD71BETCqq191crLkCoVgYBI2_doE_FRdLLkjrd8QvXXaddEoDICAmj_cit8gVcfd5ZZrYe1VnWxjW1)


![](https://lh6.googleusercontent.com/be48xfvgYp3lGS7svXxDzYVIgEyBstkWaD6U5uD4DHcb1ERTJSMLxyvCwv_El1Z2KNHqqe1m-dT-psnRq0q2YFgketB0vF-Fq3eG9OZvb6YhffEgno7kybp8i5ETMGG4bzkLWyWs)


![](https://lh5.googleusercontent.com/IUS4Y3zlgjoip78qK_0rb--GFbrnuCFnrAh3UZ6vpy15_rvB_xB8qPx4VmnIk0diL9Q010n-PZ5c3LAm2GaHiSSpXviN0ouLYx1avhO3ThPC3J5kNtZZTE0J3LPDpzzsDuPM-PgO)


![](https://lh5.googleusercontent.com/4ho-vVrf90SyuPpD7cCD8ZnBS5xmchDz9zlVpOaFD_wPJ4raeQXUBIElcFcxGeWaCtaT8h-XJWpperaSsBEeUcVN7ESLyFBcZAp95HIBAEXHMAef0EKVkH9JxWBuidr0QDoN7jd6)


  

7.  **‘186101ATB’ 처방건수로 지역별 폐암(기관지, 폐의 악성신생물) 환자수 예측**
    

![](https://lh6.googleusercontent.com/ul9RtvmG3hWudy11Tab3qxs4bGNXu0pc8Q4V56xzGf4cDBx3e0iB3Czy_MgrlIDF4GmfzAVzAzk9AiMIyQHsm51DqTdPr7lEmh8aJ4DH4qZKD8rK5B6GXuL0LBWZOYNIpCQIl6_P)


![](https://lh5.googleusercontent.com/bO4Kbjo8SqRZxxxYD443EUP7rdkGqSOM1LHrYK_MuQgkYGK8z93kPfCpmYmhNxUqFpX9Kdrvn96xXE24BOG5Ra9AyOs02KwQxxVPkY_AgQJEtRnFXBrXSsF_pP8nlGeDe9kiyQzz)


![](https://lh4.googleusercontent.com/FxJvLTBR8VMPTsJztCrdV1wgXZnorJCUHLvRYgrROxEcu3z5X0BQZXsnqYwjOxf_LU5iMfRQHZRJAnLzMaHHtPLyTojC4ukfoS2ilTASjrX0oyht5zgEUPjNccWv2Z6v5N3Ln_pZ)

![](https://lh3.googleusercontent.com/IAl46SQGZOLHLX2d0cOLUEZi6X5OHZmjIom2C9pzWA1XX37ex9JK5zlbbAK633ZFnEqmxT6WZFaRfnGy3fpJICp0b0VVtpka0MNgYCHlPFOntfRgHCCw1ptPiREGa_XN0rFkV_fX)


  

8.  **‘421001ATB’ 처방건수로 지역별 구역 및 구토 환자수 예측**
    

![](https://lh5.googleusercontent.com/Rv-vCaw4HkDweGtJwy2BC5i_7dj9uJfNNJDhgPXTH8BuJFXbXa-bZXnPjrPBwEbegnQsEGnw1IaHj1klNXkL2et0vwA1Yiz0WcUm2z5DBDJa-3-KX4tI-fpYKlNxd3MKjNyOKmxa)


![](https://lh4.googleusercontent.com/Jqkj_37gi8hMXEy8RxkumYcCLJ-JYkJySp9Qj3b6ppKX5qsQwSTZkICu0oO6a50K9qKOJdiSj-uyb6NH7MZrzrukTobLDMPPiMNThphT0OtnO0Uart58kLmhyqOXC2-y7G6CYBEk)


![](https://lh3.googleusercontent.com/HvcRhJKIfyHnh0_RiKI0zE-YHm9g2XluvNrWSHvwQFh4c8yQE67RKh9th2DjCVmFduA3HCIpvI4k0lI4Gnuo39OiPipNHI5t7BxXKPZXa0jv21au3-IawBZthoiXyfHzsHsjUhPk)


![](https://lh3.googleusercontent.com/E4ShEkedz4s7QPgAVse0-jRpeJEDB0GHQ61X4V8MYnPvZzyAiLJqwVGHYQ-sRRCfJSY4hgFaRa-5QzJvzABKXtKUbrIoIjhH6g_EhwzJ1p-QZF_vsb0U0v8x9c0RLmWhttxLae27)


9.  **‘133301ATB’ 처방건수로 지역별 위궤양 환자수 예측**
    

![](https://lh4.googleusercontent.com/uVW8EkdlF7h6gUz6dtY6pxLWr9_MZ6pXy9IqtgpntuT2UXNv2lpnuC3Yx0eRlP2OcyXzzu4wU_vt_rd5i_CbjfK3Xydw5hRk3XI3kPfp81f4WbkcaTvqepu5FI1Y_otjmrtEfr_b)


![](https://lh5.googleusercontent.com/l1HNKDg27mMnoJXkWjiR7Hg30CwQk9eDgLoI2GKKZ0MX8g6lzHI7KVb2_XhDOOx83nziwhgl9W39dnPuOvn2IdrR8gBTgGjt-JhqoDndj8bL7t0fErs8c6Gtg2n6zW0UK-EiUzqy)


![](https://lh6.googleusercontent.com/EbnLUegTHVbzb3YEJCVF4Et2iFVEVg5esJicoIbVQbqacXfNvB8xdqi8TsN3bodnuOkrFrhN37zn8256r5NRD2hTApmPfF81Md222vLMKeRsierqOwWAQTxZ3FIlv3rPXdpha6xs)


![](https://lh5.googleusercontent.com/9_DxIQlGhKwjR-4IkBH0yuo4Zrm54VFABgVtMWQTEkQe-5RfChS5zz4NIW3VqFM5MLkVOtDA6CtndDtyTLV2Fc9S_gbQI2SPktrUfTfKuqF4XCdTk3xAiR5uNE8xD-nXC6s84rN3)


  

10.  **‘133301ATB’ 처방건수로 지역별 십이지장궤양 환자수 예측**
    

![](https://lh5.googleusercontent.com/_v2mpa-IMx3J78QXeaqdNnvPYQJutm9XuL_53aDsxBKXOZTuf_51S582fjtw_Cppbard4yjWN9PNMIKgz82nm9e7goHd7PQ5qXbQ80ZGjVAOs5JFEyDNu_mBJSgPWfwO5xFT7Orh)


![](https://lh3.googleusercontent.com/QIOybs_r5mG0B5v4u-KNCUhFLt_quWGyIg5yXEys5-bIgemzP2PP4bHns_nsgu4Sg-gNrS07GKZmKOn5n_MzXFkjKjm7vtZwXqzTz5lbtOsM6UxswP8X1YzZoFqvi-2fhUNZ2lfw)


![](https://lh3.googleusercontent.com/DwvSOJRG8NdFxLNbayAdYWJmOtEgHTt5x6G8N1wmnyttJG9jGKgbXKhyfW67mKsmocGIqNu7tDr0sTOjXXaghilVRUR1xyabJENiLtYccKQY62R6FeVgLucRJ-AhbSYlOajlH7KR)


![](https://lh3.googleusercontent.com/YWnsKsHhos06IcgTbMtGunJnpaeGqFZtyd23Ex6ponEfy8L__MtTUZMr9WNAGq2nj4Cpa5tiieIpHrAFRAGE8Rk8QwFD9ChNdghxlq9VgdbUqZx51hSdruvMLsWFpFDnbQN9yJFl)

  

11.  **‘271800ATB’ 처방건수로 지역별 위-식도 역류병 환자수 예측**
    

![](https://lh6.googleusercontent.com/8KYoJ7FSVmGiZ8-oC0TvV7zG6opN5QvWjO4JMqRdu3l1JMSSBYjlCFJ0MWbl4Tp9YsJDF7QkEsIp_0jq7U4ITuT_B_WJAHHwzZpH42NrSC9leFJtdzIbd44YUhIdoGWRELjhT0PG)


![](https://lh4.googleusercontent.com/PgIaeq86virD5biCc3LXZ7tQnmsbJUpR_3_x47EZehmUl0Atkl3vN16GnTV3lXLHOdvopFoaNykKGTELn91KaMyPFmul0yt_oNHch8yAl_0hZmrylHwhrXkMZ1zq8r2b94UjsGJX)


![](https://lh5.googleusercontent.com/5ehFlrTltPujCT9rQxEZBeS2MCLuSqGdznlhtsG6OfWIPThdT_V_c0czdqCE5OqHWvejaVkOVJYbCH4USDOfUA_58BDJJq_8APCb-jsgXLsJDGDcQryUksoGkgLugIjzk1z6fBZU)


![](https://lh6.googleusercontent.com/Xz5smnImTAHdHmvsOqOcC5OAgdgSDIAg91qgw5WWwBJqvlDemXddh-Y7AX7kcEjeWJ7nAtfkDcOQG-MeAW-I6LJStNcBqQZMvbWXdNzvN0vNSxSluOJudPwP3Gm2TLoi34duzOfK)



# **지역별 위험도 산출**



## **2018년 지역별 예상 환자 수 기반 위험도 예측**

1.  **방법**
    

-   예상 위험도는 다른 지역과 비교하여 ‘경미’, ‘보통’, ‘주의’의 3가지 수준으로 나누어 산출한다.
	- **경미** : 지역별 환자수의 평균과의 지역별 환자수의 오차의 평균보다 훨씬 큰 수치로 예상 환자수가 현저히 낮을 때
	- **보통** : 지역별 환자수의 평균과의 지역별 환자수의 오차의 평균과 비슷한 수치의 예상 환자수일 때
	- **주의** : 지역별 환자수의 평균과의 지역별 환자수의 오차의 평균보다 훨씬 큰 수치로 예상 환자수가 높을 때
    

  

2.  **결과**
    

※ 예상 환자수는 결과의 소수점 첫째자리에서 반올림하여 산출하였음

a.  ‘428901ATB’ 처방건수로 예측한 지역별 급성기관지염 환자수에 따른 위험도
![](https://lh5.googleusercontent.com/zXhh_HYojY0DBU8Wtd2HbtDiDPdkL95n2Rg2rRdLrrhrwxVJNqWjejt-JnRKIkILqWjihyKDh7sC1gUUq5GLPqGqKSPRoLpuJ-4eHWNZnvelp1fSL4AEgd823nyerMkk-MXim0HD)

b. ‘428901ATB’ 처방건수로 예측한 지역별 만성기관지염 환자수에 따른 위험도
**![](https://lh3.googleusercontent.com/N5zZUAL4keGHnVC7JX6p5wSIWgU5N_D1Y1XqC2XrIpVaWXEC5hhizJI2Z9bwKHq-xvy-J4LAHvTv_ZvR2BqhrbsuIP8XJ7_oT7ZYgcAYoFKtz2e-kExrmi-RppKDdKCPsZE8TlI6)**
c.  ‘220902ATB’ 처방건수로 지역별 만성부비동염 환자수 예측
**![](https://lh4.googleusercontent.com/-IbbwByVjNaGDhBpiBGaz6Cbb0F1aaxe9EznomTo79_eErlgrf_4_ug_NuThYs84JUUCcThMCNygnIpnry7OeMGT6LR18EqF8X3kC_e2v_SqcAPGaL7mWckDsw2uOOa3E2pLkbke)**
d. ‘220902ATB’ 처방건수로 지역별 알러지성비염 환자수 예측
**![](https://lh4.googleusercontent.com/F-NwK4YI4MTdCHyrU-5XvTFKewATrXbizBBKALu1wDv89MrsUV_w1WWTxTA5cfHf4jUSY2pH2vWUFGDEemC5i8iGiPc56HmmSybAkFOqAL8IssHYH7RjyHztgsayXRZF-iwl5zEh)**
e.  ‘186101ATB’ 처방건수로 지역별 양성 류마티스관절염 환자수 예측
**![](https://lh4.googleusercontent.com/l7j4YnYC_Jl_HI1k-HoDb15tMooALjf58ItxQqbeT0iv9Hv0Gb-YreNZe2lXSZKl5677nvmV51TBPb7YHR4IPSf2CGNwwbcizJsn6RN67DhSpwJx-gX-wkdtnTrk08UaP1wMHbjG)**
f.  ‘186101ATB’ 처방건수로 지역별 전립선암(전립선의 악성 신생물) 환자수 예측
**![](https://lh5.googleusercontent.com/SiDdQqKY0y3fi8Di6wcvYmJnbDVv33f1GZOmJ8ldEj3TtAgTJ0k4veaCCistghD4cDyjTPyn72aqnfejWhYsM5Qdp28_amLZZsMDCYUWbBsc8-d8ZFYUZRFlaG9nzXN2qImW3R-b)**
g.  ‘186101ATB’ 처방건수로 지역별 폐암(기관지, 폐의 악성신생물) 환자수 예측**![](https://lh3.googleusercontent.com/cHRJSbpkbvefP5iJiRQmmCeHa7jGLsoeK3jOgQivl8aTJdidQbTOyomxKC7lkcYJxbauv8XYBnQaBNe8J1K7oar5iaBD2BxkNysbn8OVnO-MMOWOqQcnZaEfSP2iqHJP7SyMqPuN)**
h.  ‘421001ATB’ 처방건수로 지역별 구역 및 구토 환자수 예측
**![](https://lh5.googleusercontent.com/U1EwqdU0K2n6sdKKkGOraA0R7V4NfVhfJ1BYSOTYpp4gNtENyCWMD4sb1hKmCjP3AofbmBpKqSWehR4j0jxepnQlWWqvDMxowVSdO4bLIpOmDjM3i5glXS06n1mPx4eXjUP1BINj)**
i.  ‘133301ATB’ 처방건수로 지역별 위궤양 환자수 예측**![](https://lh6.googleusercontent.com/DydeoO0MAncZUlsEbtF7RwYhFFkggEFM617xwz1uLos-TZigcVHbVWH6ES230BhIt7SoXUOpHZyk0voNIl1Im74ZNEkikSfGjvVtYpxvTXa7zNScD6wAdy5XdU0BXbWZ8MUG8FFe)**
j.  ‘133301ATB’ 처방건수로 지역별 십이지장궤양 환자수 예측**![](https://lh4.googleusercontent.com/aW-wX3pntV-3o4MJo4Ostedosq9WulJPAJu0C2ug4NM8bT_mzmC98puxgY_aPVX0fUeH-o8hvd43-jB1KrZlb-ETAR1x0BlCHCG1XffRHzFbGjYKaa2iLbV1TXfOU34kfQGE94P3)**
k.  ‘271800ATB’ 처방건수로 지역별 위-식도 역류병 환자수 예측**![](https://lh3.googleusercontent.com/O71Y2GfWABBB1FVYl7uZqokBRy742gfQS0ZhwLYzhN-xGugfLxZAcmxKJfqAefD3fHJRUTOXKnwQIFxWZfP7g9-ugLmKpCRxkuOOCTL-hUkHdpIph9aTgf0QfMdmUv3lcDlkyFvs)**

# 참고문헌
이상용. (2016). 의약품처방정보 공공데이터 분석을 통한 충북의 특성 및 시사점. 충북 FOCUS(120), 1-22
