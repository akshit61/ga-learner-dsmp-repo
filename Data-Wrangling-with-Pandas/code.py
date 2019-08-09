# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)

# code ends here


# --------------
# code starts here
banks = bank.drop('Loan_ID',axis =1)
#print(banks.isnull().sum())
bank_mode = banks.mode()
#print(bank_mode)
banks['Gender'][banks['Gender'].isnull()] = str(bank_mode['Gender'])
banks['Married'][banks['Married'].isnull()] = str(bank_mode['Married'])
banks['Dependents'][banks['Dependents'].isnull()] = str(bank_mode['Dependents'])
banks['Self_Employed'][banks['Self_Employed'].isnull()] = str(bank_mode['Self_Employed'])
banks['LoanAmount'][banks['LoanAmount'].isnull()] = float(bank_mode['LoanAmount'])
banks['Loan_Amount_Term'][banks['Loan_Amount_Term'].isnull()] = float(bank_mode['Loan_Amount_Term'])
banks['Credit_History'][banks['Credit_History'].isnull()] = float(bank_mode['Credit_History'])
banks.info()


#code ends here


# --------------
# Code starts here
avg_loan_amount = pd.pivot_table(banks,index = ['Gender','Married','Self_Employed'],values='LoanAmount')
print(avg_loan_amount)

# code ends here



# --------------
# code starts here
loan_approved_se = len(banks[(banks['Self_Employed'] == 'Yes')&(banks['Loan_Status'] == 'Y')])
print(loan_approved_se)


loan_approved_nse = len(banks[(banks['Self_Employed'] == 'No')&(banks['Loan_Status'] == 'Y')])
print(loan_approved_nse)

percentage_se = (loan_approved_se/614) * 100
percentage_nse = (loan_approved_nse/614)*100
print('percentage_se : '+ str(percentage_se))
print('percentage_nse : '+ str(percentage_nse))
# code ends here


# --------------
# code starts here
def monthsToYears(months):
    return months//12
loan_term = banks['Loan_Amount_Term'].apply(lambda x:monthsToYears(x))
#print(loan_term)
big_loan_term = len(loan_term[loan_term >= 25])
print(big_loan_term)
# code ends here


# --------------
# code starts here
loan_groupby = banks.groupby('Loan_Status')
loan_groupby = loan_groupby[['ApplicantIncome','Credit_History']]
mean_values = loan_groupby.mean()
print(mean_values)
# code ends here


