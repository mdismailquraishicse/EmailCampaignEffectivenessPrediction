import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class PreprocessEmailCompaign:
    def __init__(self, df):
        self.df = df
    def nullHandler(self):
        drop_cols = ['Customer_Location'] # drop the columns because already lost important informations.
        impute_cols = ['Total_Links', 'Total_Images', 'Total_Past_Communications'] # impute these columns with median or mean
        self.df.drop(drop_cols, axis=1, inplace=True)
        for col in impute_cols:
            median = self.df[col].quantile(.5)
            self.df[col] = self.df[col].fillna(median)

    def eda(self):
        pass