# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path

#Code starts here 
data = pd.read_csv(path)
#print(data) 

data['Gender'].replace('-','Agender',inplace=True)
#print(data)

gender_count = pd.value_counts(data['Gender'].values, sort=True)
print(gender_count)

gender_count.plot.barh()


# --------------
#Code starts here
alignment = data['Alignment'].value_counts()
print(alignment)

alignment.plot.pie(title='Character Alignment')


# --------------
#Code starts here

sc_df = data[['Strength','Combat']].copy()
#print(sc_df)

sc_covariance = sc_df.Strength.cov(sc_df.Combat)
#print(sc_covariance)

sc_strength = sc_df['Strength'].std()
#print(sc_strength)

sc_combat = sc_df['Combat'].std()
#print(sc_combat)

sc_pearson = sc_covariance/(sc_strength*sc_combat)


ic_df = data[['Intelligence','Combat']].copy()

ic_covariance = ic_df.Intelligence.cov(ic_df.Combat)

ic_intelligence = ic_df['Intelligence'].std()

ic_combat = ic_df['Combat'].std()

ic_pearson = ic_covariance/(ic_intelligence*ic_combat) 

print(sc_covariance)
print(ic_covariance)


# --------------
#Code starts here
total_high = data['Total'].quantile(q=0.99)
print(total_high)

super_best = data[data.Total>total_high]
print(super_best)

super_best_names = super_best['Name'].tolist()
print(super_best_names)


# --------------
#Code starts here
fig1, ax_1 = plt.subplots()
ax_1.set_title('Intelligence')
ax_1.boxplot(data['Intelligence'])

fig2, ax_2 = plt.subplots()
ax_2.set_title('Speed')
ax_2.boxplot(data['Speed'])

fig3, ax_3 = plt.subplots()
ax_3.set_title('Power')
ax_3.boxplot(data['Power'])



