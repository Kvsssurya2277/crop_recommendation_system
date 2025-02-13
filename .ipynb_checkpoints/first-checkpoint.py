import pandas as pd
import numpy as np
import seaborn as sns
crop=pd.read_csv("Crop_recommendation.csv")
# print(crop.head())
# print(crop.shape)
#print(crop.info())
#print(crop.isnull().sum())
#print(crop.duplicated().sum())
#print(crop.describe())
#print(crop.corr())
sns.heatmap(crop.corr, annot=True, cbar=True)