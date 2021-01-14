# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 15:39:19 2021
"""

import json
import numpy

##Import Json file

with open("Raw_Data.json") as f:
    BMI_Raw_Data=json.load(f)

##Calculate BMI

for d in BMI_Raw_Data:
    d['BMI_val']=(d['WeightKg']/((d['HeightCm']/100)**2))
    d['BMI_val']=numpy.round_(d['BMI_val'],decimals=1)
    if d['BMI_val']<=18.40:
        d['BMI_Category']="Underweight"
        d['Health_Risk']="Malnutrition"
    elif d['BMI_val']>=18.5 and d['BMI_val']<=24.9:
        d['BMI_Category']="Normal Weight"
        d['Health_Risk']="Low Risk"
    elif d['BMI_val']>=25 and d['BMI_val']<=29.9:
        d['BMI_Category']="Overweight"
        d['Health_Risk']="Enhanced risk"
    elif d['BMI_val']>=30.0 and d['BMI_val']<=34.9:
        d['BMI_Category']="Moderately obese"
        d['Health_Risk']="Medium risk"
    elif d['BMI_val']>=35 and d['BMI_val']<=39.9:
        d['BMI_Category']="Severely obese"
        d['Health_Risk']="High risk"
    else:
        d['BMI_Category']="Very severely obese"
        d['Health_Risk']="Very high risk"
        
