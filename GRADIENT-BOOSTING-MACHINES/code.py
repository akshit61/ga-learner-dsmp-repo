# --------------
import pandas as pd
from sklearn.model_selection import train_test_split
#path - Path of file 

# Code starts here
df = pd.read_csv(path)
X = df.drop(columns = ['customerID','Churn'])
y = df['Churn'].copy()
X_train,X_test,y_train,y_test = train_test_split(X,y,random_state = 0,test_size = 0.3)


# --------------
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Code starts here
pd.set_option('display.max_rows',None)
index = X_train[X_train['TotalCharges'].str.contains(' ') == True].index.tolist()
X_train.loc[index,'TotalCharges'] = np.nan
X_train['TotalCharges'] = X_train['TotalCharges'].astype(float)
mean = X_train['TotalCharges'].mean()
X_train['TotalCharges'].fillna(mean,inplace = True)
label = LabelEncoder()
cat = list(X_train.select_dtypes(include = 'object'))
for i in cat:
    X_train[i] = label.fit_transform(X_train[i])

index = X_test[X_test['TotalCharges'].str.contains(' ') == True].index.tolist()
X_test.loc[index,'TotalCharges'] = np.nan
X_test['TotalCharges'] = X_test['TotalCharges'].astype(float)
mean = X_test['TotalCharges'].mean()
X_test['TotalCharges'].fillna(mean,inplace = True)
label = LabelEncoder()
cat = list(X_test.select_dtypes(include = 'object'))
for i in cat:
    X_test[i] = label.fit_transform(X_test[i])
X_test.head()

y_train.replace({'No':0,'Yes':1},inplace = True)
y_test.replace({'No':0,'Yes':1},inplace = True)








# --------------
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

# Code starts here
ada_model =AdaBoostClassifier(random_state = 0)
ada_model.fit(X_train,y_train)
y_pred = ada_model.predict(X_test)
ada_score = accuracy_score(y_test,y_pred)
print('Accuracy score :',ada_score)
ada_cm = confusion_matrix(y_test,y_pred)
print('Confusion Matrix :\n',ada_cm)
ada_cr = classification_report(y_test,y_pred)
print('Classification Report :\n',ada_cr)



# --------------
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV

#Parameter list
parameters={'learning_rate':[0.1,0.15,0.2,0.25,0.3],
            'max_depth':range(1,3)}

# Code starts here
xgb_model = XGBClassifier(random_state=0)
xgb_model.fit(X_train,y_train)
y_pred = xgb_model.predict(X_test)
xgb_score = accuracy_score(y_test,y_pred)
print('accuracy score :',xgb_score)
xgb_cm = confusion_matrix(y_test,y_pred)
print('confusion matrix :\n',xgb_cm)
xgb_cr = classification_report(y_test,y_pred)
print('classification report :\n',xgb_cr)

clf_model = GridSearchCV(estimator = xgb_model,param_grid = parameters)
clf_model.fit(X_train,y_train)
y_pred = clf_model.predict(X_test)
clf_score = accuracy_score(y_test,y_pred)
print('accuracy score :',clf_score)
clf_cm = confusion_matrix(y_test,y_pred)
print('confusion matrix :\n',clf_cm)
clf_cr = classification_report(y_test,y_pred)
print('classification report :\n',clf_cr)


