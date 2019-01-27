##Polynomial Features do not help.

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lars #ordinary linear regression + w/ ridge regularization
from sklearn.preprocessing import StandardScaler, PolynomialFeatures

lm = LinearRegression()
lars = Lars()

poly = PolynomialFeatures(4)

poly.fit(df[['PASS_YDs_challenger', 'PASS_CMP_challenger', 'PASS_ATT_challenger', 'PASS_TDs_challenger',\
                       'PASS_INT_challenger', 'RUSH_ATT_challenger', 'RUSH_YDS_challenger', 'RUSH_TDs_challenger',\
                       'SACK_YDs_defender', 'FUMBLES_LOST_challenger', 'FUMBLES_LOST_defender', 'PENALTY_YDs_defender',\
                       'TOP_int_challenger']])

cross_val_score(lars, poly.transform(df[['PASS_YDs_challenger', 'PASS_CMP_challenger', 'PASS_ATT_challenger', 'PASS_TDs_challenger',\
                       'PASS_INT_challenger', 'RUSH_ATT_challenger', 'RUSH_YDS_challenger', 'RUSH_TDs_challenger',\
                       'SACK_YDs_defender', 'FUMBLES_LOST_challenger', 'FUMBLES_LOST_defender', 'PENALTY_YDs_defender',\
                       'TOP_int_challenger']]), y=df[['Final']], cv=5, scoring='r2', verbose=4)