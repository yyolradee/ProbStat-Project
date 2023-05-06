import pandas as pd
import scipy.stats as st
import numpy as np
from scipy.stats import poisson

df = pd.read_csv("FootballPlayerStats.csv")

mean_shots = df.Shots.mean()
expect_shots = 2

print(f"จากสถิติ นักฟุตบอล 5 ลีคใหญ่ในยุโรป ฤดูกาล 2021-2022 มีค่าเฉลี่ยในการยิงประตู {mean_shots:.2f} ครั้งต่อเกม ")
print(f"จงหาความน่าจะเป็นที่นักฟุตบอลจะยิงประตู ได้มากกว่า {expect_shots} ครั้งต่อเกม\n")
# คำนวณค่า Poisson Distribution สำหรับจำนวนประตูที่นักฟุตบอลทำได้ในเกม
# โดยใช้ค่าเฉลี่ยของ shots ที่ทำได้ในเกม และสร้าง Distribution สำหรับการทำประตูของทีมเรา

# Define the Poisson distribution with lambda= mean_shots
dist_shots = st.poisson(mu=mean_shots)

print("x แทนจำนวนประตูที่ยิงได้")
print(f"x ~ P(x; {mean_shots:.2f})")
ans_prob = 0
print(f"P(x < {expect_shots}) = 1 - [", end="")
for s in range(0, expect_shots + 1, 1):
    #นำ Poisson Distribution มาหาความน่าจะเป็น
    prob_shots = dist_shots.pmf(s)

    ans_prob += prob_shots
    print(f"P(x = {s})",  end="")
    if(s == expect_shots):
        print(']')
        break
    print(' + ', end="")

ans_prob = 1 - ans_prob

print(f"\nความน่าจะเป็นที่นักฟุตบอลจะยิงประตู ได้มากกว่า {expect_shots} ครั้งต่อเกม = {ans_prob * 100:.2f}%")