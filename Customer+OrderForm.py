
import pandas as pd
from scipy import stats as stats
from scipy.stats import chi2_contingency
from scipy.stats import chi2

data = pd.read_csv("D:\\DS\\books\\ASSIGNMENTS\\Hypothesis testing\\Costomer+OrderForm.csv")
data
data.head()
data.dtypes

print(data['Phillippines'].value_counts(), 
      data['Indonesia'].value_counts(), 
      data['Malta'].value_counts(),
      data['India'].value_counts())

# Observed
obs = ([[271,267,269,280], [29,33,31,20]])

stat, p, dof, exp = chi2_contingency(obs)
print("STATS: ", stat)
print("P_value: ", p)
print("Degree of Freedom: ", dof)
print("Expected: ", exp)

alpha = 0.05

print('significance=%.3f, p=%.3f' % (alpha, p))
if p < alpha:
    print("Ho is Rejected and H1 is Accepted")
else:
    print("Ho is Accepted and H1 is Rejected")
    
# CONCLOSION
"""
Hence the significance is 0.050,
The variables are not Related,
They are Independent variables.
"""
 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    