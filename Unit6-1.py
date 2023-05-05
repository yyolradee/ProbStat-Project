import scipy.stats as st
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("FootballPlayerStats.csv")

std = df['MP'].mean()
mean = df['MP'].std()

sd = 50 # สุ่มมา 50 คน
mp = 200 # sum of match played more than 200 match
print(f"ในสถิติปี 2021-2022 นักฟุตบอลแต่ละได้เข้าร่วมลงสนามเฉลี่ย {mean:.2f} เกม มีส่วนเบี่ยงเบนมาตรฐาน {std:.2f} เกม \nจงหาความน่าจะเป็นตัวอย่างของนักฟุตบอล {sd} คนที่ได้เข้าร่วมลงสนามมามากกว่า {mp} เกม\n")

# เนื่องจากประชากรมีขนาดใหญ่ มากกว่า 30 ค่าเฉลี่ยตัวอย่างจะมีการแจกแจงประมาณแบบปกติ
# ค่าเฉลี่ยตัวอย่างจะมีค่าเท่ากับค่าเฉลี่ยของประชากร
print(f"X - N({mean:.2f}, {(std**2/sd):.2f})")
# ค่าความแปรปรวนตัวอย่างจะเท่ากับ sigma**2/n
print(f"-->  P(X > {(mp/sd):.2f})")

top = mp/sd - mean
bot = (std**2)/sd
print(f"-->  P(X - u/sd/sqrt(n) > {(top/bot):.2f})")
print(f"-->  P(Z > {(top/bot):.2f}), 1 - P(Z <= {(top/bot):.2f})")

Zval = st.norm.sf((top/bot))
print(f'Answer is {Zval:.2f}')