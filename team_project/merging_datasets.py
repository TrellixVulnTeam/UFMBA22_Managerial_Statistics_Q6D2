import parsing_espn
import parsing_pgatour
import pandas as pd
from pandas import DataFrame

espn_data = parsing_espn.espn_scrape()
pga_data = parsing_pgatour.ball_speed


merg_espn_test = pd.merge(espn_data, pga_data, on=['PLAYER'])

merg2 = pd.merge(merg_espn_test, parsing_pgatour.Driving_distance, on=['PLAYER'])
merg3 = pd.merge(merg2, parsing_pgatour.spin_rate, on=['PLAYER'])
merg4 = pd.merge(merg3, parsing_pgatour.chs_data, on=['PLAYER'])

merg4.to_csv(r'/home/egkennedy93/programming_projects/UFMBA22_Managerial_Statistics/team_project/DataSets/PGA_test.csv', index = False, sep=',', encoding='utf-8-sig')


# print(merg_espn_test)