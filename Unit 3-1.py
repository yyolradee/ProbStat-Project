import pandas as pd
import math
from decimal import Decimal, getcontext
df = pd.read_csv("FootballPlayerStats.csv")
print("โจทย์ : หาความคาดหวังของนักฟุตบอลสัญชาติอังกฤษที่ได้รับเลือก เข้าในตำแหน่งที่เปิดรับสมัคร\n")
# จำนวนผู้สมัคร
eng_players = len(df[df['Nation'] == 'ENG'])
ita_players = len(df[df['Nation'] == 'ITA'])
all = eng_players+ita_players
# สร้าง DataFrame ของตำแหน่งและจำนวนตำแหน่งที่ต้องการ
print(f'ผู้เล่นประเทศอังกฤษ: {eng_players}')
print(f'ผู้เล่นประเทศอิตาลี : {ita_players}')
print('ตำแหน่งที่รับสมัคร: GK 1 คน, MF 1 คน, FW 1คน')

# คำนวณค่าคาดหวังของจำนวนผู้ที่จะได้รับเลือก
total_expected = 0
for x in range(0, 4):
    f = Decimal(math.comb(eng_players, x))* Decimal(math.comb(ita_players, 3 - x)) / Decimal(math.comb(all, 3))
    total_expected += x * f
# คำนวณค่าคาดหวัง
print('ค่าความคาดหวังของนักฟุตบอลสัญชาติอังกฤษที่ได้รับเลือกคือ {:.2f}'.format(total_expected))
