
import copy
import patsy

"""Feature Engineering: Adding Time of possession to the Model. But it had no notable impact"""


time_db = copy.deepcopy(database)

time_db['TOP_int_challenger'] = database['Time of Possession_challenger'].apply(lambda top: int(top.split(':')[0]))

y, X = patsy.dmatrices('Final ~ HOME_OR_AWAY +' +
                       # PASS_CMP_challenger +'\
                       # +' PASS_ATT_challenger +
                       'PASS_YDs_challenger + PASS_TDs_challenger + ' + \
                       'PASS_INT_challenger + RUSH_ATT_challenger + RUSH_YDS_challenger + RUSH_TDs_challenger + ' + \
                       'RUSH_ATT_defender + RUSH_YDS_defender + RUSH_TDs_defender + ' + \
                       'SACKS_defender + SACK_YDs_defender + FUMBLES_defender + ' + \
                       'SACKS_challenger + SACK_YDs_challenger + FUMBLES_challenger + ' + \
                       'PENALTIES_challenger + PENALTY_YDs_challenger + ' + \
                       # 'PASS_CMP_defender + PASS_ATT_defender +
                       'PASS_YDs_defender + PASS_TDs_defender + ' + \
                       'PASS_INT_defender + RUSH_ATT_defender + RUSH_YDS_defender + RUSH_TDs_defender + ' + \
                       'SACKS_defender + SACK_YDs_defender + FUMBLES_defender + FUMBLES_LOST_defender + ' + \
                       'PENALTIES_defender + PENALTY_YDs_defender + TOP_int_challenger + TOP_int_defender'
                       , data=time_db, return_type='dataframe')

model = sm.OLS(y, X)

fit = model.fit()

fit.summary()

# Did not have a significant effect.. Seemed to raise the coefficent from negative, which is more in line with reality.
