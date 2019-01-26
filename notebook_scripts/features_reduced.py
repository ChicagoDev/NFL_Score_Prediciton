from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Lasso, LassoCV, Ridge, RidgeCV
from sklearn.metrics import r2_score
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

# X, y -> Minimal Model

### Test Setup
X, X_test, y, y_test = train_test_split(X_orig, y_orig, test_size=.2, random_state=42)
X_val, X_train, y_val, y_train = train_test_split(X, y, test_size=.3, random_state=22)
###

scaler = StandardScaler()

###Models
linear_model = LinearRegression()
#lasso = Lasso(alpha=1.5) # Lasso extremely sensitive.
ridge = Ridge(alpha=20)
poly_model = LinearRegression()
###




#### Scale
X_train_scaled = scaler.fit_transform(X_train.values)
X_test_scaled = scaler.transform(X_test.values)
X_val_scaled = scaler.transform(X_val.values)

####

### Polynomials
#poly_features = PolynomialFeatures(degree=5) # Every increase in polynomial results in a decrease in fit...
#X_train_poly = poly_features.fit_transform(X_train.values)
#X_test_poly = poly_features.transform(X_test.values)
#X_val_poly = poly_features.transform(X_val.values)
###


linear_model.fit(X_train, y_train)
ridge.fit(X_train_scaled, y_train)
#poly_model.fit(X_train_poly, y_train)
lasso.fit(X_train_scaled, y_train)


human_feature_r2 = linear_model.score(X_val, y_val)
#poly_feature_r2 = poly_model.score(X_val_poly, y_val)

#lasso_feature_r2 = lasso.score(X_val_scaled, y_val)
ridge_feature_r2 = ridge.score(X_val_scaled, y_val)

print(f'The scores for the regression tests are:'+'\n\t'+ f'Human {(human_feature_r2):.4f}'+'\n\t'+ f' RIDGE: {(ridge_feature_r2):.4f}')
      #+'\n\t'+  f'POLY: {(poly_feature_r2):.4f}'+'\n\t'+ f'LASSO: {(lasso_feature_r2):.4f}')