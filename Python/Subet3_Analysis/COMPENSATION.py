# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 10:25:22 2022

@author: Daniel
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 13:33:53 2022

@author: danhu
"""

import pandas as pd
import static_frame as sf #pip install --user static-frame
from datetime import datetime
import numpy as np
import time

datafilename = 'subset_3_ISED.csv'

datafile = sf.Frame.from_pandas(pd.read_csv(datafilename))


class DataHandler():
    def __init__(self, dataframe):
        # full dataframe
        self.obj = dataframe
        
    def GetData_ByYear(self, year):
        return self.obj.loc[self.obj['SURVEYR'] == int(year)]
        
    
    def GetData_ByQuestionNum(self, number):
        if len(str(number)) == 1:
            number = '0' + str(number)
        else:
            number = str(number)
        return self.obj.loc[self.obj['QUESTION'] == 'Q{}'.format(number)]
    
    
    def GetData_ByDemographicCondition(self, conditionstring):
        try:
            return self.obj.loc[self.obj['BYCOND'] == '{}'.format(conditionstring)]
        except:
            print('<ERROR> Unable to query dataframe. Ensure you have entered the function argument correctly.')
            print("e.g. <DataStructure>.GetDataByDemographicCondition('Q115 = 1')")
    
    #use these functions to filter you master dataset
    
    def GetData_Gender_Male(self): ##
        # return self.obj[self.obj['BYCOND'] == "Q115 = 1"]
        return self.obj.loc[self.obj['BYCOND'] == "Q115 = 1"]
    
    def GetData_Gender_Female(self):
        # return self.obj[self.obj['BYCOND'] == "Q115 = 2"]
        return self.obj.loc[self.obj['BYCOND'] == "Q115 = 2"]
    
    def GetData_Gender_Diverse(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q115 = 3']
    
    def GetData_Indigeneous(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q116 = 1']

    def GetData_Indigeneous_C(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q116 = 2']
  
    def GetData_FirstNation(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q117 = 1']

    def GetData_Metis(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q117 = 2']    
    
    def GetData_Disability_General(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q118 = 1']
    
    def GetData_Disability_General_C(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q118 = 2']

    def GetData_Disability_Vision(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q119A = 1']

    def GetData_Disability_Vision_C(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q119A = 2']
    
    def GetData_Disability_Hearing(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q119B = 1']

    def GetData_Disability_Hearing_C(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q119B = 2']
    
    def GetData_Disability_Mobility(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q119C = 1']

    def GetData_Disability_Mobility_C(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q119C = 2']
    
    def GetData_Disability_Dexterity(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q119D = 1']

    def GetData_Disability_Dexterity_C(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q119D = 2']
    
    def GetData_Disability_MentalHealth(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q119E = 1']

    def GetData_Disability_MentalHealth_C(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q119E = 2']

    def GetData_Disability_Sensory(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q119F = 1']

    def GetData_Disability_Sensory_C(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q119F = 2']

    def GetData_Disability_Chronic(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q119G = 1']

    def GetData_Disability_Chronic_C(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q119G = 2']

    def GetData_Disability_Cognitive(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q119H = 1']

    def GetData_Disability_Cognitive_C(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q119H = 2']
    
    def GetData_Disability_Intellectual(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q119I = 1']

    def GetData_Disability_Intellectual_C(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q119I = 2']
    
    def GetData_Disability_Other(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q119J = 1']

    def GetData_Disability_Other_C(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q119J = 2']

    def GetData_VisibleMinority_General(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q120 = 1']

    def GetData_VisibleMinority_General_C(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q120 = 2']

    def GetData_VisibleMinority_Black(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q121A = 1']

    def GetData_VisibleMinority_Black_C(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q121A  = 2']
    
    def GetData_VisibleMinority_Chinese(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q121B = 1']

    def GetData_VisibleMinority_Chinese_C(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q121B = 2']

    def GetData_VisibleMinority_Filipino(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q121C = 1']

    def GetData_VisibleMinority_Filipino_C(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q121C = 2']

    def GetData_VisibleMinority_Japanese(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q121D = 1']

    def GetData_VisibleMinority_Japanese_C(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q121D = 2']
    
    def GetData_VisibleMinority_Korean(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q121E = 1']

    def GetData_VisibleMinority_Korean_C(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q121E = 2']
    
    def GetData_VisibleMinority_SouthAsian(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q121F = 1']

    def GetData_VisibleMinority_SouthAsian_C(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q121F = 2']
    
    def GetData_VisibleMinority_SoutheastAsian(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q121G = 1']

    def GetData_VisibleMinority_SoutheastAsian_C(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q121G = 2']
    
    def GetData_VisibleMinority_WestAsian(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q121H = 1']

    def GetData_VisibleMinority_WestAsian_C(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q121H = 2']

    def GetData_VisibleMinority_LatinAmerican(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q121I = 1']

    def GetData_VisibleMinority_LatinAmerican_C(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q121I = 2']

    def GetData_VisibleMinority_MixedOrigin(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q121J = 1']

    def GetData_VisibleMinority_MixedOrigin_C(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q121J = 2']
    
    def GetData_VisibleMinority_Other(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q121K = 1']

    def GetData_VisibleMinority_Other_C(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q121K = 2']

    def GetData_Sexuality_Heterosexual(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q122 = 1']

    def GetData_Sexuality_Homosexual(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q122 = 2']

    def GetData_Sexuality_Bisexual(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q122 = 3']
    
    def GetData_Sexuality_Xsexual(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q122 = 4']

    def GetData_Sexuality_NoAnswer(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q122 = 5']
    
    def Show_Indicators(self):
        return list(self.obj['INDICATORENG'].unique())

    def GetData_ByIndicator(self, indicator):
        indicators = self.Show_Indicators()
        if str(indicator) in indicators:
            return self.obj.loc[self.obj['INDICATORENG'] == '{}'.format(indicator)]
        else:
            print('You must pass a valid indicator as a string. Use the Show_Indicators() method to show options.')
            
    def Show_Subindicators(self):
        return list(self.obj.SUBINDICATORENG.unique())

    def GetData_BySubindicator(self, subindicator):
        subindicators = self.Show_Subindicators()
        if str(subindicator) in subindicators:
            return self.obj.loc[self.obj['SUBINDICATORENG'] == '{}'.format(subindicator)]
        else:
            print('You must pass a valid subindicator as a string. Use the Show_Subindicators() method to show options.')
            
            
 
run = 1

if run == 1:
    
    
    
       
    # begin data anaylsis
    print('Will now begin data anlaysis.')
    df = DataHandler(datafile)
    
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print('{}   |   <Discarding data from previous years.>'.format(now))        
    time.sleep(0.5)
    print('-----------------------------------------------------')
    df = DataHandler(df.GetData_ByYear(2020))
    print('-----------------------------------------------------')    
    
    
    # bin data by indicators
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print('{}   |   <Binning data by indicator.>'.format(now))        
    print('-----------------------------------------------------')
    df_indicator_list = df.Show_Indicators()
    print('Current Indicator is COMPENSATION.')
    print('-----------------------------------------------------')
    time.sleep(0.5)
    df_i = {}
    for i in range(len(df_indicator_list)):
        df_i[df_indicator_list[i]] = DataHandler(df.GetData_ByIndicator(df_indicator_list[i]))
    time.sleep(0.5)    
    

    
    def weighted_average_score(scorecol, numcol):

        holder_score = np.zeros(len(scorecol))
        holder_num = np.zeros(len(scorecol))
        
        scoreindx = scorecol.index
        numindx = numcol.index
        
        for i in range(len(scorecol)):
            if scorecol[scoreindx[i]] == '9999' or scorecol[scoreindx[i]] == ' ' or scorecol[scoreindx[i]] == None:
                holder_score[i] = 0
            else:
                holder_score[i] = scorecol[scoreindx[i]]
                
        for i in range(len(numcol)):
            if numcol[numindx[i]] == '9999' or numcol[numindx[i]] == ' ' or numcol[numindx[i]] == None:
                holder_num[i] = 0
            else:
                holder_num[i] = numcol[numindx[i]]
                        
        
        for i in range(len(scorecol)):
            if holder_score[i] == 0:
                holder_num[i] = 0
                
        for i in range(len(numcol)):
            if holder_num[i] == 0:
                holder_score[i] = 0
            
        
        population = sum(holder_num)
        out = np.array(np.zeros(len(numcol)))
        for i in range(len(numcol)):
            out[i] = holder_score[i] * holder_num[i]
        out = sum(np.array(out)) / population
            
        
        return round(out, 2)

    def get_intersection(frameA, frameB):
        a_array = np.array(frameA.index)
        b_array = np.array(frameB.index)
        return np.intersect1d(a_array, b_array)
    
    def drop_intersection(frameA, frameB): #removes the intersection of two frames from the first frame
        intersection = get_intersection(frameA, frameB)
        for i in range(len(intersection)):
            frameA = frameA.drop.loc[intersection[i]]    
        return [frameA, frameB]

    def create_intersection_frame(frameA, frameB):
        intersection_indx = get_intersection(frameA, frameB)
        out = frameA.loc[intersection_indx[0]]
        for indx in intersection_indx[1::]:
            out = sf.Frame.from_concat([out, frameA.loc[indx]])
        return out        
        

    
    # create a list of macro indicators
    macro_group_list = ['Gender', 'Indigeneous', 'Disability', 'VisibleMinority', 'Sexuality']
    
    macro_Gender = {'_Male' : 0, '_Female' : 0}#, '_Diverse' : 0} --> ISED has no employees who identified as Gender Diverse.
    macro_Indigeneous = {'' : 0, '_C' : 0}
    macro_Disability = {'_General' : 0, '_General_C' : 0}
    macro_VisibleMinority = {'_General' : 0, '_General_C' : 0}
    macro_Sexuality = {'_Heterosexual' : 0, '_Homosexual' : 0, '_Bisexual' : 0, '_Xsexual' : 0 ,'_NoAnswer' : 0}
    
    #create list of subdivisions for each macro indicator
    macro_subgroups = [macro_Gender, macro_Indigeneous, macro_Disability, macro_VisibleMinority, macro_Sexuality]
    
    #create a dict to map macro indicators to their subdivisions
    macro_groups = {macro_group_list[i] : macro_subgroups[i] for i in range(len(macro_group_list))}
    
    # create nested dictionary. Keys are the indicators, values are the macro groups
    # macro groups are themselves dicitonaries whose values are the group subdivisions

    
    df_COMPENSATION = df.GetData_ByIndicator('COMPENSATION')
    dict_COMPENSATION = {}
    for i, group in enumerate(macro_group_list):
        dict_COMPENSATION[group] = eval('macro_{}'.format(group))
        for j,subgroup in enumerate(list(dict_COMPENSATION[group].keys())):
            targetdf = eval('df.GetData_' + group + subgroup + '()')
            outdf = create_intersection_frame(df_COMPENSATION, targetdf)
            dict_COMPENSATION[group][subgroup] = outdf
            del outdf

    
    # copy for immutable dataframe
    macro_group_list = ['Gender', 'Indigeneous', 'Disability', 'VisibleMinority', 'Sexuality']
    
    macro_Gender = {'_Male' : 0, '_Female' : 0}#, '_Diverse' : 0} --> ISED has no employees who identified as Gender Diverse.
    macro_Indigeneous = {'' : 0, '_C' : 0}
    macro_Disability = {'_General' : 0, '_General_C' : 0}
    macro_VisibleMinority = {'_General' : 0, '_General_C' : 0}
    macro_Sexuality = {'_Heterosexual' : 0, '_Homosexual' : 0, '_Bisexual' : 0, '_Xsexual' : 0 ,'_NoAnswer' : 0}
    
    #create list of subdivisions for each macro indicator
    macro_subgroups = [macro_Gender, macro_Indigeneous, macro_Disability, macro_VisibleMinority, macro_Sexuality]
    
    #create a dict to map macro indicators to their subdivisions
    macro_groups = {macro_group_list[i] : macro_subgroups[i] for i in range(len(macro_group_list))}
    
    
    df_COMPENSATION = df.GetData_ByIndicator('COMPENSATION')
    COMPENSATION_was = {}
    for i, group in enumerate(macro_group_list):
        COMPENSATION_was[group] = eval('macro_{}'.format(group))
        for j,subgroup in enumerate(list(dict_COMPENSATION[group].keys())):
            staticscore = dict_COMPENSATION[group][subgroup]['SCORE100']
            staticcount = dict_COMPENSATION[group][subgroup]['ANSCOUNT']
            was = weighted_average_score(staticscore, staticcount)
            COMPENSATION_was[group][subgroup] = was
            del staticcount
            del staticscore
    
    print(COMPENSATION_was)

                        
    
else: 
    print('Data analysis skipped.')




        
    