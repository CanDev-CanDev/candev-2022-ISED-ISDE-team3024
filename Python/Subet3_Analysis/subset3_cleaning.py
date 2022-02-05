# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 13:33:53 2022

@author: danhu
"""

import pandas as pd
import numpy as np

datafile = 'subset_3_ISED.csv'


class DataHandler():
    def __init__(self, datafile):
        self.obj = pd.read_csv(datafile)
        
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
    
    def GetData_Males(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q115 = 1']
    
    def GetData_Females(self):
        return self.obj.loc[self.obj['BYCOND'] == 'Q115 = 1']
    
    def GetData_GenderDiverse(self):
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
        return list(self.obj.INDICATORENG.unique())

    def GetData_ByIndicator(self, indicator):
        indicators = self.Show_Indicators()
        if indicator in indicators == True:
            return self.obj.loc[self.obj['INDICATORENG'] == '{}'.format(indicator)]
        else:
            print('You must pass a valid indicator as a string. Use the Show_Indicators() method to show options.')
            
    def Show_Subindicators(self):
        return list(self.obj.SUBINDICATORENG.unique())

    def GetData_BySubindicator(self, subindicator):
        subindicators = self.Show_Subindicators()
        if subindicator in subindicators == True:
            return self.obj.loc[self.obj['SUBINDICATORENG'] == '{}'.format(subindicator)]
        else:
            print('You must pass a valid subindicator as a string. Use the Show_Subindicators() method to show options.')
#            
#    def Percent_Positive_by_Demographic_and_Indicator():







        
    