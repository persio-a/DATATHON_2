#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 13:46:04 2020

@author: maxfranco
"""


import pandas as pd
import numpy as np
import glob
import datetime as dt

df = pd.read_csv('Target_Data.csv')
df['key'] = df['Course'].astype(str)+df['Subject'].astype(str)

key_list = list(df['key'].unique())

for i in key_list:
    df[df['key']== i].to_csv('utk_dfs/df{}.csv'.format(i), index=False)
    
df2965 = df[df['key']== '2965']


df2965.to_csv('df2965.csv', index=False)


churn = pd.read_csv('churn.csv')

churn.columns


coverages = pd.read_excel('/Users/utkarsh/Desktop/Datathon_2/Data sets/Coverages.xlsx', index = False)
coverages = coverages.fillna(0)
coverages.isnull().sum()

coverages.columns
coverages.head()
year
coverages['total_visits_2015'] = coverages.loc[:,2011]+coverages.loc[:,2012]+coverages.loc[:,2013]+coverages.loc[:,2014]+coverages.loc[:,2015]
coverages['total_visits_2016'] = coverages.loc[:,2011]+coverages.loc[:,2012]+coverages.loc[:,2013]+coverages.loc[:,2014]+coverages.loc[:,2015] +coverages.loc[:,2016]
coverages['total_visits_2017'] = coverages.loc[:,2011]+coverages.loc[:,2012]+coverages.loc[:,2013]+coverages.loc[:,2014]+coverages.loc[:,2015] +coverages.loc[:,2016]+coverages.loc[:,2017]
coverages['total_visits_2018'] = coverages.loc[:,2011]+coverages.loc[:,2012]+coverages.loc[:,2013]+coverages.loc[:,2014]+coverages.loc[:,2015] +coverages.loc[:,2016]+coverages.loc[:,2017]+coverages.loc[:,2018]
coverages['total_visits_2019'] = coverages.loc[:,2011]+coverages.loc[:,2012]+coverages.loc[:,2013]+coverages.loc[:,2014]+coverages.loc[:,2015] +coverages.loc[:,2016]+coverages.loc[:,2017]+coverages.loc[:,2018]+coverages.loc[:,2019]




a = coverages.groupby('Customer Heading')['total_visits_2015','total_visits_2016','total_visits_2017','total_visits_2018','total_visits_2019'].sum()



a = coverages.groupby('Customer Heading')['total_visits'].sum()



a = a.reset_index()

a = a.to_frame()

b = coverages.groupby('Customer Heading')['Current id_Representative'].count()

b = b.to_frame()

c = pd.merge(a, b, on='Customer Heading')

c.to_csv('coverage_finall_prepared.csv')



coverages['Customer Heading'].nunique()
len(coverages)

b[b['Current id_Representative'] == 7]
a.describe()

coverages.columns

coverages[coverages['Customer Heading'] == 126544].to_excel('max.xlsx')



activities = pd.read_excel('/Users/utkarsh/Desktop/Datathon_2/Data sets/Activities.xlsx')

activities.columns
activities['year'] = activities['Date'].dt.year
activities_type = pd.get_dummies( activities, columns= ['Type activity'] )


activities_type = activities_type.groupby(['Customer heading', 'year'])['Type activity_Administration',
                                         'Type activity_Collect Information', 'Type activity_Commercial',
                                         'Type activity_Customer training', 'Type activity_Implementation',
                                         'Type activity_In-house training', 'Type activity_Internal',
                                         'Type activity_Others', 'Type activity_Presentation',
                                         'Type activity_Prospecting', 'Type activity_Support'].sum()

activities_cylce_sum = activities.groupby(['Customer heading', 'year'])['count_cicle'].sum()

activities_cycle_dummy =  pd.read_csv('Activities2.csv')
activities_cycle_dummy['Date'] =pd.to_datetime(activities_cycle_dummy['Date'])

activities_cycle_dummy['year'] = activities_cycle_dummy['Date'].dt.year
activities_cycle_dummy.columns


activities_cycle_dummy = activities_cycle_dummy.groupby(['Customer heading', 'year'])['ADMINISTRATION', 'BIOLOGY AND GEOLOGY',
                                                       'ECONOMY', 'ENGLISH (INFANT)', 'ENGLISH (PRIMARY)',
                                                       'ENGLISH (SECONDARY)', 'FRENCH (PRIMARY)', 'FRENCH (SECONDARY)',
                                                       'FRENCH HIGH SCHOOL', 'GEOGRAPHY AND HISTORY', 'INFANT',
                                                       'INFORMATION TECHNOLOGY', 'LATIN & GREEK', 'LIBRARY',
                                                       'MANAGEMENT BOARD', 'MATHEMATICS', 'MUSIC (PRIMARY)',
                                                       'MUSIC (SECONDARY)', 'ORIENTATION', 'OTHER', 'OWNERSHIP TEAM',
                                                       'PASTORAL TEAM', 'PHILOSOPHY', 'PHYSICS AND CHEMISTRY',
                                                       'PLASTIC COURSE', 'PRIMARY', 'QUALITY', 'REGIONAL LANGUAGE',
                                                       'RELIGION (INFANT)', 'RELIGION (PRIMARY)', 'RELIGION (SECONDARY)',
                                                       'SCIENCE', 'SPANISH LANGUAGE', 'TECHNOLOGY', 'UNALLOCATED','(blank)'].sum()


len(activities_type)
len(activities_cylce_sum)
len(activities_cycle_dummy)

activities_processed = pd.merge(activities_type, activities_cylce_sum, on=['Customer heading','year'])
activities_processed = pd.merge(activities_processed, activities_cycle_dummy, on=['Customer heading','year'])
len(activities_processed)

activities_processed.to_csv('activities_processed.csv')

activities_check  = pd.read_csv("/Users/utkarsh/Desktop/Datathon_2/activities_processed.csv")