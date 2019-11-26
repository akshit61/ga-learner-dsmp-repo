# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Code starts here
data = pd.read_csv(path)
#plt.figure(figsize = (10,8))
#plt.hist(data['Rating'].value_counts())
#plt.show()

data = data[data['Rating'] <= 5]
plt.figure(figsize = (10,8))
plt.hist(data['Rating'].value_counts())
plt.show()
data['Rating'].value_counts()
#Code ends here


# --------------
# code starts here
total_null = data.isnull().sum()
percent_null = (total_null/data.isnull().count())*100
missing_data = pd.concat([total_null,percent_null],axis = 1,keys = ['Total','Percent'])
print(missing_data.shape)

data.dropna(inplace = True)
total_null_1 = data.isnull().sum()
percent_null_1 = (total_null_1/data.isnull().count())*100
missing_data_1 = pd.concat([total_null_1,percent_null_1],axis = 1,keys = ['Total','Percent'])
print(missing_data_1.shape)
# code ends here


# --------------

#Code starts here
plt.figure(figsize = (10,8))
sns.catplot('Category','Rating',data = data,kind = 'box',height = 10)
plt.xticks(rotation = 90)
plt.title('Rating vs Category [BoxPlot]')
plt.show()
#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here
data['Installs'] = data['Installs'].str.rstrip('+')
data['Installs'] = data['Installs'].str.replace('\,','',regex = True)
data['Installs'] = data['Installs'].astype(int)
le = LabelEncoder()
data['Installs'] = le.fit_transform(data['Installs'])

plt.figure(figsize = (10,8))
sns.regplot('Installs','Rating',data = data)
plt.title('Rating vs Installs [RegPlot]')
plt.show()
#Code ends here



# --------------
#Code starts here

data['Price'] = data['Price'].str.lstrip('$')
data['Price'] = data['Price'].astype(float)
plt.figure(figsize = (10,8))
sns.regplot(x = 'Price',y ='Rating',data = data)
plt.title('Rating vs Price [RegPlot]')
plt.show()
#Code ends here


# --------------

#Code starts here

data['Genres'] = data['Genres'].str.replace('\;[\w\d\s\W]+','',regex = True)
#data['Genres'].unique()
gr_mean = data.groupby('Genres', as_index = False)[['Rating']].mean()
gr_mean.describe()
gr_mean = gr_mean.sort_values(by = 'Rating')
print('Min Rating : {0:s}  Max Rating : {1:s}'.format(str(gr_mean['Rating'].min()),str(gr_mean['Rating'].max())))
#Code ends here


# --------------

#Code starts here
data['Last Updated'] = pd.to_datetime(data['Last Updated'])
#data['Last Updated'].head()
max_date = data['Last Updated'].max()
data['Last Updated Days'] = max_date - data['Last Updated'] 
data['Last Updated Days'] = data['Last Updated Days'].dt.days
plt.figure(figsize = (10,8))
sns.regplot('Last Updated Days', 'Rating', data = data)
plt.title = 'Rating vs Last Updated [RegPlot]'
plt.show()
#Code ends here


