import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st

df = pd.read_csv('FootballPlayerStats.csv')

print("โจทย์ : หาเปอร์เซนต์ของนักฟุตบอลที่มีอายุระหว่าง 20-25 ปี ถ้าอายุมีการแจกแจงแบบปกติ\n")

# หาค่าเฉลี่ย และส่วนเบี่ยงเบนมาตรฐาน ของอายุนักฟุตบอล
ageMean = df.Age.mean()
ageStd = df.Age.std()
print(f"mean = {ageMean}\nStandard Division = {ageStd}\n")

print("X แทนอายุของนักฟุตบอล")
print(f"X ~ N({ageMean}, ({ageStd})^2)")
print("หา P(20 < X < 25)")

# z = (X - ageMean) / ageStd
# หา z score ของช่วงอายุที่ต้องการ
age20 = (20 - ageMean) / ageStd
age25 = (25  -ageMean) / ageStd

print("\nสิ่งที่โจทย์ต้องการคือ")
print(f"P({age20} < z < {age25})")
print(f"หรือ P(z < {age25}) - P(z <= {age20})")

# หา P score จาก standard normal distribution
pScoreAge20 = st.norm.sf(abs(age20))
pScoreAge25 = st.norm.sf(abs(age25))

print(f"P(z < {age25}) = {pScoreAge25}")
print(f"P(z <= {age20}) = {pScoreAge20}")
print()
print(f"ดังนั้น P({age20} < z < {age25}) = {pScoreAge25} - {pScoreAge20}")

ans = pScoreAge25 - pScoreAge20

print(f"คำตอบคือ {ans}")

# แสดงกราฟ
df.Age.hist()
plt.show()