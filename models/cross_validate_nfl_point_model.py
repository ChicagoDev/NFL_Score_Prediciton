import pickle

import numpy as np
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler

"""
FEATURES FOR LINEAR MODEL TO PREDICT SUPERBOWL SCORE:

 Total Yards
 Pass Completions
 Pass Touchdowns
 Pass Interceptions
 Rush Yards
 Rush Touchdowns
 Turnovers
 Penalty Yards
 Fumbles Lost

 And I Factor in an opponent's:

 Pass Completions
 Pass Touchdowns
 Penalty Yards

"""

""" Load the feature Matrix and Result Vector that was created in Jupyter Notebook """
data_matrix = []
with open('models/feature_matrix_andY_vector_ORIG.pkl', 'rb') as file:
 data_matrix = pickle.load(file)

y = data_matrix[0]
X_nfl = data_matrix[1]


### Models
linear_model_nfl = LinearRegression()
lasso_nfl = Lasso(alpha=1) # Lasso extremely sensitive.
ridge_nfl = Ridge(alpha=1)
###



### Scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_nfl.values)

###

### Cross Validate
folds = KFold(n_splits=5, shuffle=True, random_state=51)
scaler = StandardScaler()


r2_linear_model_nfl = np.array(cross_val_score(linear_model_nfl, X_nfl, y, cv=folds, scoring='r2', n_jobs=2))
r2_lasso_model_nfl = np.array(cross_val_score(lasso_nfl, X_scaled, y, cv=folds, scoring='r2', n_jobs=2, ))
r2_ridge_model_nfl = np.array(cross_val_score(ridge_nfl, X_scaled, y, cv=folds, scoring='r2', n_jobs=2))
###

print(f'The average R2 for Linear Model is {r2_linear_model_nfl.mean()}.')
print(f'The average R2 for Lasso is is {r2_lasso_model_nfl.mean()}.')
print(f'The average R2 for Ridge is {r2_ridge_model_nfl.mean()}.')



