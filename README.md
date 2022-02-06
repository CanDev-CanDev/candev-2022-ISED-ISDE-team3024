# TeamMcTeamFace


DESCRIPTION:

This repository contains Python files to filter data from StatCan's public service employee survey (Subset 3).

Data analysis focused on identifying weighted average Indicator scores (out of 100) for Innovation, Science, and Economic Development Canada (ISED).

The six Indicators of interest are:

COMPENSATION, EMPLOYEE ENGAGEMENT, LEADERSHIP, WORKFORCE, WORKPLACE, WORKPLACE WELL-BEING

These Indicators are groupings of questions in the Survey. The Dataset includes a score out of 100 for each demographic group for each question. This repository contains code to filter, manipulate, and obtain specific data of the information contained in Subset 3.


----------------------------------------

AUTHORS:

An Ni Guo, Varun Mehta, Yuqi (Yumi) Xiang, Daniel Hutama

----------------------------------------

USAGE:

Running any of the <INDICATORNAME>.py functions will create a dictionary that contains the weighted averages score for certain demographic groups using data from the 2020 survey.

For instance, running COMPENSATION.py yields the following dictionary:
  
{'Gender': {'_Male': 66.84, '_Female': 64.0}, 'Indigeneous': {'': 60.04, '_C': 64.98}, 'Disability': {'_General': 57.81, '_General_C': 65.14}, 'VisibleMinority': {'_General': 66.76, '_General_C': 63.93}, 'Sexuality': {'_Heterosexual': 66.25, '_Homosexual': 64.56, '_Bisexual': 59.9, '_Xsexual': 61.25, '_NoAnswer': 58.51}}

The scores give an indication on ISED's performance in the COMPENSATION indicator for each demographic group listed. 

E.g. ISED emplopees who identify as male give a score of 66.84/100. Employees who identify as Bisexual give a score of 59.9/100. 

Employees with disabilities of any type give a score of 57.81/100, whereas the complement (indicated with 'C') give a score of 65.14. This allows the user to infer that job satisfaction for employees with disabilities may benefit from improved compensation.
  
----------------------------------------

COOL STUFF:
  
The python code to analyze the data throws the csv info into a dataframe, which is then thrown into a custom class. This class has methods which allow you to easily filter the data. For instance dataframe.Get_Gender_Male() returns all the rows of Subset 3 (or a subset of Subset 3) with the BYCOND column entry as "Q115 = 1."
  
Macro demographic groups, such as disabilities of vision, which were included with other disability types, can be explored in detail with the scripts found in the "Subset3_Lower_Level_Analysis" folder.
  
  
 ----------------------------------------

  COMPARISON WITH OTHER DEPARTMENTS
  
 The excel file needed for this functionality is too big for Github (413 MB). Please get in touch with me (Daniel Hutama) if you need the file. The needed file name is 'subset_3_ISED_C.csv'.  Since this is missing from the GitHub Repo, you will run into errors trying to run <INDICATORNAME_ALL>.py.
