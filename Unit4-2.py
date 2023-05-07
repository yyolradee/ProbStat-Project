import pandas as pd

df = pd.read_csv('FootballPlayerStats.csv')

def factorial(n):
    if n < 0:
        raise ValueError('factorial is not defined for negative numbers')
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = 10
x = 2
p = df[df['Squad'] == 'Barcelona']['G/Sh'].mean()
result = 0
for i in range(x):
    result += (factorial(n)/(factorial(n-i)*factorial(i)))*(p**i)*((1-p)**(n-i))

px = "["
for i in range(x):
    if(i == x-1):
        px += f"p(x={i})]"
    else:
        px += f"p(x={i}) + "



print(f"โจทย์ : ค่าเฉลี่ย goal per shot ของผู้เล่นทั้งหมดในทีม barcelona ใน 1 แมทช์ คือ {p*100:.2f}%")
print(f"จงหาความน่าจะเป็นที่จะยิง {n} ครั้ง แล้วทำประตูได้สำเร็จอย่างน้อย {x} ลูก")
print(f"p(x >= {x}) = 1 - p(x < {x}) = 1 - {px}")
print(f"ตอบ ความน่าเป็นที่ทีม barcelona จะยิง {n} ครั้ง แล้วทำประตูได้สำเร็จอย่างน้อย {x} ลูก คือ {1-result:.2f}")
