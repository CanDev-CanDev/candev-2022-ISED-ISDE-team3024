import pandas as pd
import numpy as np
from functools import reduce

def ImportData():
    '''
    purpose: import csv files
    '''
    df1 = pd.read_csv("/Users/anniguo/Downloads/CANDEV/Data/subset-1-sous-ensemble-1.csv")
    df2 = pd.read_csv("/Users/anniguo/Downloads/CANDEV/Data/subset-2-sous-ensemble-2.csv")
    df3 = pd.read_csv("/Users/anniguo/Downloads/CANDEV/Data/subset-3-sous-ensemble-3.csv")
    df4 = pd.read_csv("/Users/anniguo/Downloads/CANDEV/Data/subset-4-sous-ensemble-4.csv")
    df5 = pd.read_csv("/Users/anniguo/Downloads/CANDEV/Data/subset-5-sous-ensemble-5.csv")
    df6 = pd.read_csv("/Users/anniguo/Downloads/CANDEV/Data/subset-6-sous-ensemble-6.csv")
    df7 = pd.read_csv("/Users/anniguo/Downloads/CANDEV/Data/subset-7-sous-ensemble-7.csv")
    return df1, df2, df3, df4, df5, df6, df7

def TruncateData(df):
    '''
    purpose: work with selected columns and filtering the SCORE100 column with numbers less than or equal to 100.
    '''
    df_truncate = df[["LEVEL1ID", "SURVEYR", "DEPT_E", "DESCRIP_E", "QUESTION", "SCORE100", "ANSCOUNT", "INDICATORENG", "SUBINDICATORENG"]]
    df_truncate = df_truncate[~(df_truncate["SCORE100"]== " ")]
    df_truncate["ANSCOUNT"] = df_truncate["ANSCOUNT"].astype(int)
    df_truncate["SCORE100"] = df_truncate["SCORE100"].astype(int)
    df_truncate = df_truncate[df_truncate["SCORE100"]<=100]
    return df_truncate

def TruncatedData():
    '''
    purpose: connect functions ImportData and TruncateData to get the cleaned datasets for all 7 subsets
    '''
    df1, df2, df3, df4, df5, df6, df7 = ImportData()
    df1_truncated, df2_truncated, df3_truncated, df4_truncated, df5_truncated, df6_truncated, df7_truncated = TruncateData(df1), TruncateData(df2), TruncateData(df3), TruncateData(df4), TruncateData(df5), TruncateData(df6), TruncateData(df7)
    return df1_truncated, df2_truncated, df3_truncated, df4_truncated, df5_truncated, df6_truncated, df7_truncated

def ISEDData(df):
    '''
    purpose: filtering out the ISED data for further analysis
    # either LEVEL1ID=10 or DEPT_E="Innovation, Science and Economic Development Canada" works
    # here, I am only doing both to double check the filtering work correctly 
    '''
    df_ISED = df.loc[(df["LEVEL1ID"] == 10) & (df["DEPT_E"] == "Innovation, Science and Economic Development Canada")]
    df_ISED = df_ISED.drop(["LEVEL1ID", "DEPT_E"], axis=1)
    return df_ISED
    
def ISED_Data():
    '''
    purpose: connect functions TruncatedData and ISED_Data to get the cleaned datasets for all 7 subsets
    '''
    df1, df2, df3, df4, df5, df6, df7 = TruncatedData()
    df1_ISED, df2_ISED, df3_ISED, df4_ISED, df5_ISED, df6_ISED, df7_ISED = ISEDData(df1), ISEDData(df2), ISEDData(df3), ISEDData(df4), ISEDData(df5), ISEDData(df6), ISEDData(df7)
    return df1_ISED, df2_ISED, df3_ISED, df4_ISED, df5_ISED, df6_ISED, df7_ISED

def general_descrip_subsets1_5(df):
    '''
    purpose: switch the DESCRIP_E column to the end of the dataframe and rename it to DESCRIP
    
    subset5: shift work, full time status, flexible working arrangements, employment status, occupational category, community, and Other Leave with Pay. 
    '''
    df = df[[col for col in df.columns if col != 'DESCRIP_E' ] + ['DESCRIP_E']].rename(columns={"DESCRIP_E": "DESCRIP"})
    return df


