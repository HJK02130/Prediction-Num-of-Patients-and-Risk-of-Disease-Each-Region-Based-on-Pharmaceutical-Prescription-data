# <div align=center> A Prediction of Number of Patients and Risk of Disease <br/> in Each Region Based on Pharmaceutical Prescription Data </div>

<div align=right> <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/HJK02130/Android-App-That-Recommends-Computer-Science-Lecture-Videos?style=flat-square"> <img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/HJK02130/Android-App-That-Recommends-Computer-Science-Lecture-Videos?style=flat-square"> <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/HJK02130/Android-App-That-Recommends-Computer-Science-Lecture-Videos?style=flat-square"> </div>


### Contents
1. [Overview](#overview)
2. [Requirements](#requirements)
3. [Languages and Development Tools](#languages-and-development-tools)
4. [Architecture](#architecture)
5. [Repository Explaination](#repository-explaination)
6. [Result](#result)
7. [Conclusion](#conclusion)
8. [Reference](#reference)
9. [Developer](#developer)


### Overview

In the news and various materials, the number of patients with a specific disease by region is statistical data from national health examination data. And it is not accurate data because not only the entire population does not participate, but also only those over a certain age regularly participate. In addition, there are many statistics on the number of patients divided by age, sex, etc., but statistics on the number of patients divided by region can only be found about the most common diseases.<br/><br/>

In this study, we predict the number of patients by region in 2018 for specific diseases. In addition, based on the number of analyzed patients, we predict the risk of occurrence of the disease by region and derive implications for the risk of the disease by region. For data analysis, we used drug prescription data from 2010 to 2017 of Korea, and predict the number of patients by region applying the 2018 drug prescription data through correlation analysis and regression analysis.<br/><br/>
  
First, we figure out the degree of association between a specific drug and various diseases for which the drug is effective through correlation analysis using Pearson's correlation coefficient. Thereafter, we obtain a linear regression equation that calculates the expected total number of patients with a disease highly related to the corresponding drug based on the number of prescriptions for the drug through a linear regression analysis between drugs and diseases with a high degree of relatedness. Finally, we substitute the number of drug prescriptions in 2018, the most recent data, into the linear regression equation and predict the number of patients with specific diseases in 2018 by region using a specific weight concept. Also we calculate the disease risk obtained by comparing with other regions.<br/><br/>
  
뉴스 및 각종 자료의 지역별 특정 질병의 환자 수는 국민건강검진자료로부터 통계된 자료로, 온 국민이 참여하지 않을 뿐더러 특정 연령 이상만 정기적으로 참여하기 때문에 정확한 자료가 아니다. 또한, 연령, 성별 등을 기준으로 나뉘어진 환자 수 통계는 많이 있지만, 지역을 기준으로 나뉘어진 환자 수 통계는 흔한 질병의 자료만 찾아볼 수 있다.<br/><br/>

본 연구에서는 특정 질병들의 2018년 지역별 환자 수를 예측한다. 또, 분석한 환자 수를 바탕으로 해당 질병에 대한 발생 위험도를 지역별로 예측하여 지역별로 질병에 대한 위험도의 시사점을 도출한다. 데이터 분석을 위해 대한민국의 2010년에서 2017년까지의 의약품 처방 데이터를 기반으로 상관분석과 회귀분석을 통해 가장 최근 데이터인 2018년 의약품 처방 데이터를 적용시켜 지역별 환자 수를 예측한다.<br/><br/>

상관분석과 회귀분석을 이용하여 결과를 도출하는 방법은 다음과 같다. 먼저, Pearson 상관계수를 이용한 상관분석을 통해 특정 의약품과 해당 의약품이 효과를 발휘하는 여러가지 질병들과의 연관된 정도(r)를 파악한다. 이후 연관된 정도가 높게 대응되는 의약품과 질병끼리의 선형회귀분석을 통해 의약품 처방건수를 바탕으로 해당 의약품과 연관성이 높은 질병의 예상 총 환자수를 산출하는 선형회귀식을 얻는다. 선형회귀식에 가장 최근 데이터인 2018년도 의약품 처방건수 데이터를 대입하고 가중치 개념을 도입하여 2018년 지역별 특정 질병들의 환자수를 예측하고 마지막으로 다른지역과 비교하여 얻어진 질병 발생 위험도를 산출한다.

### Requirements
+ Python 3.6

### Languages and Development Tools
<img src="https://img.shields.io/badge/Python-3766AB?style=flat-square&logo=Python&logoColor=white"/> <br />
<img src="https://img.shields.io/badge/Google Colab-F9AB00?style=flat-square&logo=GoogleColab&logoColor=white"/> <img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=VisualStudioCode&logoColor=white"/>

### Architecture
[📑 Here is Detailed Project Description]()
<div align=center>  <img src="./img/architecture.png"> </div>

### Repository Explaination
###### 📄 correlation.py<br/> Correlation analysis between medicine and disease
###### 📄 preprocessing.py<br/> Data preprocessing
###### 📄 prediction.py<br/> Prediction of the number of patients by disease using linear regression and weight formula
###### 📄 regression.ipynb<br/> Regressiong analysis for prediction of the number of patients using 
###### 📄 transformation.py<br/> Data transforming

### Result
[📽 Here is Application Demo Video](https://drive.google.com/file/d/1SLPcyupCKiRhhxkCYXfACbGaBZ4pzmKs/view?usp=share_link)
#### Video Based Recommended list
<img src="./img/result1.png">

#### User Based Recommended list
<img src="./img/result2.png">

#### My Page
<img src="./img/result3.png">

### Conclusion
In the recommendation system, we implemented a total of three recommendation systems: content-based, association rule-based, and thumbnail image-based. Unlike existing YouTube, the recommendation system has been diversified, and users can check the system.<br/></br>
Also, This application was developed by interconnecting three: python-firebase-flutter. It's rarecase in which all these three are linked, and since all are free distribution, it is meaningful in that reduced development costs.<br/><br/>
By implementing text summarization, it not only provides users with a simple YouTube video viewing platform, but also provides video summary information. It is meaningful in that it provides additional information for selection, not just video recommendation, to a user who selects a video to watch for learning purposes.<br/><br/>
The application created through this project is expected to increase added value and build a new learning platform by contributing close to the essence of shared content. In addition, based on the above, it is expected to create a new market for low-cost app development that links three tools using free distribution tools and sources. Lastly, if the scope is expanded to parascience and medical science, it is expected that students from socially disadvantaged classes will be able to study by finding high-quality lecture contents.

### Reference
이상용 . (2016). 의약품처방정보 공공데이터 분석을 통한 충북의 특성 및 시사점. 충북 FOCUS, 120, 1-22.

### Developer
Hyunji Kim
<br />
Hyunji Kim's <a href="mailto:hjk021@khu.ac.kr"> <img src ="https://img.shields.io/badge/Gmail-EA4335.svg?&style=flat-squar&logo=Gmail&logoColor=white"/> 
	<a href = "https://github.com/HJK02130"> <img src ="https://img.shields.io/badge/Github-181717.svg?&style=flat-squar&logo=Github&logoColor=white"/> </a>
