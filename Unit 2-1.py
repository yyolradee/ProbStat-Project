import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('FootballPlayerStats.csv')

mp = 30 # Matches played มากกว่า 30 เกม
print(f"\nโจทย์ : ถ้าเลือกนักฟุตบอลมา 1 คน โดยมีเงื่อนไขกำหนดว่าจะต้องมี Matches played มากกว่า {mp} เกม\nจงหาความจะเป็นที่ผู้ได้รับเลือกไม่เคยได้ใบแดง\n")

All_player = len(df)  # จำนวนข้อมูลทั้งหมด
MP30 = len(df[df.MP > mp]) # จำนวนผู้เล่นที่มี Match played มากกว่า 30
MP30_NoRed = len(df[(df.MP > mp) & (df.CrdR == 0)]) # จำนวนผู้เล่นที่มี Match played มากกว่า 30 และไม่เคยได้ใบแดง

print(f"จำนวนผู้เล่นทั้งหมด : {All_player}")
print(f"จำนวนผู้เล่นทั้งหมดที่มี Matches played มากกว่า {mp} เกม : {MP30}")
print(f"จำนวนผู้เล่นทั้งหมดที่มี Matches played มากกว่า {mp} เกมและไม่เคยได้ใบแดง : {MP30_NoRed}\n")

P_MP30_NoRed = MP30_NoRed/All_player
P_MP30 = MP30/All_player

print(f"ความน่าจะเป็นที่ผู้เล่นทั้งหมดมี Match played มากกว่า {mp} เกม และไม่เคยได้ใบแดง : {P_MP30_NoRed:.2f}")
print(f"ความน่าจะเป็นที่ผู้เล่นทั้งหมดมี Match played มากกว่า {mp} เกม : {P_MP30:.2f}\n")

Ans = (P_MP30_NoRed/P_MP30)
print(f"ดังนั้นความน่าจะเป็นที่ผู้เล่นมี Match played มากกว่า {mp} เกม และไม่เคยได้ใบแดงคือร้อยละ {Ans:.2f}\n")
# No_RedCard = df[df.CrdR == 0].count()
