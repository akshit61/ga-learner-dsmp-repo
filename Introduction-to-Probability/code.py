# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)
p_a = len(df[df['fico']>700])/len(df)
df1 = df[df['purpose'] == 'debt_consolidation']
p_b = len(df1)/len(df)
p_a_b = len(df[(df['fico']>700) & (df['purpose'] == 'debt_consolidation')])/len(df)
#if (p_a_b == p_):
    #result = True
#else:
    #result = False
result = True if ((p_a_b*p_a)/p_b == p_a) else False
print(result)
# code ends here


# --------------
# code starts here
prob_lp = len(df[df["paid.back.loan"] == "Yes"])/len(df)
prob_cs = len(df[df["credit.policy"] == "Yes"])/len(df)
new_df = df[df["paid.back.loan"] == "Yes"]

#prob_pd_cs = len(df[(df["paid.back.loan"] == "Yes") & (df["credit.policy"] == "Yes")])/len(df)
prob_pd_cs = len(new_df[new_df['credit.policy'] == "Yes"])/len(new_df)
bayes = prob_pd_cs*prob_lp/prob_cs
print(bayes)
# code ends here


# --------------
# code starts here
df['purpose'].value_counts().plot(kind = 'bar')
plt.show()
df1 = df[df["paid.back.loan"] == "No"]
df1['purpose'].value_counts().plot(kind = 'bar')
plt.show()
# code ends here


# --------------
# code starts here

inst_median = df['installment'].median()
inst_mean = df['installment'].mean()
plt.hist(x = df['installment'],bins = 10)
plt.show()
plt.hist(x = df['log.annual.inc'],bins =10)
plt.show()
# code ends here