def Regexp_descrip_subset2(df):
    '''  
    purpose: build a column named DESCRIP by applying regular expression techniques to the DESCRIP_E column to clean up the categories and pop out the DESCRIP_E column in the end
    idea for filtering the age group: # https://data.oecd.org/emp/employment-rate-by-age-group.htm
    
    subset2:supervisor status, length of time in public service and organization, and age.
    '''
    
    df["DESCRIP"] = df.loc[:, "DESCRIP_E"] \
                     .str.replace(r'(^Less.*)', 'less than 3 years experiences') \
                     .str.replace(r'(^3.*)', '3 - 10 years experiences') \
                     .str.replace(r'(^11.*)', '11 - 20 years experiences') \
                     .str.replace(r'(^More.*)', 'more than 20 years experiences') \
                     .str.replace(r'(.*under$)', 'age 24 and under') \
                     .str.replace(r'(.*25.*|.*30.*|.*35.*|.*40.*|.*45.*|.*50.*)', 'age 25 - 54') \
                     .str.replace(r'(.*55.*|.*60.*)', 'age 55 and above')
    df.pop("DESCRIP_E")
    return df

def Regexp_descrip_subset3(df):
    '''
    purpose: build a column named DESCRIP by applying regular expression techniques to the DESCRIP_E column to clean up the categories and pop out the DESCRIP_E column in the end
    
    # https://www.canada.ca/en/treasury-board-secretariat/services/collective-agreements/job-evaluation/job-evaluation-standards-public-service-employees.html
    subset3:gender, sexual orientation and employment equity breakdowns. 
    '''
    df["DESCRIP"] = df.loc[:, "DESCRIP_E"] \
                      .str.replace(r'(.* - Not selected.*$)', 'Prefer not to answer') \
                      .str.replace(r'(Male gender)', 'gender - Male') \
                      .str.replace(r'(Female gender)', 'gender - Female') \
                      .str.replace(r'(Gender diverse)', 'gender - diverse') \
                      .str.replace(r'(Heterosexual)', 'sexuality - Heterosexual') \
                      .str.replace(r'(^Gay.*|Bisexual)', 'sexuality - LGBTQ2S+') \
                      .str.replace(r'(Another sexual orientation)', 'sexuality - other') \
                      .str.replace(r'(Chinese)', 'Visible minority - Chinese') \
                      .str.replace(r'(^Southeast Asian.*)', 'Visible minority - Southeast Asian') \
                      .str.replace(r'(^South Asian/East Indian.*)', 'Visible minority - South Asian/East Indian') \
                      .str.replace(r'(^Non-White West Asian.*)', 'Visible minority - Non-White West Asian, North African or Arab') \
                      .str.replace(r'(Black)', 'Visible minority - Black') \
                      .str.replace(r'(Filipino)', 'Visible minority - Filipino') \
                      .str.replace(r'(Person of mixed origin.*)', 'Visible minority - Person of mixed origin') \
                      .str.replace(r'(Other visible minority group|Visible minority$)', 'Visible minority - other') \
                      .str.replace(r'(Indigenous|First Nation.*|M�tis)', 'Non-visible minority - Indigenous') \
                      .str.replace(r'(Non-White Latin American.*)', 'Non-visible minority - Non-White Latin American') \
                      .str.replace(r'(^A chronic.*)', 'disabilities - chronic health') \
                      .str.replace(r'(^A cognitive.*)', 'disabilities - cognitive') \
                      .str.replace(r'(^A mental.*)', 'disabilities - mental health') \
                      .str.replace(r'(^A sensory.*)', 'disabilities - sensory') \
                      .str.replace(r'(^A hearing.*)', 'disabilities - hearing') \
                      .str.replace(r'(^A seeing.*)', 'disabilities - vision') \
                      .str.replace(r'(^A mobility.*)', 'disabilities - mobility') \
                      .str.replace(r'(^An issue with.*)', 'disabilities - flexibility') \
                      .str.replace(r'(^Other.*)', 'disabilities - other')
    df.pop("DESCRIP_E")
    return df
    
