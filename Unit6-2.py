import scipy.stats as st
import math
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("FootballPlayerStats.csv")

# ค่าเฉลี่ย และส่วนเบี่บงเบนของเวลาที่นักฟุตบอลลงเล่นในสนาม
mean = df.Min.mean()
std = df.Min.std()

print(f"โจทย์ : จากสถิติของนักฟุตบอล 5 ลีคใหญ่ในยุโรป ฤดูกาล 2021-2022 พบว่านักฟุตบอลลงเล่นในสนามตลอดทั้งฤดูกาลเฉลี่ย {mean:.2f} นาที และมีส่วนเบี่ยงเบนมาตรฐาน {std:.2f} นาที")
print(f"จงหาความน่าจะเป็นที่นักฟุตบอล 100 คน ลงเล่นในสนามน้อยกว่า 1000 นาที\n")

print("X แทนเวลาที่นักฟุตบอลลงเล่นในสนาม (นาที)")
print(f"จะได้ X ~ N({mean:.2f}, ({std:.2f})^2 / √100)")
print("หา P(X < 1000)\n")

# z-score ของ P(X < 1000)
z_score = (1000 - mean) / (std / math.sqrt(100))
print(f"ดังนั้น P(X < 1000) = P(Z < (1000 - 1234.76) / (977.64 / √100))")
print(f"                 = P(Z < {z_score:.2f})")

# P score ของ (Z < -2.40)
z_val = st.norm.sf(z_score)
print(f"                 = {z_val:.2f}")

# แสดงกราฟ
df.Min.hist()
plt.show()