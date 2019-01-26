import pickle
from sklearn.linear_model import LinearRegression
from sklearn.externals.joblib import load
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
import numpy as np
import os


class NFLScorePrediction(object):




    def __init__(self):

        #print(os.getcwd())

        self.cross_val_lin_model = load('../models/linear_model_cv_ed_ORIG.pkl')
        dmatricies = []
        with open('../models/feature_matrix_andY_vector_ORIG.pkl', 'rb') as fl:
            dmatricies = pickle.load(fl)
        self.X_orig = dmatricies[1]
        self.y_orig = dmatricies[0]




    def get_r2_with_cv(self):

        folds = KFold(n_splits=5, shuffle=True, random_state=51)

        lm_r2 = np.array(cross_val_score(self.cross_val_lin_model, self.X_orig, self.y_orig, cv=folds, scoring='r2'))
        return lm_r2.mean()