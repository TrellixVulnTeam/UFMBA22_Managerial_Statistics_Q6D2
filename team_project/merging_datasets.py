import parsing_espn
import parsing_pgatour
import os
import pandas as pd
from pandas import DataFrame

espn_data = parsing_espn.espn_scrape()
pga_data = parsing_pgatour.ball_speed



merg_espn_test = pd.merge(espn_data, pga_data, on=['PLAYER'])
merge2 = pd.merge(merg_espn_test, parsing_pgatour.Driving_distance, on=['PLAYER'])
merge3 = pd.merge(merge2, parsing_pgatour.spin_rate, on=['PLAYER'])
merge4 = pd.merge(merge3, parsing_pgatour.chs_data, on=['PLAYER'])
merge5 = pd.merge(merge4, parsing_pgatour.carry_distance, on=['PLAYER'])
merge6 = pd.merge(merge5, parsing_pgatour.launch_angle, on=['PLAYER'])


final_merge = merge6
final_merge.replace(',', '', regex=True, inplace=True)

dir_path = os.path.dirname(os.path.realpath(__file__))
final_merge.to_csv(dir_path+'/DataSets/PGA_2020_Stats.csv', index=False, sep=',', encoding='utf-8-sig')
