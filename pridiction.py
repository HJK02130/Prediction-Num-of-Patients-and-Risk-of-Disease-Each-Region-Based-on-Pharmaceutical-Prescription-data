
### 질병별 지역별 환자수 예측 ###
### 순서 : 서울특별시, 부산광역시, 대구광역시, 인천광역시, 광주광역시, 대전광역시,
###       울산광역시, 세종특별자치시, 경기도, 강원도, 충청북도, 충청남도, 전라북도,
###       전라남도, 경상북도, 경상남도

# 의약품의 지역별 가중치 계산
def cal_WeightOfPerCity(part1, part2, part3, pop):
    sumLst = []
    WopcLst = []
    for i in range(16):
        sum = part1[i] + part2[i] + part3[i]
        sumLst.append(sum)
        sum = 0
        wopc = sumLst[i] / pop[i] * 100
        WopcLst.append(wopc)
    return WopcLst

# 의약품의 전국 가중치 계산
def cal_MonthlyTotalWeight(WopcLst):
    sum = 0
    for i in WopcLst:
        sum += i
    return sum

# 회귀분석 결과로 나온 예상 환자수의 1% 계산
def cal_OnePercentPatients(a, x, b):
    Opp = (a * x + b) / 100
    return Opp

# 위 계산값을 입력으로 한 최종 지역별 환자수 산출 함수
def prediction(wopcLst, sum, opp, preList):
    for i in wopcLst:
        prdct = (i / sum) * 100 * opp
        preList.append(prdct)
        prdct = 0

top1part1 = [6462, 2701, 1620, 2303, 1238, 1552, 757, 225, 9727, 1118, 1452, 1991, 1814, 1405, 1846, 2426]
top1part2 = [6477, 2233, 1435, 2368, 1113, 1501, 853, 264, 9992, 955, 1605, 1965, 1588, 1408, 1776, 2482]
top1part3 = [6479, 2479, 1574, 2260, 1038, 1350, 890, 282, 10180, 957, 1478, 1876, 1739, 1659, 1994, 2531]

top2part1 = [4747, 1668, 928, 1360, 884, 813, 422, 260, 7467, 641, 774, 1014, 693, 777, 926, 1487]
top2part2 = [4505, 1333, 721, 1689, 890, 860, 495, 264, 7777, 627, 1027, 1071, 807, 837, 946, 1812]
top2part3 = [4830, 1385, 987, 1473, 713, 834, 603, 241, 8307, 521, 806, 1070, 895, 781, 929, 1574]

top3part1 = [4573, 1866, 1604, 1663, 677, 994, 749, 191, 6433, 695, 1213, 1326, 1017, 1134, 1575, 1697]
top3part2 = [4902, 1597, 1344, 1603, 643, 931, 805, 172, 6281, 717, 1224, 1305, 942, 1046, 1777, 1786]
top3part3 = [4919, 1728, 1530, 1595, 583, 799, 801, 184, 6531, 701, 1168, 1101, 1109, 1226, 1518, 1852]

top4part1 = [4067, 1882, 1274, 1464, 556, 815, 554, 140, 5254, 593, 866, 1166, 894, 1028, 1250, 1629]
top4part2 = [3840, 1814, 1241, 1384, 534, 893, 623, 104, 5337, 447, 992, 1127, 962, 856, 1385, 1930]
top4part3 = [3983, 1858, 1172, 1246, 477, 759, 580, 140, 5385, 463, 944, 1011, 877, 903, 1355, 1660]

top5part1 = [4132, 1580, 1323, 1398, 847, 770, 475, 138, 5303, 680, 856, 1118, 1424, 1165, 1475, 1527]
top5part2 = [3930, 1486, 1267, 1346, 880, 745, 528, 111, 5330, 688, 968, 1086, 1411, 1201, 1594, 1618]
top5part3 = [4327, 1506, 1395, 1305, 801, 699, 510, 172, 5254, 589, 795, 943, 1474, 1204, 1622, 1557]

top6part1 = [2557, 1093, 706, 757, 413, 476, 260, 78, 3480, 323, 400, 510, 582, 623, 653, 864]
top6part2 = [2749, 1132, 636, 765, 439, 480, 338, 71, 3348, 442, 425, 587, 702, 651, 762, 965]
top6part3 = [2781, 977, 755, 730, 394, 509, 354, 63, 3462, 397, 430, 444, 611, 619, 691, 896]

top7part1 = [2184, 1124, 751, 718, 371, 470, 327, 89, 3211, 382, 471, 507, 604, 464, 674, 914]
top7part2 = [2304, 893, 704, 709, 388, 456, 406, 125, 3343, 452, 480, 574, 584, 567, 797, 1071]
top7part3 = [2435, 1249, 777, 706, 369, 396, 383, 88, 3403, 358, 405, 545, 537, 475, 740, 983]

top8part1 = [1506, 823, 571, 441, 351, 293, 205, 63, 2195, 216, 396, 410, 320, 472, 457, 728]
top8part2 = [1798, 743, 441, 472, 373, 315, 252, 61, 2253, 229, 423, 390, 385, 424, 700, 741]
top8part3 = [1719, 691, 459, 434, 244, 296, 216, 48, 2123, 237, 430, 321, 425, 421, 620, 688]

