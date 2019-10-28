import pandas as pd
import math

## file reading commented for the examiner to check
## use own 'path' for the file Malware_train.csv

fileR = pd.read_csv(
    "/Users/muhammadshahid/Desktop/SASUniversityEdition/myfolders/Malware_train_s.csv",
    index_col="MachineIdentifier",
    engine="c",
    low_memory=False
)

prob = len(fileR[fileR.HasDetections == 1].index) / len(fileR.index)

if prob < 0.5:
    t_Hold = (10*(1-prob)) / prob
else:
    t_Hold = (10*prob) / (1-prob)

def s_logit(row, sm):
    var1 = row.churn_rate
    var0 = 1-var1
    p1 = prob
    p0 = 1-p1
    final = math.log(var1+(p1*sm)) - math.log(var0+(p0*sm))
    return final
    

def smoothing_func(fileR, target, threshold, variable):
    freq = fileR[[variable, target]]
    
    churn = freq.groupby(by=variable, as_index=False, sort=True).sum()
    count = freq.groupby(by=variable, as_index=False, sort=True).count() 

    combined = pd.merge(count, churn, how="left", on=variable) 
    combined.columns = [variable, 'freq', 'churn'] 
 
    combined.loc[combined['freq'] < t_Hold, variable] = 'Other' 
    combined = combined.groupby(by=variable, as_index=False, sort=True).sum() 

    combined['churn_rate'] = combined['churn'] / combined['freq']

    combined['Logit with sm=0'] = combined.apply(lambda row: s_logit(row=row, sm=0), axis=1)
    combined['Logit with sm=10'] = combined.apply(lambda row: s_logit(row=row, sm=10), axis=1)
    combined['Logit with sM=100'] = combined.apply(lambda row: s_logit(row=row, sm=100), axis=1)
    final = combined.sort_values('freq')
    
    return final

print(smoothing_func(fileR, 'HasDetections', t_Hold, 'AppVersion'))
print(smoothing_func(fileR, 'HasDetections', t_Hold, 'Census_ActivationChannel'))
print(smoothing_func(fileR, 'HasDetections', t_Hold, 'Census_ChassisTypeName'))
print(smoothing_func(fileR, 'HasDetections', t_Hold, 'Census_DeviceFamily'))
print(smoothing_func(fileR, 'HasDetections', t_Hold, 'Census_FirmwareManufacturerIdentifier'))