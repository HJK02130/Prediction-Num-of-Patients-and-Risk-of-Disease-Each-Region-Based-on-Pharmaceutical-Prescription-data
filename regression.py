
### 아래는 의약품 271800ATB과 '위-식도 역류병' 간 회귀분석 ###

from sklearn import linear_model
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')

data = {'medicine': [5829, 7190, 13719, 15174, 17232, 27795, 33590, 37009+18422],
        'paitient': [2847763, 3107033, 3378715, 3533638, 3635931, 3873549,
       4179510, 4287987]}
data = pd.DataFrame(data)
print(data)

data.plot(kind="scatter", x="medicine", y="paitient", figsize=(5, 5), color="black")

linear_regression = linear_model.LinearRegression() # 선형회귀모델
linear_regression.fit(X=pd.DataFrame(data["medicine"]), y=data["paitient"])  # 모델 학습
prediction = linear_regression.predict(X=pd.DataFrame(data["medicine"]))     # 예측한 환자수
print('a value = ', linear_regression.intercept_)   # 회귀식의 절편
print('b value = ', linear_regression.coef_)        # 회귀식의 기울기
# 회귀식
print('y(환자수) =', linear_regression.coef_, "x(처방건수) + (", linear_regression.intercept_, ")")

#  적합도 검증
residuals = data["paitient"] - prediction
residuals.describe()

SSE = (residuals**2).sum()
SST = ((data["paitient"]-data["paitient"].mean())**2).sum()
R_squared = 1 - (SSE/SST)
print('R_squared = ', R_squared)

data.plot(kind = "scatter", x = "medicine", y = "paitient", figsize = (5, 5), color = "black")

#  선형회귀선
plt.plot(data["medicine"], prediction, color="red")
plt.show()