top9part1 = [3554, 1322, 1007, 1025, 703, 629, 353, 105, 4605, 800, 508, 1117, 857, 997, 1052, 1609]
top9part2 = [3463, 1291, 944, 1098, 674, 692, 482, 92, 4998, 610, 581, 1123, 815, 964, 1138, 1703]
top9part3 = [3503, 1380, 1031, 1197, 640, 540, 453, 133, 4748, 725, 590, 885, 832, 1088, 1157, 1687]

pop = [9673936, 3395278, 2444412, 2936117, 1490092, 1511214, 1150116, 312374, 13103188, 1520391, 1620935, 2181416, 1818157, 1790352, 2672902, 3350350]

# 1 - 급성기관지염 0.81
preList = []
wopcLst = cal_WeightOfPerCity(top1part1, top1part2, top1part3, pop)
sum = cal_MonthlyTotalWeight(wopcLst)
opp = cal_OnePercentPatients(64.264080318, 38637+38015+38766, 9139314.477)
prediction(wopcLst, sum, opp, preList)
print("1 - 급성기관지염 0.81")

# 1-만성기관지염 0.62
print(preList, '\n')
preList = []
wopcLst = cal_WeightOfPerCity(top1part1, top1part2, top1part3, pop)
sum = cal_MonthlyTotalWeight(wopcLst)
opp = cal_OnePercentPatients(0.70605659, 38637+38015+38766, 328852.60620221513)
prediction(wopcLst, sum, opp, preList)
print("1-만성기관지염 0.62")
print(preList, '\n')

# 2-만성부비동염 0.77
preList = []
wopcLst = cal_WeightOfPerCity(top2part1, top2part2, top2part3, pop)
sum = cal_MonthlyTotalWeight(wopcLst)
opp = cal_OnePercentPatients(5.3969381, 24861+25661+25949, 1839775.6078401387)
prediction(wopcLst, sum, opp, preList)
print("2-만성부비동염 0.77")
print(preList, '\n')

# 2-알러지성비염 0.84
preList = []
wopcLst = cal_WeightOfPerCity(top2part1, top2part2, top2part3, pop)
sum = cal_MonthlyTotalWeight(wopcLst)
opp = cal_OnePercentPatients(31.6859374, 24861+25661+25949, 4540199.553023627)
prediction(wopcLst, sum, opp, preList)
print("2-알러지성비염 0.84")
print(preList, '\n')

# 3-양성류마티스관절염 0.81
preList = []
wopcLst = cal_WeightOfPerCity(top3part1, top3part2, top3part3, pop)
sum = cal_MonthlyTotalWeight(wopcLst)
opp = cal_OnePercentPatients(0.83643518, 27407+27075+27345, 53965.65085582699)
prediction(wopcLst, sum, opp, preList)
print("3-양성류마티스관절염 0.81")
print(preList, '\n')

# 3-전립선의 악성 신생물 0.86
preList = []
wopcLst = cal_WeightOfPerCity(top3part1, top3part2, top3part3, pop)
sum = cal_MonthlyTotalWeight(wopcLst)
opp = cal_OnePercentPatients(1.02945098, 27407+27075+27345, 14685.96133503622)
prediction(wopcLst, sum, opp, preList)
print("3-전립선의 악성 신생물 0.86")
print(preList, '\n')

# 3-기관지 및 폐의 악성신생물 0.83
preList = []
wopcLst = cal_WeightOfPerCity(top3part1, top3part2, top3part3, pop)
sum = cal_MonthlyTotalWeight(wopcLst)
opp = cal_OnePercentPatients(0.84513662, 27407+27075+27345, 58965.158825309925)
prediction(wopcLst, sum, opp, preList)
print("3-기관지 및 폐의 악성신생물 0.83")
print(preList, '\n')

# 4-구역 및 구토 0.74
preList = []
wopcLst = cal_WeightOfPerCity(top4part1, top4part2, top4part3, pop)
sum = cal_MonthlyTotalWeight(wopcLst)
opp = cal_OnePercentPatients(5.28927012, 23432+23469+22813, 274529.11360980634)
prediction(wopcLst, sum, opp, preList)
print("4-구역 및 구토 0.74")
print(preList, '\n')

# 8-위궤양 0.60
preList = []
wopcLst = cal_WeightOfPerCity(top8part1, top8part2, top8part3, pop)
sum = cal_MonthlyTotalWeight(wopcLst)
opp = cal_OnePercentPatients(23.31024397, 9447+10000+9372, 381894.4740519151)
prediction(wopcLst, sum, opp, preList)
print("8-위궤양 0.60")
print(preList, '\n')

# 8-십이지장궤양 0.70
preList = []
wopcLst = cal_WeightOfPerCity(top8part1, top8part2, top8part3, pop)
sum = cal_MonthlyTotalWeight(wopcLst)
opp = cal_OnePercentPatients(3.39175259, 9447+10000+9372, 192670.59747242814)
prediction(wopcLst, sum, opp, preList)
print("8-십이지장궤양 0.70")
print(preList, '\n')

# 9-위-식도 역류병 0.92
preList = []
wopcLst = cal_WeightOfPerCity(top9part1, top9part2, top9part3, pop)
sum = cal_MonthlyTotalWeight(wopcLst)
opp = cal_OnePercentPatients(27.7697546, 20243+20668+20589, 2994719.9976300076)
prediction(wopcLst, sum, opp, preList)
print("9-위-식도 역류병 0.92")
print(preList, '\n')