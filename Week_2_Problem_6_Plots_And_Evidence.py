# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 12:33:03 2021

@author: charl
"""
# Set up for analysis
import pandas as pd
import numpy as np
import matplotlib as plt

df = pd.read_csv("train.csv")

df.head(10)

"""
Gender vs Loan Status
"""
group = df.groupby(["Gender", "Loan_Status"]).size().reset_index(name="Count") # Creates a table with the count of each combination
group["Gender and Loan_Status"] = group["Gender"] + " " +  group["Loan_Status"] # Adds a column with combined text of the columns 
print(group)

group.plot(x="Gender and Loan_Status", y = ["Count"], kind = "bar") # Creates a bar chart of the count of each combination of Gender and Loan Status

"""
Successful Loan Amount vs Education
"""
mask = df['Loan_Status'].isin(['N']) # Only includes unsuccesful loans
onlysuccessful = df[~mask] # Filters out all unsuccessful loans
onlysuccessful.boxplot(column = "LoanAmount", by = "Education") # Creates a box plot of the successful loans, sorted by the different Education types

new = onlysuccessful[["Education", "LoanAmount"]] # Creates a data frame with only two columns
new.groupby("Education").describe() # Creates a description by the Education values

"""
Credit Record vs Loan Applications, and Property_Area vs Loan Applications
"""
df.groupby(["Credit_History", "Loan_Status"]).size().reset_index(name="Count")

df.groupby(["Property_Area", "Loan_Status"]).size().reset_index(name="Count")




