# <div align=center> A Prediction of Number of Patients and Risk of Disease <br/> in Each Region Based on Pharmaceutical Prescription Data </div>

<div align=right> <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/HJK02130/Android-App-That-Recommends-Computer-Science-Lecture-Videos?style=flat-square"> <img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/HJK02130/Android-App-That-Recommends-Computer-Science-Lecture-Videos?style=flat-square"> <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/HJK02130/Android-App-That-Recommends-Computer-Science-Lecture-Videos?style=flat-square"> </div>


### Contents
1. [Overview](#overview)
2. [Requirements](#requirements)
3. [Languages and Development Tools](#languages-and-development-tools)
4. [Issue](#issue)
5. [Usage](#usage)
6. [Architecture](#architecture)
7. [Repository Explaination](#repository-explaination)
8. [Result](#result)
9. [Conclusion](#conclusion)
10. [Reference](#reference)
11. [Developer](#developer)


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

### Issue
+ make_video.py is being modifyed.

### Usage
Filetree (modifying)

### Architecture
[📑 Here is Detailed Project Description]()
<div align=center>  <img src="./img/architecture.png"> </div>

### Repository Explaination
###### 📁 sdsapp<br/>Developed application folder. mainapp.dart is a main dart file.<br/>
###### 📁 data_aquisition<br/>Data collecting code using YouTube Data API
> ###### 📁 csv<br/>Total data collected by category. Data such as search, title, number of views, and number of likes.
> ###### 📁 videos<br/>Metadata for each video (.json)
> ###### 📁 subtitles<br/>Subtitle data of lecture video obtained using youtube-transcript-api
> ###### 📁 data<br/>Summarized subtitle data (.json, .csv)
> ###### 📄 make_recommendation.py<br/>The code that stores a list of recommendations by category
> ###### 📄 make_video.py<br/>The code that stores metadata and recommendation list for each video
> ###### 📄 summarize.py<br/The code that summarizes and saves the saved subtitle data
> ###### 📄 SDS_content_based_recommendation.ipynb<br/>The code that saves a recommendation list using content based recommendation per videoID based on title
> ###### 📄 maketsne.py<br/>The code that reduces the dimension of an image thumbnail to tsne and saves it

###### 📁 firestore<br/>Data for uploading data to the Firebase Firestore database and node.js project files 
> ###### 📄 video.json<br/>Metadata of each video and recommended list information for each video
> ###### 📄 user.json<br/>The video ID information of the video watched and liked by the virtual user using the app.
> ###### 📄 recommendation.json<br/>The number of views, number of likes, and recently uploaded video recommendation list for each category.
> ###### 📄 index.js<br/>The code to upload the above files to the Firestore database. In the firebase.initializeApp() function, you must enter the value of the API key assigned to each of you.


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
+ Bae, J.-H., & Shin, H.-Y. (2020). 대학교육의 질 제고를 위한 이러닝 활성화 방안 연구: 유튜브 러닝 콘텐츠 사례를 중심으로. 한국융합학회논문지, 11(7), 309–317. https://doi.org/10.15207/JKCS.2020.11.7.309
+ BAher, S., & L.M.R.J., L. (2012). Best Combination of Machine Learning Algorithms for 3Course Recommendation System in E-learning. International Journal of Computer Applications, 41(6), 1–10. https://doi.org/10.5120/5542-7598
+ Chtouki, Y., Harroud, H., Khalidi, M., & Bennani, S. (2012). The impact of YouTube videos on the student’s learning. 2012 International Conference on Information Technology Based Higher Education and Training (ITHET), 1–4. https://doi.org/10.1109/ITHET.2012.6246045
+ Covington, P., Adams, J., & Sargin, E. (2016). Deep Neural Networks for YouTube Recommendations. Proceedings of the 10th ACM Conference on Recommender Systems, 191–198. https://doi.org/10.1145/2959100.2959190
+ DeWitt, D., Alias, N., Siraj, S., Yaakub, M. Y., Ayob, J., & Ishak, R. (2013). The Potential of Youtube for Teaching and Learning in the Performing Arts. Procedia - Social and Behavioral Sciences, 103, 1118–1126. https://doi.org/10.1016/j.sbspro.2013.10.439
+ Hidalgo, E. A., Tehas, F. S., & Magana, S. de M. (n.d.). MushroomApp: A Mushroom Mobile App. 18.
+ Jaffar, A. A. (2012). YouTube: An emerging tool in anatomy education. Anatomical Sciences Education, 5(3), 158–164. https://doi.org/10.1002/ase.1268
+ Moon, E.-M. (2019). An Analysis on YouTube Contents to Build E-learning Videos for Interior Design Education. Journal of the Korean Institute of Interior Design, 28(6), 41–50. https://doi.org/10.14774/JKIID.2019.28.6.041
+ Nasar, Z., Jaffry, S. W., & Malik, M. K. (2019). Textual keyword extraction and summarization: State-of-the-art. Information Processing & Management, 56(6), 102088. https://doi.org/10.1016/j.ipm.2019.102088
+ Yoo, T., Jeong, H., Lee, D., & Jung, H. (2021, April). LectYS: A System for Summarizing Lecture Videos on YouTube. In 26th International Conference on Intelligent User Interfaces (pp. 90-92).
+ Van der Maaten, L., & Hinton, G. (2008). Visualizing data using t-SNE. Journal of machine learning research, 9(11).
+ https://ko.wikipedia.org/wiki/%EC%BD%94%EC%82%AC%EC%9D%B8_%EC%9C%A0%EC%82%AC%EB%8F%84
+ https://en.wikipedia.org/wiki/Apriori_algorithm

### Developer
Hyunji Kim, Taewon Yoo, Hyunjin Jeon.
<br />
Hyunji Kim's <a href="mailto:hjk021@khu.ac.kr"> <img src ="https://img.shields.io/badge/Gmail-EA4335.svg?&style=flat-squar&logo=Gmail&logoColor=white"/> 
	<a href = "https://github.com/HJK02130"> <img src ="https://img.shields.io/badge/Github-181717.svg?&style=flat-squar&logo=Github&logoColor=white"/> </a>
