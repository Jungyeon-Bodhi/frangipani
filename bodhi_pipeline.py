#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Bodhi Global Analysis (Jungyeon Lee)
"""

import bodhi_indicator as bd
import bodhi_PMF as pmf
import pandas as pd

"""
Evaluation
"""
# Specify the file path for the clean dataset
df = pd.read_excel('data/24-SFCG-GLO-2 - Data_cleaned.xlsx')
indicators = []

# Create indicators and provide additional details as needed (Evaluation)
def statistics(df, indicators):
    
    category = bd.Indicator(df, "Respondent category", 0, ['1'], i_cal=None, i_type='count', description='Respondent Category', period='midline', target = None)
    category.add_var_order(["Women in Action participant",
                            "Listening Club member"])
    indicators.append(category)
    
    age = bd.Indicator(df, "Respondent Age Group", 0, ['Age Group'], i_cal=None, i_type='count', description='Respondent Age Group', period='midline', target = None)
    age.add_breakdown({'1':'Category'})
    age.add_var_order(["18-25",
                       "26-35",
                       "36-55",
                       "56+"])
    indicators.append(age)
    
    province = bd.Indicator(df, "Respondent Province", 0, ['4'], i_cal=None, i_type='count', description='Respondent Province', period='midline', target = None)
    province.add_breakdown({'1':'Category', "Age Group":"Age Group"})
    province.add_var_order(["Muyinga",
                            "Makamba",
                            "Rumonge",
                            "Kayanza"])
    indicators.append(province)
    
    sex = bd.Indicator(df, "Respondent Sex", 0, ['3'], i_cal=None, i_type='count', description='Respondent Sex', period='midline', target = None)
    sex.add_breakdown({'1':'Category', "Age Group":"Age Group", "4":"Province"})
    sex.add_var_order(["Female",
                       "Male"])
    indicators.append(sex)
    
    community = bd.Indicator(df, "Respondent Community", 0, ['5'], i_cal=None, i_type='count', description='Respondent Community', period='midline', target = None, visual=False)
    community.add_breakdown({'1':'Category', "Age Group":"Age Group", "3":"Sex", "4":"Province"})
    indicators.append(community)
    
    disability = bd.Indicator(df, "Respondent Disability Status", 0, ['Disability'], i_cal=None, i_type='count', description='Respondent Disability Status', period='midline', target = None)
    disability.add_breakdown({'1':'Category', "Age Group":"Age Group", "3":"Sex", "4":"Province"})
    disability.add_var_order(["No Disability",
                              "Disability"])
    indicators.append(disability)
    
    occupation = bd.Indicator(df, "Respondent Occupation", 0, ['10'], i_cal=None, i_type='count', description='Respondent Occupation', period='midline', target = None, visual=False)
    occupation.add_breakdown({'1':'Category', "Age Group":"Age Group", "3":"Sex", "4":"Province", "Disability":"Disability"})
    indicators.append(occupation)
    
    marital = bd.Indicator(df, "Respondent Marital", 0, ['11'], i_cal=None, i_type='count', description='Respondent Marital', period='midline', target = None, visual=False)
    marital.add_breakdown({'1':'Category', "Age Group":"Age Group", "3":"Sex", "4":"Province", "Disability":"Disability"})
    indicators.append(marital)
    
    economic_group = bd.Indicator(df, "Economic Group", 0, ['18'], i_cal=None, i_type='count', description='Respondent Economic Group', period='midline', target = None)
    economic_group.add_breakdown({'1':'Category', "Age Group":"Age Group", "3":"Sex", "4":"Province", "Disability":"Disability"})
    economic_group.add_var_order(["Yes",
                                  "No"])
    indicators.append(economic_group)   
    
    civil_group = bd.Indicator(df, "Civil Group", 0, ['19'], i_cal=None, i_type='count', description='Respondent Civil Society Organisation', period='midline', target = None)
    civil_group.add_breakdown({'1':'Category', "Age Group":"Age Group", "3":"Sex", "4":"Province", "Disability":"Disability"})
    civil_group.add_var_order(["Yes","No"])
    indicators.append(civil_group)   
    
    safe = bd.Indicator(df, "Feel_Safe", 0, ['feel_safe'], i_cal=None, i_type='count', description="Feel Safe Indicator", period='midline', target = None)
    safe.add_breakdown({'1':'Category', "Age Group":"Age Group", "3":"Sex", "4":"Province", "Disability":"Disability"})
    safe.add_var_order(["Very safe",
                        "Safe",
                        "Moderate",
                        "Unsafe",
                        "Not at all safe"])
    indicators.append(safe)  
    
    lnd12 = bd.Indicator(df, "lnd.1.2", 0, ['21'], i_cal=None, i_type='count', description="Ind.1.2: % of listeners (M/F) of media programs produced within the framework of the project who demonstrate \ntheir support for the inclusion of women in the economy and for gender equality, compared to non-listeners", period='midline', target = None)
    lnd12.add_breakdown({'1':'Category', "Age Group":"Age Group", "3":"Sex", "4":"Province", "Disability":"Disability"})
    lnd12.add_var_order(["Yes","No"])
    indicators.append(lnd12)  
    
    lnd12_1 = bd.Indicator(df, "lnd.1.2_1", 0, ['20'], i_cal=None, i_type='count', description="Have you benefited from the media programs and awareness-raising activities carried out by Search for Common Ground as part of the ‘Je na We mw'iterambere’ project?", period='midline', target = None, visual=False)
    lnd12_1.add_breakdown({'1':'Category', "Age Group":"Age Group", "3":"Sex", "4":"Province", "Disability":"Disability"})
    lnd12_1.add_var_order(["Yes, often",
                           "Yes, sometimes",
                           "Yes, but rarely",
                           "Yes, but very rarely",
                           "No, never"])
    indicators.append(lnd12_1)  
    
    lnd12_2 = bd.Indicator(df, "lnd.1.2_2", 0, ['23'], i_cal=None, i_type='count', description="If yes, what was the contribution of the project‘Je na We mw'iterambere’/de Search to these initiatives?", period='midline', target = None, visual=False)
    lnd12_2.add_breakdown({'1':'Category', "Age Group":"Age Group", "3":"Sex", "4":"Province", "Disability":"Disability"})
    lnd12_2.add_var_order(["No contribution, the initiatives developed independently of the project",
                           "The project made a small contribution to these initiatives",
                           "The project had a moderate contribution to these initiatives",
                           "A strong contribution - these initiatives would not exist without the project",
                           "Unsure"])
    indicators.append(lnd12_2)
    
    lnd12_3 = bd.Indicator(df, "lnd.1.2_3", 0, ['24'], i_cal=None, i_type='count', description="What do you think about the inclusion of women in the economic life of your community in relation to the development of the whole community ?", period='midline', target = None, visual=False)
    lnd12_3.add_breakdown({'1':'Category', "Age Group":"Age Group", "3":"Sex", "4":"Province", "Disability":"Disability"})
    lnd12_3.add_var_order(["Very important or essential",
                           "Important or essential",
                           "Moderately important or essential",
                           "Not at all important or essential",
                           "The project had a detrimental effect on these initiatives"])
    indicators.append(lnd12_3)

    lnd13 = bd.Indicator(df, "lnd.1.3", 0, ['Ind1.3'], i_cal=None, i_type='count', description="Ind.1.3: % of targeted CSO members (F/M) who report regularly interacting with \nthe media to transform discriminatory social norms and cultural barriers for women", period='midline', target = None)
    lnd13.add_breakdown({'1':'Category', "Age Group":"Age Group", "3":"Sex", "4":"Province", "Disability":"Disability"})
    lnd13.add_var_order(["Adequate","Inadequate"])
    indicators.append(lnd13)  
    
    df_women = df[df["3"] == "Female"].copy()
    
    lnd21 = bd.Indicator(df_women, "lnd.2.1", 0, ['Ind2.1'], i_cal=None, i_type='count', description="Ind.2.1: % targeted women who believe they can make a positive difference \nin the economic empowerment of women in their community", period='midline', target = None)
    lnd21.add_breakdown({'1':'Category', "Age Group":"Age Group", "3":"Sex", "4":"Province", "Disability":"Disability"})
    lnd21.add_var_order(["Adequate","Inadequate"])
    indicators.append(lnd21)
    
    lnd21_1 = bd.Indicator(df_women, "lnd.2.1_1", 0, ['26'], i_cal=None, i_type='count', description="Does your business activity contribute to increased investment and economic profitability in your household?", period='midline', target = None)
    lnd21_1.add_breakdown({'1':'Category', "Age Group":"Age Group", "3":"Sex", "4":"Province", "Disability":"Disability"})
    lnd21_1.add_var_order(["Strongly agree",
                           "Agree",
                           "Neither agree nor disagree",
                           "Disagree",
                           "Strongly disagree"])
    indicators.append(lnd21_1)
    
    lnd22 = bd.Indicator(df_women, "lnd.2.2", 0, ['Ind2.2'], i_cal=None, i_type='count', description="Ind.2.2: % of women and young girl “entrepreneurs” supported by \nthe project who have significantly higher incomes/savings at the end of the project", period='midline', target = None)
    lnd22.add_breakdown({'1':'Category', "Age Group":"Age Group", "3":"Sex", "4":"Province", "Disability":"Disability"})
    lnd22.add_var_order(["Adequate","Inadequate"])
    indicators.append(lnd22)
    
    lnd22_1 = bd.Indicator(df, "lnd.2.2_1", 0, ['31'], i_cal=None, i_type='count', description="In your opinion, what are the main obstacles which limit the economic autonomy of women in your community ?", period='midline', target = None, visual= False)
    lnd22_1.add_breakdown({'1':'Category', "Age Group":"Age Group", "3":"Sex", "4":"Province", "Disability":"Disability"})
    lnd22_1.add_var_order(["Restrictive social norms regarding the role of women in society",
                           "Gender discrimination in the labor market",
                           "Lack of family support for women's entrepreneurial initiatives",
                           "Constraints related to family and domestic responsibilities",
                           "Limited access to financial resources or investment opportunities for women",
                           "Lack of capacity to carry out",
                           "Economic activities",
                           "Other"])
    indicators.append(lnd22_1)
    
    lnd23 = bd.Indicator(df_women, "lnd.2.3", 0, ['Ind2.3'], i_cal=None, i_type='count', description="Ind.2.3: % of women and young girl entrepreneurs targeted by the project \nwho report having a better support network to increase their autonomy following their participation in the project", period='midline', target = None)
    lnd23.add_breakdown({'1':'Category', "Age Group":"Age Group", "3":"Sex", "4":"Province", "Disability":"Disability"})
    lnd23.add_var_order(["Adequate","Inadequate"])
    indicators.append(lnd23)
    
    pip_1 = bd.Indicator(df, "PIP_1", 0, ['33'], i_cal=None, i_type='count', description="To what extent do you agree with this statement: I feel that my voice and opinion are taken into account in the project.", period='midline', target = None)
    pip_1.add_breakdown({'1':'Category', "Age Group":"Age Group", "3":"Sex", "4":"Province", "Disability":"Disability"})
    pip_1.add_var_order(["Strongly agree",
                           "Agree",
                           "Neither agree nor disagree",
                           "Disagree",
                           "Strongly disagree"])
    indicators.append(pip_1)
    
    pip_2 = bd.Indicator(df, "PIP_2", 0, ['38'], i_cal=None, i_type='count', description="Do you know how to report any harm or concerns that you or someone else \nmay have experienced while participating in the activity/project?", period='midline', target = None)
    pip_2.add_breakdown({'1':'Category', "Age Group":"Age Group", "3":"Sex", "4":"Province", "Disability":"Disability"})
    pip_2.add_var_order(["Yes",
                         "No"])
    indicators.append(pip_2)
    
    return indicators
    
# Create indicators for several statistical tests such as OLS, ANOVA, T-test and Chi2
def statistical_indicators(df, indicators):
    feel_safe = bd.Indicator(df, "Feel Safe", 0, ['36'], i_cal=None, i_type='count', description='On a scale of 1 to 5 (5 = very safe, 1 = not at all safe), how safe do you feel participating in the project?', s_test = 'stats', s_group = {'1':'Category', "Age Group":"Age Group", "3":"Sex", "4":"Province", "Disability":"Disability"})
    indicators.append(feel_safe)
    
    income = bd.Indicator(df, "Income", 0, ['28'], i_cal=None, i_type='count', description="Before the intervention, what was your monthly income?", s_test = 'stats', s_group = {'1':'Category', "Age Group":"Age Group", "3":"Sex", "4":"Province", "Disability":"Disability"})
    indicators.append(income)
    
    income_change = bd.Indicator(df, "Income Change", 0, ['30'], i_cal=None, i_type='count', description="If yes, what percentage change has there been?", s_test = 'stats', s_group = {'1':'Category', "Age Group":"Age Group", "3":"Sex", "4":"Province", "Disability":"Disability"})
    indicators.append(income_change)
    return indicators

# Create the PMF class ('Project Title', 'Evaluation')
frangipani = pmf.PerformanceManagementFramework('Frangipani', 'Evaluation')

indicators = statistics(df, indicators)
indicators = statistical_indicators(df, indicators)
frangipani.add_indicators(indicators)

file_path1 = 'data/24-SFCG-GLO-1 - Statistics.xlsx' # File path to save the statistics (including breakdown data)
file_path2 = 'data/24-SFCG-GLO-1 - Test Results.xlsx'  # File path to save the chi2 test results
folder = 'visuals/' # File path for saving visuals
frangipani.PMF_generation(file_path1, file_path2, folder) # Run the PMF
