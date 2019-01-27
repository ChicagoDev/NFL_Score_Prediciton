"""Create the Data"""
pd.get_dummies(df['index_challenger']).head()

nfl_db = pd.DataFrame()
with open('nfl.db.1.1.pkl', 'rb') as fl:
    nfl_db = pickle.load(fl)

dummies_def = pd.get_dummies(nfl_db['index_defender'])

big_model_db = nfl_db.rename(columns={'Net Pass Yards_challenger': 'NET_PASS_YDS_challenger', 'Net Pass Yards_defender': 'NET_PASS_YARDS_defender'})

big_model_db = big_model_db.drop(columns=['1','2','3','4'])

big_model_db.columns

pd.get_dummies(big_model_db['index_challenger'])

pd.get_dummies(big_model_db['index_defender'])

big_dummy_db = big_model_db.merge(pd.get_dummies(big_model_db['index_challenger']), left_index=True, right_index=True)

big_dummy_db = big_model_db.merge(pd.get_dummies(big_model_db['index_defender']), left_index=True, right_index=True, suffixes=('challenger', 'defender'))

ridge_tests_R2 = np.zeros([1,0])

ridge_tests_R2.shape

#######################
###

"""Create The model and test. Print the Ridge vs. Lasso Graph."""

ridge_test_arr = []
lasso_test_arr = []

X_1, y_1 = big_dummy_db.drop(
    columns=['Final', 'HOME_OR_AWAY', 'TEAM', 'index_defender', 'Time of Possession_challenger',
             'Time of Possession_defender', 'index_challenger', 'index_defender', 'Fourth Down Conv._challenger',
             'Third Down Conv._defender', 'Fourth Down Conv._defender']), big_model_db['Final']

X_a, x_test_a, y_a, y_test_a = train_test_split(X_1, y_1, test_size=.2, random_state=42)

X_train_a, X_val_a, y_train_a, y_val_a = train_test_split(X_a, y_a, test_size=.25, random_state=15)

X_train_scaled = scaler.fit_transform(X_train_a.values)
X_val_scaled = scaler.transform(X_val_a.values)
X_test_scaled = scaler.transform(x_test_a.values)

for i in range(1, 2000):
    ridg_mod = Ridge(alpha=i)
    lass_mod = Lasso(alpha=i)

    ridg_mod.fit(X_train_a, y_train_a)
    lass_mod.fit(X_train_a, y_train_a)

    ridge_test_arr.append(ridg_mod.score(X_val_a, y_val_a))
    lasso_test_arr.append(lass_mod.score(X_val_a, y_val_a))

ridge_tests_R2 = np.array(ridge_test_arr)
lasso_tests_R2 = np.array(lasso_test_arr)

x_points = np.arange(1, 2000)

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8))
plt.title('Lasso vs Ridge in NFL Dataset (Teams as Feature)', fontsize=25)
plt.xlabel('Lambda', fontsize=20)
plt.ylabel('R-Squared', fontsize=20)

sns.set_style('whitegrid')

sns.lineplot(x=x_points, y=ridge_tests_R2)

sns.lineplot(x=x_points, y=lasso_tests_R2)

plt.legend(['RIDGE', 'LASSO'], fontsize=18)

plt.savefig('images/lasso_v_ridge_dummy_teams.png')

# Disclaimer No Teams.
