import pandas as pd
import numpy as np
from functools import reduce
from DataFrameFunctionsCleaning import concat_dfs

def CompareOverall_and_ISED(df1, df2):
    '''
    purpose: to compare the percent difference of counted DESCRIP_E of ISED to the overall counted DESCRIP_E
    
    note: this function has been depreciated for the purpose of this challenge since the numbers are very close to each other.
    '''
    descrip_1 = pd.DataFrame(df1[["DESCRIP_E"]].value_counts()).rename(columns={0: "cnt_all"})
    descrip_2 = pd.DataFrame(df2[["DESCRIP_E"]].value_counts()).rename(columns={0: "cnt_ISED"})
    descrip = pd.concat([descrip_1, descrip_2], axis=1).fillna(0)
    
    # unit: %
    descrip_pct = (100. * descrip / descrip.sum()).round(1).rename(columns={"cnt_all": "cnt_all_pct", "cnt_ISED": "cnt_ISED_pct"}) 
    descrip_pct["pct_diff"] = descrip_pct["cnt_ISED_pct"] - descrip_pct["cnt_all_pct"]
    
    descrip_pct_compare = descrip_pct[~(descrip_pct["pct_diff"]>=0)].sort_values(by=["pct_diff"])
    return descrip_pct_compare

def Filter_Indicator(filters):
    '''
    purpose: filtering out the dataframe rows by selected column values
    filters: "WORKPLACE WELL-BEING", "COMPENSATION", "WORKPLACE", "WORKFORCE", "EMPLOYEE ENGAGEMENT", "LEADERSHIP"
    filters can be either one above
    '''
    dfs = concat_dfs()
    dfs_filtered = dfs[dfs["INDICATORENG"] == filters]
    return dfs_filtered

def weighted_average_df(df):
    '''
    purpose: to calculate the weighted average based on columns SCORE100 and ANSCOUNT to the dataframe that grouped by columns of INDICATORENG, SUBINDICATORENG, QUESTION, DESCRIP
    '''
    df_weighted = pd.DataFrame(df.groupby(["INDICATORENG", "SUBINDICATORENG", "QUESTION", "DESCRIP"]) \
                    .apply(lambda x: np.average(x["SCORE100"], weights=x["ANSCOUNT"]))).round(2)
    return df_weighted

def analysis(filters):
    '''
    purpose: set up the general dataframe for purpose of analysis with features named gap: 2019vs2018, gap: 2020vs2019, and diff. between gaps
    '''
    df = Filter_Indicator(filters)
    df1, df2, df3 = df[df["SURVEYR"] == 2018], df[df["SURVEYR"] == 2019], df[df["SURVEYR"] == 2020]
    df1.pop("SURVEYR") 
    df2.pop("SURVEYR")
    df3.pop("SURVEYR")
    df1_weighted, df2_weighted, df3_weighted = weighted_average_df(df1).rename(columns={0: "2018_weighted"}), weighted_average_df(df2).rename(columns={0: "2019_weighted"}), weighted_average_df(df3).rename(columns={0: "2020_weighted"})
    dfs = [df1_weighted, df2_weighted, df3_weighted]
    dfs_final = reduce(lambda df_left, df_right: pd.merge(df_left, df_right, left_index=True, right_index=True, how='outer'), dfs).fillna(0)
    
    dfs_final["gap: 2019vs2018"] = dfs_final["2019_weighted"] - dfs_final["2018_weighted"]
    dfs_final["gap: 2020vs2019"] = dfs_final["2020_weighted"] - dfs_final["2019_weighted"]
    dfs_final["diff. between gaps"] = dfs_final["gap: 2020vs2019"] - dfs_final["gap: 2019vs2018"]
    
    return dfs_final

def analysis_comparison(filters):
    '''
    purpose: output the comparison dataframes as follows: 
    		 res1: comparison between gaps, showed the result in a bad way in which the recommendations are needed
    		 res2: comparison between gaps, showed the result in a good way in which the old strategies should still apply in the future
    		 res3: comparison between 2020 to 2019, showed the result in a bad way in which the recommendations are needed
    		 res4: comparison between 2020 to 2019, showed the result in a good way in which the old strategies should still apply in the future
    		 res5: overall weighted by column DESCRIP
    '''
    df = analysis(filters)
    df_filter = df[~((df["2018_weighted"] == 0) | (df["2019_weighted"] == 0) | (df["2020_weighted"] == 0))]
    
    # comparison between gaps
    res1 = df_filter[df_filter["diff. between gaps"]<0].sort_values(by="diff. between gaps")
    res2 = df_filter[df_filter["diff. between gaps"]>0].sort_values(by="diff. between gaps", ascending=False)
    
    # comparison between 2020 to 2019
    res3 = df_filter[df_filter["gap: 2020vs2019"]<0].sort_values(by="gap: 2020vs2019")
    res3.pop("diff. between gaps")
    res4 = df_filter[df_filter["gap: 2020vs2019"]>0].sort_values(by="gap: 2020vs2019", ascending=False)
    res4.pop("diff. between gaps")
    
    # overall weighted by column DESCRIP
    df_filter2 = df[~(df["2020_weighted"] == 0)]
    res5 = df_filter2[["2020_weighted"]].reset_index().groupby(["DESCRIP"]).mean().round(2).sort_values(by="2020_weighted")
    
    return res1, res2, res3, res4, res5

def analysis_top8(df, mode, cols):
    '''
    purpose: output the top8 results
    mode: "ascending and diff. between gaps", "descending and diff. between gaps", "ascending and 2020vs2019 gap", "descending and 2020vs2019 gap"
    cols: "diff. between gaps", "gap: 2020vs2019"
    '''
    if (mode == "ascending and diff. between gaps"):
    	df = df.sort_values(cols).groupby(level=[0,1]).head(8)
    elif (mode == "descending and diff. between gaps"):
        df = df.sort_values(cols, ascending=False).groupby(level=[0,1]).head(8)
    elif (mode == "ascending and 2020vs2019 gap"):
       	df = df.sort_values(cols).groupby(level=[0,1]).head(8)
    elif (mode == "descending and 2020vs2019 gap"):
       	df = df.sort_values(cols, ascending=False).groupby(level=[0,1]).head(8)
    return df