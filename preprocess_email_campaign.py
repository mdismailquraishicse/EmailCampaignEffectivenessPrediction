import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.outliers_influence import variance_inflation_factor

class PreprocessEmailCompaign:
    def __init__(self, df):
        self.df = df
        self.features = list(df.columns)
    def nullHandler(self):
        drop_cols = ['Customer_Location'] # drop the columns because already lost important informations.
        impute_cols = ['Total_Links', 'Total_Images', 'Total_Past_Communications'] # impute these columns with median or mean
        self.df.drop(drop_cols, axis=1, inplace=True)
        for col in impute_cols:
            median = self.df[col].quantile(.5)
            self.df[col] = self.df[col].fillna(median)

    def get_vif(self, excluded):
        features =[i for i in self.df.columns if i not in excluded]
        vif = {features[i]:float(variance_inflation_factor(self.df[features].values,i)) for i in range(len(features))}
        vif = pd.Series(vif)
        features = list(vif.index)
        features.append('Email_Status')
        self.features = features
        return vif