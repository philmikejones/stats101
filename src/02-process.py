#! ~/miniconda3/bin/python3

# Process the downloaded data files for use in the notebooks
# Save the resulting data as a pickle for simplicity
# If the pickle breaks it doesn't matter because we have the original
# data and this processing script

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.stats

# Living costs and food survey
food = pd.read_csv(
    "../data/external/UKDA-7932-tab/tab/lcfs_2013_teaching.tab",
    sep = "\t"
)

# Income (`P344pr`) is top-coded so remove this
food = food[food["P344pr"] < 1184]

food.to_pickle("../data/processed/food")


# Sheffield age census
age_shf = pd.read_csv("../data/external/age_shf.csv")
age_shf = age_shf[["C_AGE_NAME", "OBS_VALUE"]]
age_shf.C_AGE_NAME = age_shf.C_AGE_NAME.str.replace("Age under 1", "0")
age_shf.C_AGE_NAME = age_shf.C_AGE_NAME.str.replace(" and over", "")
age_shf.C_AGE_NAME = age_shf.C_AGE_NAME.str.replace("Age ", "")
age_shf.C_AGE_NAME = pd.to_numeric(age_shf.C_AGE_NAME)

sum_obsvalue = age_shf.OBS_VALUE.sum()  # to check the spread
age_shf = age_shf.loc[age_shf.index.repeat(age_shf["OBS_VALUE"])]

if len(age_shf.index) != sum_obsvalue:
    raise Exception("age data frame not spread correctly")

age_shf = age_shf.drop("OBS_VALUE", axis = 1)  # default 'axis' is 'index'

age_shf.to_pickle("../data/processed/age_shf")


# Eastbourne age Census
age_ebn = pd.read_csv("../data/external/age_ebn.csv")
age_ebn = age_ebn[["C_AGE_NAME", "OBS_VALUE"]]
age_ebn.C_AGE_NAME = age_ebn.C_AGE_NAME.str.replace("Age under 1", "0")
age_ebn.C_AGE_NAME = age_ebn.C_AGE_NAME.str.replace(" and over", "")
age_ebn.C_AGE_NAME = age_ebn.C_AGE_NAME.str.replace("Age ", "")
age_ebn.C_AGE_NAME = pd.to_numeric(age_ebn.C_AGE_NAME)

sum_obsvalue = age_ebn.OBS_VALUE.sum()  # for checks
age_ebn = age_ebn.loc[age_ebn.index.repeat(age_ebn["OBS_VALUE"])]

if len(age_ebn.index) != sum_obsvalue:
    raise Exception("age_ebn data frame not spread correctly")

age_ebn = age_ebn.drop("OBS_VALUE", axis = 1)

age_ebn.to_pickle("../data/processed/age_ebn")
