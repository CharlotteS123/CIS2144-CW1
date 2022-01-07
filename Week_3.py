"""
Created on Mon Oct 25 22:08:55 2021

@author: charl
"""
# Set up libraries
import pandas as pd
import numpy as np
import matplotlib as plt

df = pd.read_csv("train.csv")

# Data Cleaning - fixing missing values
df.isna().sum() # Shows missing values

new = df.dropna(thresh=None)
new.head(10)

# Data Cleaning - removing outliers
new.boxplot()

"""
This for loop iterates through each numerical column and removes the outliers for
each one. The outliers are any values outside of the upper and lower bounds, which
are values (1.5*IQR) outside of the quartile values.
"""
num = ["ApplicantIncome", "CoapplicantIncome", "LoanAmount", "Loan_Amount_Term"]
for i in num:
    Q1 = new[i].quantile(0.25)
    Q3 = new[i].quantile(0.75)
    IQR = Q3-Q1
    Lower_Bound = Q1 - (1.5*IQR)
    Upper_Bound = Q3 + (1.5*IQR)
    new = new[~((new[i]<Lower_Bound)|(new[i]>Upper_Bound))]
new.boxplot()

# Data Transformation - Changing categorical information to numerical values

numerical = new
numerical["Loan_ID"] = numerical["Loan_ID"].str[2:] # removes LP from each value
numerical["Loan_ID"] = numerical["Loan_ID"].astype(str).astype(int)
numerical = pd.get_dummies(numerical)

print(numerical.head(10))

