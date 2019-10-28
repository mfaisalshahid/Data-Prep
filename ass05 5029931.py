import pandas as pd
import math
import numpy as np
# The entire assignment is done in the format stated in the assignment. You can check it by running this assignment.
df = pd.read_csv(
    "/Users/muhammadshahid/Desktop/DATAPREP/FinalRaw.csv",
    engine="c",
    low_memory=False
)
# name = pd.read_csv("/Users/muhammadshahid/Desktop/DATAPREP/FinalRaw.csv", nrows=1)
# print (name)

columns = [
    "CL_Limit",
    "PD_Limit",
    "MP_Limit",
    "CreditScoreNum",
    "InsuranceExperienceDaysNum",
    "PreCreditTierNum",
    "PriorSwitchesCount",
    "RateManualNum",
    "UWTierNum"
]

q1ans = df[columns].fillna(df[columns].median())
print('*****************************')
print (q1ans)

print('*****************************')
q2ans = df['PNIAge'].clip(16, 100)

print (q2ans)

# I could not find N_mod in the dataset for question 3

columns1 = [
    "RateManualNum",
    "PD_Limit",
    "FirmCode",
    "agege75_lt30_lt21_pointed",
    "PD_Limit",
    "MP_Limit",
    "maxvehvalue",
    "PIP_Limit",
    "nextpremch"
]
print ('RANK')
q3ans = df[columns1].rank()
print (q3ans)
print('*****************************')
print ('Before Transformation')
print (df[columns1].mean(), df[columns1].skew(), df[columns1].median())

print('*****************************')
print ('After Transformation')
print (q3ans[columns1].mean() , q3ans[columns1].skew(), q3ans[columns1].median())


columns2 = [
    "UWTierNum",
    "noncancelendmts",
    "incurred_loss"
]
print('*****************************')
print('LOG')
q4ans = df[columns2].apply(np.log)
print (q4ans)
print('*****************************')
print ('Before Transformation')
print (df[columns2].mean(), df[columns2].skew(), df[columns2].median())
print('*****************************')
print ('After Transformation')
print (q4ans[columns2].mean() , q4ans[columns2].skew(), q4ans[columns2].median())

print('*****************************')
print ("POWER")
power = [
    ('total_fee', 0.5),
    ('total_ann_prem', 0.3125),
    ('CL_Limit', 0.25),
    ('npchcat', 0.125),
    ('InsuranceExperienceDaysNum', 0.375),
    ('CP_Limit', 0.4325)
]
x = 0
for i in power:
	print (i[x])
	tformed = df[i[x]] ** i[x+1]
	print (tformed)
	print ('Before Transformation')
	print ('mean = ', df[i[x]].mean(), 'skew = ', df[i[x]].skew(), 'median = ', df[i[x]].median())
	print ('After Transformation')
	print ('mean = ', tformed.mean() ,'skew = ', tformed.skew(), 'median =' , tformed.median())
	print('*****************************')


