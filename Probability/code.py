# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)
fico700 = len(df[df['fico']>700])
#print(fico700)
p_a = fico700/len(df)
print(p_a)

purp = len(df[df['purpose']=='debt_consolidation'])
p_b = purp/len(df)
print(p_b)

#print(df['purpose'].value_counts())

df1 = df[df['purpose']=='debt_consolidation']

lendf1 = len(df1[df1['fico']>700])

prob = lendf1/len(df1)
#print(prob)


#(len(df[df['purpose']=='debt_consolidation' & df['fico']>700])/len(df))

p_a_b =  prob/p_a
print(p_a_b)

result = p_a_b==p_a
print(result)



# code ends here


# --------------
# code starts here
prob_lp = len(df[df['paid.back.loan']=='Yes'])/len(df)
print(prob_lp)

prob_cs = len(df[df['credit.policy']=='Yes'])/len(df)
print(prob_cs)

new_df = df[df['paid.back.loan']=='Yes']

new_df_credit = len(new_df[new_df['credit.policy']=='Yes'])

prob_pd_cs = new_df_credit/len(new_df)
print(prob_pd_cs)

bayes = (prob_pd_cs*prob_lp)/prob_cs
print(bayes)
# code ends here


# --------------
# code starts here
plt.bar(np.arange(len(df['purpose'])),df.purpose)

df1 = df[df['paid.back.loan']=='No']

plt.bar(np.arange(len(df1['purpose'])),df1.purpose)

# code ends here


# --------------
# code starts here

inst_median = df['installment'].median()
print(inst_median)

inst_mean = df['installment'].mean()
print(inst_mean)

plt.hist(df.installment,bins=10)
#df.info()
plt.hist(df['log.annual.inc'],bins=10)

# code ends here


