# This is the function to make a training dataset. 
""" Variables are: 
    unbroken_data:   is a pandas dataframe of weather variable data, with datetimmes as the index
    x_cols:          is a LIST of the column names for the input variables
    y_col:           is the name (string) of the column of the output variable
    TS_value:     is a decimal value defining how much of the dataset to use for training vs validation (0.99) = 99% training 1% validation
    
(Maybe use NAME: as a string name to assosiate with the output of this function?)
"""

import os
import pandas as pd
import numpy as np 
from sklearn.preprocessing import StandardScaler



def make_training_dataset(unbroken_data, x_cols, y_col, TS_value = 0.80):
    
    TRAIN_SPLIT = int(len(unbroken_data)*TS_value)     
    # split data for train and validation
    train_data = unbroken_data.iloc[:TRAIN_SPLIT]
    val_data = unbroken_data.iloc[TRAIN_SPLIT:]

    # set up the training datasets
    X_train = train_data[x_cols].values  
    # scale the x component of the training data
    X_train_scaler = StandardScaler().fit(X_train)
    X_train = X_train_scaler.transform(X_train)

    y_train = train_data[y_col].values                 # scale the y data too, and then make the scale unique to use it to unscale the final data later
    y_train = y_train.reshape(-1, 1)
    y_train_scaler = StandardScaler().fit(y_train)
    y_train = y_train_scaler.transform(y_train)


    # set up the validation datasets
    X_val = val_data[x_cols].values  
    # scale the x component of the training data
    X_val_scaler = StandardScaler().fit(X_val)
    X_val = X_val_scaler.transform(X_val)

    y_val = val_data[y_col].values
    y_val = y_val.reshape(-1, 1)
    y_val_scaler = StandardScaler().fit(y_val)
    y_val = y_val_scaler.transform(y_val)

    return X_train, y_train, X_val, y_val, train_data, val_data, y_train_scaler, y_val_scaler, X_train_scaler