def Regexp_descrip_subset4(df):
    '''
    purpose: build a column named DESCRIP by applying regular expression techniques to the DESCRIP_E column to clean up the categories and pop out the DESCRIP_E column in the end
    
    subset4: occupational group and level
    '''
    
    df["DESCRIP"] = df.loc[:, "DESCRIP_E"] \
                     .str.replace(r'(01$|02$)', 'junior') \
                     .str.replace(r'(03$|04$|05$)', 'senior') \
                     .str.replace(r'(06$)', 'export') \
                     .str.replace(r'(07$)', 'manager')
    df.pop("DESCRIP_E")
    return df

def Regexp_descrip_subset6(df):
    '''
    purpose: build a column named DESCRIP by applying regular expression techniques to the DESCRIP_E column to clean up the categories and pop out the DESCRIP_E column in the end
    
    subset6: province/territory of work, first official language, language requirements, service to public, bilingual areas of work. 
    '''
    df["DESCRIP"] = df.loc[:, "DESCRIP_E"] \
                        .str.replace(r'(^The bilingual region of Montr�al.*)', 'The bilingual region of Montreal')    
    df.pop("DESCRIP_E")
    return df
    
def Regexp_descrip_subset7(df):
    '''
    purpose: build a column named DESCRIP by applying regular expression techniques to the DESCRIP_E column to clean up the categories and pop out the DESCRIP_E column in the end
    
    subset7: organizational structure
    '''
    df["DESCRIP"] = df.loc[:, "DESCRIP_E"].str.split('-', n=1, expand=True)[0] \
    									  .str.replace(r'(Patent Branch|.*CIPO.*)', 'Canadian Intellectual Property Office (CIPO)') \
    							          .str.replace(r'(.*SIPS.*|RO)', 'Strategy and Innovation Policy Sector (SIPS)') \
    							          .str.replace(r'(.*SBMS.*|OSB)', 'Small Business and Marketplace Services Sector (SBMS)') \
    							          .str.replace(r'(.*CMS.*|HRB|CFSPB)', 'Corporate Management Sector (CMS)') \
    							          .str.replace(r'(.*STS.*|SMOB|CRC)', 'Spectrum and Telecommunications Sector (STS)') \
    							          .str.replace(r'(.*DTSS.*|CIO)', 'Digital Transformation Service Sector (DTSS)') \
    							          .str.replace(r'(.*CB.*|COB)', 'Competition Bureau (CB)') \
    							          .str.replace(r'(.*ICS.*|.*Innovation,.*)', 'Innovation, Science and Economic Development Canada (ISED)') \
    							          .str.replace(r'(.*SRS.*)', 'Science and Research Sector (SRS)') \
    							          .str.replace(r'(.*DMO.*)', "Deputy Minister's Office (DMO)") \
    							          .str.replace(r'(.*IS.*)', 'Industry Sector (IS)') \
    							          .str.replace(r'(MC)', 'MC-NCR Engineering and Laboratory Services') \
    							          .str.replace(r'(CC)', 'CC- Incorporations and Information Products and Services')
    df.pop("DESCRIP_E")
    return df
    
def concat_dfs():
    '''
    purpose: connect functions ISED_Data, general_descrip_subsets1_5, and Regexp_descrip_subset to concat all the output dataframes into one dataframe for future analysis
    '''
    df1, df2, df3, df4, df5, df6, df7 = ISED_Data()
    df1_new, df5_new = general_descrip_subsets1_5(df=df1), general_descrip_subsets1_5(df=df5)
    df2_new, df3_new, df4_new, df6_new, df7_new = Regexp_descrip_subset2(df=df2), Regexp_descrip_subset3(df=df3), Regexp_descrip_subset4(df=df4), Regexp_descrip_subset6(df=df6), Regexp_descrip_subset7(df=df7)

    dfs = pd.concat([df1_new, df2_new, df3_new, df4_new, df5_new, df6_new, df7_new], axis=0)
    return dfs
