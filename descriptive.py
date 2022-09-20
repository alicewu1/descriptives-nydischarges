import math
import statistics # for descriptive statistics
import numpy as np # for single/multi dimensional arrays
from scipy import stats # scientific computing based on numpy
import pandas as pd 
import matplotlib.pyplot # for data visualization
from pandas.plotting import scatter_matrix # for plotting data
from statsmodels.formula.api import ols 
import seaborn ## for statistical visualizations


#load in 2016 dataset using API CSV link
sparcs=pd.read_csv('https://health.data.ny.gov/resource/gnzp-ekau.csv')
sparcs

sparcs.shape # 1000 rows x 34 columns
sparcs.columns # view column name
sparcs.dtypes # view data types 
