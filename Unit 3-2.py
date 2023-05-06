import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy.stats as st
import random
import math

df = pd.read_csv('FootballPlayerStats.csv')
img = mpimg.imread('342797500_624340512563165_5391218019196705160_n.png')

#รูปภาพที่สุ่มได้
plt.imshow(img)
# สุ่มข้อมูล เนื่องจากการสุ่มมีหลากหลายแบบ ในส่วนของคำตอบจะเป็นคำตอบที่สุ่มได้นักแตะที่อยู่ Comp premier League 4 คนเท่านั้น
# random_rows = df.sample(n=10)
# print(random_rows)
print('\nจากข้อมูลสถิตินักฟุตบอล 5 ลีคใหญ่ในยุโรป มีข้อมูลนักแตะจำนวน 2921 คน สุ่มข้อมูลนักแตะมา 10 คน \nจะได้ 4 คนที่อยู่ใน Comp premier League ถ้าสุ่มนักแตะมา 5 คน\n')

# สูตรคำนวณ
def c(n, k):
    return math.comb(n, k)

ans0 = round((c(4, 0) * c(6,5)) / c(10, 5), 2)
ans1 = round((c(4, 1) * c(6,4)) / c(10, 5), 2)
ans2 = round((c(4, 2) * c(6,3)) / c(10, 5), 2)
ans3 = round((c(4, 3) * c(6,2)) / c(10, 5), 2)
ans4 = round((c(4, 4) * c(6,1)) / c(10, 5), 2)

print('ก.จงหาฟังก์ชันความน่าจะเป็นที่จะสุ่มได้ Comp premier League\n')
print(f'ถ้าสุ่มนักแตะ 5 คน เพื่อหานักแตะที่อยู่ใน Comp premier League จากทั้งหมด 10 คน สามารถทำได้ C(10,5) = {c(10, 5)} วิธี')

print('ถ้าสุ่มได้ Comp premier League ได้ 0 แสดงว่า X=0')
print(f'F(0) = P(x=0) = (C(4,0) * C(6,5)) / C(10,5) = {ans0}\n')

print('ถ้าสุ่มได้ Comp premier League ได้ 1 แสดงว่า X=1')
print(f'ans : F(1) = P(x=1) = (C(4,1) * C(6,4)) / C(10,5) = {ans1}\n')

print('ถ้าสุ่มได้ Comp premier League ได้ 2 แสดงว่า X=2')
print(f'ans : F(2) = P(x=2) = (C(4,2) * C(6,3)) / C(10,5) = {ans2}\n')

print('ถ้าสุ่มได้ Comp premier League ได้ 3 แสดงว่า X=3')
print(f'ans : F(3) = P(x=3) = (C(4,3) * C(6,2)) / C(10,5) = {ans3}\n')

print('ถ้าสุ่มได้ Comp premier League ได้ 4 แสดงว่า X=4')
print(f'ans : F(4) = P(x=4) = (C(4,4) * C(6,1)) / C(10,5) = {ans4}\n')

print('ข.จงหาความน่าจะเป็นที่จะสุ่มได้ Comp premier League มากกว่า 2 คน')
print('ans : P(X>2) = F(3) + F(4) = 0.26')

plt.show()
