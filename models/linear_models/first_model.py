import pandas as pd
import pickle
import statsmodels.api as sm
import patsy

database = pd.DataFrame()

with open ('nfl.db.1.0.pkl', 'rb') as fl:
    database = pickle.load(fl)
fl.close


database = database.rename({'HOME/AWAY': 'HOME_OR_AWAY'}, axis=1)

"""I Took Pass completions and pass attempts out of the model because they were negative coefficients, and that didn't 
ring true to reality with me. After that change, the intercept fell by about a touchdown, which bodes true."""

# All in one model

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
                       'PENALTIES_defender + PENALTY_YDs_defender' ,data=database, return_type='dataframe')

model = sm.OLS(y,X)

fit = model.fit()



fit.summary()

#######################################

### Model including Time of Possession, for a benchmark.###

# CHECK YOUR VALUES THEYRE DUPLICATED
y4, X4 = patsy.dmatrices('Final ~ HOME_OR_AWAY +' +
                         'PASS_CMP_challenger + ' + \
                         'PASS_ATT_challenger + ' + \
                         'PASS_YDs_challenger + ' + \
                         'PASS_TDs_challenger + ' + \
                         'PASS_INT_challenger + ' + \
                         'RUSH_ATT_challenger + ' + \
                         'RUSH_YDS_challenger + ' + \
                         'RUSH_TDs_challenger + ' + \
                         'SACKS_defender + ' + \
                         'SACK_YDs_defender + ' + \
                         'FUMBLES_LOST_challenger + ' + \
                         'SACKS_challenger + ' + \
                         'SACK_YDs_challenger + ' + \
                         'FUMBLES_challenger + ' + \
                         'PENALTIES_challenger +' + \
                         'PENALTY_YDs_challenger + ' + \
                         'PASS_CMP_defender + ' + \
                         'PASS_ATT_defender + ' + \
                         'PASS_YDs_defender + ' + \
                         'PASS_TDs_defender + ' + \
                         'PASS_INT_defender + ' + \
                         'RUSH_ATT_defender + ' + \
                         'RUSH_YDS_defender + ' + \
                         'RUSH_TDs_defender + ' + \
                         'SACKS_defender + ' + \
                         'SACK_YDs_defender + ' + \
                         'FUMBLES_defender + ' + \
                         'FUMBLES_LOST_defender + ' + \
                         'PENALTIES_defender +' + \
                         'PENALTY_YDs_defender + ' + \
                         'TOP_int_challenger + ' + \
                         'TOP_int_defender' \
                         , data=df, return_type='dataframe')

model_all_features = sm.OLS(y4, X4)

fit_all_features = model_all_features.fit()

fit_all_features.summary()

### Check to see if the residuals are normally distributed

fit_all_features.resid.plot(style='o', figsize=(12,8));


########################

#### Decrease features


y5, X5 = patsy.dmatrices('Final ~ HOME_OR_AWAY +' + \
                         'PASS_CMP_challenger + ' + \
                         'PASS_ATT_challenger + ' + \
                         'PASS_YDs_challenger + ' + \
                         'PASS_TDs_challenger + ' + \
                         'PASS_INT_challenger + ' + \
                         'RUSH_ATT_challenger + ' + \
                         'RUSH_YDS_challenger + ' + \
                         'RUSH_TDs_challenger + ' + \
                         ##'RUSH_ATT_defender + ' +\
                         # 'RUSH_YDS_defender + ' +\
                         ##'RUSH_TDs_defender + ' +\
                         # 'SACKS_challenger + ' +\
                         # 'SACK_YDs_challenger + ' +\
                         # 'SACKS_defender + ' +\
                         'SACK_YDs_defender + ' + \
                         # 'FUMBLES_challenger + ' +\
                         'FUMBLES_LOST_challenger + ' + \
                         # 'PENALTIES_challenger +' +\
                         'PENALTY_YDs_challenger + ' + \
                         ##'PASS_CMP_defender + ' +\
                         # 'PASS_ATT_defender + ' +\
                         # 'PASS_YDs_defender + ' +\
                         ##'PASS_TDs_defender + ' +\
                         # 'PASS_INT_defender + ' +\
                         # 'FUMBLES_defender + ' +\
                         'FUMBLES_LOST_defender + ' + \
                         # 'PENALTIES_defender +' +\
                         # 'TOP_int_defender + ' +\
                         'PENALTY_YDs_defender + ' + \
                         'TOP_int_challenger', data=df, return_type='dataframe')

model2 = sm.OLS(y5, X5)

fit = model2.fit()

fit.summary()
