import pandas as pd
from DataFrameFunctionsCleaning import ImportData, TruncatedData, ISED_Data



def CheckShape(mode='none'):
    '''
    purpose: you can check the changes on dataframe shapes before and after applying the filtering the datasets
    '''
    if (mode == 'none'):
        df1, df2, df3, df4, df5, df6, df7 = ImportData()
    elif (mode =='truncated'):
    	df1, df2, df3, df4, df5, df6, df7 = TruncatedData()
    elif (mode == 'ISEDonly'):
    	df1, df2, df3, df4, df5, df6, df7 = ISED_Data()
    
    for i in range(1, 8):
        print(f"""shape of subset{i}: {eval(f"df{i}").shape}""")

def CheckNulls():
    '''
    purpose: check if there's NULL values in the dataframe
    '''
    df1, df2, df3, df4, df5, df6, df7 = ISED_Data()
    for i in range(1, 8):
        print(f"""**subset{i} dataset**\n
        Total Number of Null values:\n\n{eval(f"df{i}").isna().sum()}\n
        ========================================\n
        """)
        
def CheckSurveyYear():
    '''
    purpose: check the survey year in the ISED data
    '''
    df1, df2, df3, df4, df5, df6, df7 = ISED_Data()
    for i in range(1, 8):
        print(f"""**subset{i} dataset**\n
		\n{eval(f"df{i}")["SURVEYR"].value_counts()}\n
        ========================================\n
        """)