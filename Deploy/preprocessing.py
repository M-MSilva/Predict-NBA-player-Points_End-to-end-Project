# -*- coding: utf-8 -*-
from sklearn.base import BaseEstimator, TransformerMixin # the TransformerMixin to ensure fit_transform()
import pandas as pd
import numpy as np

#we collect the data
Dataset = pd.read_csv('https://raw.githubusercontent.com/M-MSilva/Predict-NBA-player-Points-End-to-end-Project/master/Dataset/NBA_Athletes.csv',
                      on_bad_lines='skip',decimal='.', thousands=',',encoding='utf-8')

#irrelevant
Dataset['POS'].replace({'C-F':'F-C','G-F':'F-G'},inplace=True)

#new dataset that will be used for prediction
NbaDataset = Dataset.drop("APG", axis=1)

#some data must become float
NbaDataset = NbaDataset.astype({'GP':'float','FTA':'float','2PA':'float','3PA':'float'})

#we delete all unnecessary data
NbaDataset = NbaDataset[['MIN%','MPG','TOPG','GP','USG%','FTA','2PA','3PA','BPG']].copy()


Nba_num = NbaDataset.select_dtypes(include=[np.number])#only the numerical data for later


#we must first get the column indices
names = "GP", "FTA", "2PA", "3PA","TOPG"
gp_ix, fta_ix, pa2_ix, pa3_ix, topg_ix = [Nba_num.columns.get_loc(i) for i in names ] 

#create the transformer that will imput the fit_transform
class CreateCombinedAttributes(BaseEstimator, TransformerMixin):
    def __init__(self, add_PA2PG=True,add_FTAPG=True,add_PA3PG=True): 
        self.add_PA2PG = add_PA2PG
        self.add_FTAPG = add_FTAPG
        self.add_PA3PG = add_PA3PG
    def fit(self, X, y=None):
        return self #to implement the fit method
    def transform(self, X): 
        TOT = X[:, topg_ix]*X[:, gp_ix]
        if (self.add_PA2PG & self.add_FTAPG & self.add_PA3PG):
            PA2PG = X[:, pa2_ix] / X[:, gp_ix]
            FTAPG = X[:, fta_ix] / X[:, gp_ix]
            PA3PG = X[:, pa3_ix] / X[:, gp_ix]
            return np.c_[X, FTAPG, PA3PG,
                         PA2PG,TOT]
        else:
            return np.c_[X, TOT]

