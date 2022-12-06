# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 22:58:53 2022

@author: kjide
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#ClimateChange = pd.read_excel('climate change.xls')
#print(ClimateChange)

# Define functions
def readfile(doc):
    filedata = pd.read_excel(doc , skiprows = 3)
    return filedata, filedata.transpose()


Climate_Change = readfile('climate change.xls')
print(Climate_Change)


UrbanPop = Climate_Change[1].iloc[4:,[989, 2205, 2661, 3041, 4181, 13225, 9197]]
#print(UrbanPop)
UrbanPop = UrbanPop.reset_index()
#print(UrbanPop)
UrbanPop = UrbanPop.set_axis(["Year", "Australia", "Brazil", "Canada", 
                              "China", "Germany", "Nigeria", "Kenya"], axis=1)
print(UrbanPop)


Methane_Emissions = Climate_Change[1].iloc[4:,[1018, 2234, 2690, 3070, 4210, 13254, 9226]]
#print(Methane_Emissions)
Methane_Emissions = Methane_Emissions.reset_index()
#print(Methane_Emissions)
Methane_Emissions = Methane_Emissions.set_axis(["Year", "Australia", "Brazil", "Canada", 
                                                "China", "Germany", "Nigeria", "Kenya"], axis=1)
Methane_Emissions = Methane_Emissions = Methane_Emissions.dropna(axis=0)
print(Methane_Emissions)


CO2_Emissions = Climate_Change[1].iloc[4:,[1032, 2248, 2704, 3084, 4224, 13268, 9240]]
#print(CO2_Emissions)
CO2_Emissions = CO2_Emissions.reset_index()
#print(CO2_Emissions)
CO2_Emissions = CO2_Emissions.set_axis(["Year", "Australia", "Brazil", "Canada", 
                                        "China", "Germany", "Nigeria", "Kenya"], axis=1)
CO2_Emissions = CO2_Emissions = CO2_Emissions.dropna(axis=0)
print(CO2_Emissions)


Agric_Land = Climate_Change[1].iloc[4:,[1062, 2278, 2734, 3114, 4254, 13298, 9270]]
#print(Agric_Land)
Agric_Land = Agric_Land.reset_index()
#print(Agric_Land)
Agric_Land = Agric_Land.set_axis(["Year", "Australia", "Brazil", "Canada", 
                                  "China", "Germany", "Nigeria", "Kenya"], axis=1)
Agric_Land = Agric_Land = Agric_Land.dropna(axis=0)
print(Agric_Land)


Access_Elect = Climate_Change[1].iloc[4:,[1049, 2265, 2721, 3101, 4241, 13285, 9257]]
#print(Access_Elect)
Access_Elect = Access_Elect.reset_index()
#print(Access_Elect)
Access_Elect = Access_Elect.set_axis(["Year", "Australia", "Brazil", "Canada", 
                                      "China", "Germany", "Nigeria", "Kenya"], axis=1)
Access_Elect = Access_Elect = Access_Elect.dropna(axis=0)
print(Access_Elect)


Elect_Power_Cons = Climate_Change[1].iloc[4:,[1038, 2254, 2710, 3090, 4230, 13274, 9246]]
#print(Elect_Power_Cons)
Elect_Power_Cons = Elect_Power_Cons.reset_index()
#print(Elect_Power_Cons)
Elect_Power_Cons = Elect_Power_Cons.set_axis(["Year", "Australia", "Brazil", "Canada", 
                                              "China", "Germany", "Nigeria", "Kenya"], axis=1)
Elect_Power_Cons = Elect_Power_Cons = Elect_Power_Cons.dropna(axis=0)
print(Elect_Power_Cons)

