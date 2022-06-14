# -*- coding: utf-8 -*-
"""
Python file containing data loading and cleaning scripts developed during the 
analysis of the synthetic transaction data.

Created on Sat Jun 04 10:32:06 2022

@author: Colin Shields
"""

# Data Wrangling
import pandas as pd
import numpy as np

#Utils
import os

# Data Loader Function
def get_transaction_data():
    return pd.read_json('..//transactions.txt', lines=True)

# Data cleaning function
def clean_transation_data(df):
    """
    Cleans the raw transaction data based 
    on observations from descriptive statistics and visualization
    
    Parameters:
    ___________
    df: pandas dataframe
        The raw transaction data
    
    Returns:
    ________
    df: pandas dataframe
        The dataframe after cleaning steps applied
    
    """
    
    # Developing descriptive statistics of the data inidicates that empty strings are used to denote missing data
    # Convert empty strings to null values
    df.replace('', np.nan, inplace=True)
    
    # Review of datatypes showed that multiple date time colums are stored as a string
    # Convert the string to pandas datetime
    datetime_like_cols = ['transactionDateTime','currentExpDate', 'accountOpenDate', 'dateOfLastAddressChange']
    for dtc in datetime_like_cols:
        df[dtc] = pd.to_datetime(df[dtc])
    
    # Review showed that accountNumber and customerId are stored at integers. 
    # In addition CVV colums and the card last four are integers and should strings.
    # Convert to string
    str_like_cols = ['accountNumber','customerId', 'cardCVV','enteredCVV','cardLast4Digits']
    for sc in str_like_cols:
        df[sc] = df[sc].astype(str)
        
    # Drop columns with all null data
    # Note: the following columns are all null: 'echoBuffer', 'merchantZip', 'merchantCity', 'merchantState', 'merchantZip', 'recurringAuthInd', 'posOnPremises' 
    empty_cols = ['echoBuffer', 'merchantZip', 'merchantCity', 'merchantState', 'merchantZip', 'recurringAuthInd', 'posOnPremises']
    _ = df.drop(empty_cols, axis=1, inplace=True)
    
    return df
    