#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Bodhi Global Analysis (Jungyeon Lee)
"""

"""
Please define the parameters for data preprocessing pipeline
"""
import bodhi_data_preprocessing as dp

project_name = "Joint Mid-term Evaluation of the Search-IPIS DGD Programme 2022-2026"

file_type = 'xlsx' 
# Original data format: xlsx, xls, csv

file_path = "Data/24-SFCG-GLO-2 - Raw Data"
# Original data location and name (excluding file extension): "Data/(name)"

file_path_others = "Data/24-SFCG-GLO-2 - Open-End.xlsx"
# Specify the path and name of the Excel sheet where the values from the open-ended columns will be saved (New file)
# For example: "Data/(project name) others.xlsx"

enumerator_name = 'E1'
respondent_name = None
# Original column name for respondents' names (for anonymisation and duplicate removal)

identifiers = ["_submission_time", 'today', '_id', '_uuid']
# Identifiers for detecting duplicates (list, do not remove respondent_name)
# Recommendation: At least three identifiers

dates = ["2025-03-18"] 
# Remove the dates on which the pilot test was conducted from the data
# for example ['2024-07-18', '2024-07-22', '2024-07-23']

cols_new = ['start','end','today','deviceid', "E1", 'E2', 'E3',
 "1", 'Age Group', '3', '4', '5-1', '5-2', '5-3', '5-4', '6', '7', "8", "8-o", "9",
 '9-o', '10', '10-o', '11', '11-o', '12', '13', '14', '15', '16', '17',
 '18', '19', "20", "21", '22', "23", '24', '25', '26', "27", '28', '29', '30', '31', '31-o',
 '32', '33', '34', '35', '36', '37', '38', '39', '_id', '_uuid', '_submission_time', '_validation_status',
 '_notes', '_status', '_submitted_by', '__version__', '_tags', '_index']
# Specify new column names for data analysis (ensure they match the exact order of the existing columns)

list_del_cols = ['start','end','today','deviceid', "E1", 'E2', 'E3']
# Specify the columns to be excluded from the data analysis

miss_col = ["1", '3', '4' ,'6', '12', '13', '14', '15', '16', '17','18','19']
# Specify all columns that apply to all respondents for missing value detection

open_cols = ["8-o",'9-o','10-o','11-o','22','31-o','35','37','39']
# Specify the open-ended columns (which will be saved in a separate Excel sheet and removed from the data frame)

age_col = None
# If we don't have age group in this dataset, please specify the age columns (as str)

diss_cols = ['12', '13', '14', '15', '16', '17']
# If we have WG-SS questions in the dataset, please specify the columns (as list [])


"""
Run the pipeline for data preprocessing
del_type = 0 or 1
-> 0: Remove all missing values from the columns where missing values are detected
-> 1: First, remove columns where missing values make up 10% or more of the total data points
      Then, remove all remaining missing values from the columns where they are detected
"""

frangipani = dp.Preprocessing(project_name, file_path, file_path_others, list_del_cols, dates, miss_col, respondent_name, enumerator_name, identifiers, open_cols, cols_new, age_col, diss_cols, del_type = 0, file_type=file_type)
frangipani.processing()