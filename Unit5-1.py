import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

# นำ Dataset เข้า DataFrame
df = pd.read_csv('FootballPlayerStats.csv', encoding='latin-1')

# กำหนดค่าระดับนัยสำคัญ ( 5% )
alpha = 0.05

# สร้างตารางกระจายความถี่จากคอลัมน์ที่ชื่อว่า 'Pos' และ 'Age'
table = pd.crosstab(df['Pos'], pd.cut(df['Age'], [0, 20, 25, 30, 35, 40]))

# Print ตารางกระจายความถี่
print('ตารางกระจายความถี่:')
print(table)

# ใช้ np.outer คำนวณหาค่าความถี่ที่คาดหวัง
expected = np.outer(table.sum(axis=1), table.sum(axis=0)) / table.values.sum()

# Print ค่าความถี่ที่คาดหวัง
print('\nค่าความถี่ที่คาดหวัง:')
print(expected)

# คำนวณหาค่าสถิติไคสแควร์, ค่า p, ค่าองศาความเป็นอิสระ, ค่าความถี่ที่คาดหวัง และเก็บไว้ในตัวแปร
chi2, p, dof, expected = chi2_contingency(table)

# Print ค่าสถิติไคสแควร์ และ ค่า p
print(f'\nค่าสถิติไคสแควร์: {chi2:.2f}')
print(f'ค่า p: {p:.5f}')

# คำนวณหาค่าเบี่ยงเบนมาตรฐาน
std_dev = np.sqrt(chi2 / dof)
print(f'ค่าเบี่ยงเบนมาตรฐาน: {std_dev:.2f}')

# นำค่าทั้งหมดที่ได้มาไปสรุปผลว่าสมมติฐานเพื่อการทดสอบจะถูกปฎิเสธหรือไม่ โดยเทียบค่า p ที่ได้กับ alpha
if p < alpha:
    print('\nคำตอบคือ: สมมติฐานถูกปฎิเสธ (มีความแตกต่างระหว่างข้อมูลภายในตาราง)')
else:
    print('\nคำตอบคือ: สมมติฐานไม่ถูกปฎิเสธ (ไม่มีความแตกต่างระหว่างข้อมูลภายในตาราง)')

# สร้างกราฟแท่งจากตารางกระจายความถี่
table.plot(kind='bar')
plt.xlabel('Position')
plt.ylabel('Count')
plt.title('Distribution of All Football Players Age by Position')
plt.show()
