import pandas as pd
import numpy as np
from scipy import stats

# โหลดข้อมูลจากไฟล์ csv และเก็บในตัวแปร df
df = pd.read_csv('2021-2022_Football_Player_Stats.csv')

manu_df = df[df['Comp'] == 'Premier League']
num_players = len(manu_df)
print("Number of players in Premier League: {}".format(num_players))

# ค่าเฉลี่ยอายุของนักเตะ
mean_age = manu_df['Age'].mean()
print("Mean age of players in Premier League: {:.2f}".format(mean_age))

# สร้างช่วงความเชื่อมั่น 95% ของค่าเฉลี่ยอายุ
confidence_interval = stats.t.interval(0.95, len(manu_df)-1, loc=np.mean(manu_df['Age']), scale=stats.sem(manu_df['Age']))
print("Confidence interval of mean age at 95% confidence level:", confidence_interval)
