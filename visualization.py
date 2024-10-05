import matplotlib.pyplot as plt
import seaborn as sns

# 예제 데이터 리스트
old_data = [86000, 87999, 88000, 88000, 88000, 88000, 88888, 88888, 88888, 89000, 74000, 75000, 72000, 72000, 72000, 73333, 74000, 74000, 74444, 74800, 65000, 68000, 68999, 70000, 70000, 70000, 70000, 70000, 70000, 89000, 89000, 89999, 89999, 89999, 90000, 90000, 90000, 90000, 90000, 65000, 68000, 68999, 70000, 70000, 70000, 70000, 70000, 70000, 90000, 90000, 90000, 90000, 90000, 90000, 92000, 95000, 95000, 91900, 84000, 84000, 84000, 84999, 85000, 85000, 85000, 85000, 85000, 88000, 75000, 75000, 75000, 75000, 75000, 77000, 78000, 79999, 80000, 80000, 92000, 92000, 113000, 94500, 95000, 95000, 95000, 95000, 99999, 96000, 100000, 100000, 100000, 100000, 100000, 105000, 1000000, 102000, 105000, 107500, 96000, 96666, 97000, 97000, 97500, 980000, 99000, 99000, 99000, 99500, 80000, 80000, 80000, 80000, 80000, 80000, 81000, 82000, 83000, 84000, 108000, 109000, 110000, 110000, 110000, 110000, 110000, 110000, 110000, 110000, 99900, 99999, 99999, 99999, 100000, 100000, 100000, 100000, 100000, 100000, 130000, 130000, 134444, 135000, 135000, 138000, 139500, 140000, 140000, 140000, 140000, 140000, 140000, 140000, 150000, 144444, 144900, 145000, 145000, 147000, 148000, 169000, 149999, 150000, 150000, 150000, 150000, 150000, 150000, 110000, 110000, 111111, 112500, 115000, 119999, 120000, 120000, 120000, 120000, 120000, 120000, 120000, 121111, 125000, 129999, 130000, 130000, 130000, 130000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 155555, 156000, 158000, 390000, 400000, 400000, 400000, 466666, 499999, 540000, 580000, 650000, 649999, 680000, 690000, 700000, 720000, 750000, 777777, 849999, 750000, 750000, 750000, 189000, 189000, 197000, 197999, 250000, 210000, 210000, 218000, 219000, 230000, 330000, 350000, 335000, 345000, 347000, 348000, 350000, 350000, 350000, 380000, 245000, 250000, 350000, 270000, 300000, 310000, 320000, 320000, 320000, 320000, 160000, 169000, 169000, 170000, 170000, 170000, 178888, 179000, 180000, 180000]
earings_valid_23_data = [87999, 88000, 88000, 88000, 88888, 88888, 88888, 88888, 89000, 89000, 80000, 80000, 80000, 80000, 80000, 81000, 82000, 82222, 83000, 84000, 64000, 65000, 65000, 65000, 65555, 68000, 68999, 69999, 75000, 84000, 84000, 84999, 85000, 85000, 85000, 85000, 85000, 85000, 86000, 70000, 70000, 70000, 70000, 70000, 70000, 74000, 75000, 72000, 72000, 90000, 92000, 95000, 95000, 91900, 92000, 92000, 113000, 94000, 94000, 72000, 73333, 74000, 74000, 74000, 74444, 74800, 75000, 75000, 75000, 64000, 65000, 65000, 65000, 65555, 68000, 68999, 69999, 75000, 89999, 89999, 89999, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 75000, 75000, 75000, 77000, 78000, 78888, 79999, 79999, 80000, 80000, 130000, 130000, 130000, 130000, 130000, 135000, 135000, 139500, 140000, 140000, 97500, 98000, 980000, 99000, 99000, 99500, 99999, 99999, 99999, 100000, 100000, 1000000, 102000, 105000, 107500, 108000, 109000, 110000, 110000, 110000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 120000, 120000, 120000, 120000, 120000, 120000, 121111, 125000, 129999, 130000, 94500, 95000, 95000, 95000, 95000, 95000, 99999, 96000, 96000, 96666, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 155555, 156000, 147000, 148000, 169000, 149999, 150000, 150000, 150000, 150000, 150000, 140000, 140000, 140000, 140000, 140000, 150000, 144444, 144900, 145000, 145000, 110000, 110000, 110000, 110000, 110000, 111111, 112500, 115000, 119999, 120000, 280000, 280000, 285000, 288888, 290000, 290000, 295000, 295000, 299000, 299000, 299999, 299999, 300000, 300000, 300000, 300000, 300000, 300000, 300000, 180000, 189000, 189000, 197000, 210000, 210000, 218000, 219000, 217999, 320000, 320000, 320000, 320000, 320000, 320000, 320000, 320000, 325000, 325000, 269000, 270000, 280000, 315000, 275000, 277777, 278000, 279000, 280000, 280000, 330000, 330000, 330000, 330000, 349000, 350000, 335000, 345000, 347000, 348000, 349000, 350000, 350000, 350000, 350000, 350000, 350000, 350000, 350000, 350000, 300000, 333333, 350000, 360000, 310000, 310000, 310000, 310000, 311111, 158000, 160000, 169000, 169000, 170000, 170000, 170000, 178888, 179000, 180000, 230000, 245000, 250000, 350000, 255000, 259999, 260000, 260000, 260000, 264999, 380000, 380000, 380000, 390000, 400000, 400000, 400000, 400000, 400000, 400000, 500000, 403000, 405000, 409000, 410000, 410000, 411111, 415000, 420000, 420000, 420000, 430000, 439999, 450000, 455000, 466666, 470000, 480000, 480000, 485000, 488888, 499999, 560000, 540000, 540000, 580000, 555555, 570000, 590000, 600000, 380000, 355000, 360000, 360000, 365000, 370000, 390000, 377777, 380000, 380000, 1600000, 1380000, 1380000, 1450000, 1490000, 1500000, 1500000, 1600000, 1550000, 1600000, 750000, 750000, 750000, 760000, 780000, 790000, 799999, 800000, 800000, 848000, 650000, 610000, 640000, 650000, 649999, 650000, 700000, 670000, 670000, 685000, 850000, 1000000, 1000000, 1080000, 1000000, 1000000, 1100000, 1200000, 1500000, 1500000, 680000, 690000, 695000, 700000, 720000, 725000, 750000, 777777, 849999, 750000, 64000, 65000, 75000, 70000, 70000, 70000, 71000, 75000, 71000, 72000, 80000, 80000, 80000, 80000, 85000, 95000, 81999, 83000, 83000, 83000, 87000, 87000, 88000, 88000, 88000, 88000, 88000, 88000, 88848, 88888, 73000, 73000, 74000, 74999, 75000, 75000, 75000, 75000, 76000, 79999, 64000, 65000, 75000, 70000, 70000, 70000, 71000, 75000, 71000, 72000, 95000, 95000, 95000, 98765, 99000, 99999, 99999, 99999, 99999, 100000, 89000, 89000, 89000, 89500, 89990, 89999, 90000, 90000, 90000, 90000, 90000, 110000, 91000, 92000, 92000, 92000, 92000, 93000, 93000, 94999, 84000, 84000, 84000, 84999, 85000, 85000, 85000, 90000, 86500, 86999, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 100000, 100000, 100000, 100000, 100000, 100000, 105000, 145000, 105000, 105000, 105000, 105000, 105000, 105000, 105000, 110000, 110000, 278000, 111111, 111111, 111111, 111111, 111111, 115000, 115000, 120000, 120000, 120000, 120000, 120000, 125000, 129999, 130000, 130000, 130000, 130000, 130000, 130000, 133333, 134999, 170000, 143000, 144000, 145000, 145000, 145000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 155000, 160000, 159000, 159555, 160000, 160000, 135000, 135000, 137000, 138000, 139000, 139999, 139999, 140000, 140000, 140000, 222222, 230000, 250000, 350000, 270000, 270000, 290000, 280000, 280000, 290000, 170000, 170000, 180000, 180000, 180000, 190000, 199000, 199999, 200000, 200000, 285000, 285000, 295000, 290000, 290000, 300000, 300000, 300000, 300000, 330000, 330000, 345000, 350000, 333333, 335000, 337000, 338000, 339999, 345000, 395000, 399999, 400000, 400000, 400000, 400000, 400000, 400000, 400000, 405000, 499999, 500000, 520000, 535000, 540000, 540000, 550000, 580000, 599999, 555000, 370000, 370000, 370000, 375000, 375000, 380000, 380000, 389999, 390000, 399000, 450000, 450000, 450000, 450000, 450000, 450000, 466666, 480000, 490000, 499999, 580000, 650000, 610000, 640000, 650000, 649999, 650000, 650000, 670000, 670000, 685000, 680000, 690000, 695000, 700000, 720000, 725000, 750000, 777777, 849999, 750000, 750000, 750000, 750000, 760000, 780000, 790000, 799999, 800000, 800000, 848000, 850000, 1000000, 900000, 1000000, 1080000, 1000000, 1000000, 1100000, 1200000, 410000, 410000, 410000, 410000, 420000, 420000, 425000, 430000, 430000, 450000, 1500000, 1500000, 1600000, 1380000, 1380000, 1450000, 1490000, 1500000, 1500000, 1600000, 320000, 320000, 320000, 320000, 320000, 320000, 320000, 340000, 324000, 325000, 347000, 348000, 349999, 350000, 350000, 350000, 350000, 350000, 350000, 350000, 300000, 310000, 350000, 310000, 310000, 310000, 319999, 319999, 320000, 320000, 350000, 350000, 350000, 350000, 350000, 355000, 360000, 360000, 365000, 370000]

# x축: 데이터의 인덱스, y축: 데이터 값
x_values = [1]*len(earings_valid_23_data)  # 인덱스 값
y_values = earings_valid_23_data  # 리스트 값

# 산포도 그리기
# plt.figure(figsize=(15, 9))
# plt.scatter(x_values, y_values, color='blue', marker='o')

# # 제목 및 레이블 설정
# plt.title('Scatter Plot of Data')
# plt.xlabel('Index')
# plt.ylabel('Value')

# 히스토그램과 KDE 플롯 그리기
plt.figure(figsize=(10, 6))  # 플롯 크기 설정
sns.histplot(earings_valid_23_data, bins=20, kde=True)  # 히스토그램과 커널 밀도 추정

# 제목 및 레이블 설정
plt.title('Distribution of the Data')
plt.xlabel('Value')
plt.ylabel('Frequency')

# 이미지로 저장 (png 형식)
plt.savefig('scatter_plot_hist.png', dpi=300)
