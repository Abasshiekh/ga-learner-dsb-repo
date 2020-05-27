# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



#Code starts here
#load the data set
data = pd.read_csv(path)

loan_status= data['Loan_Status'].value_counts()
# initialize the figure
plt.figure(figsize=[14,8])

# label the axes
plt.xlabel("loan_status")
plt.ylabel("Loans")

# title the plot
plt.title("Distribution of Loans status across loans")

# build and show the plot
plt.bar(loan_status.index,loan_status)


# --------------
#Code starts here

#Plotting an unstacked bar plot
property_and_loan=data.groupby(['Property_Area', 'Loan_Status'])
property_and_loan=property_and_loan.size().unstack()
property_and_loan.plot(kind='bar', stacked=False, figsize=(15,10))

#Changing the x-axis label
plt.xlabel('Property_Area')

#Changing the y-axis label
plt.ylabel('Loan_Status')

#Rotating the ticks of X-axis
plt.xticks(rotation=45)

#Code ends here


# --------------
#Code starts here





education_and_loan = data.groupby(['Education','Loan_Status']).size().unstack()
education_and_loan.plot(kind = 'bar',stacked = True, figsize=(10,15))

plt.xlabel('Education Status')
plt.ylabel('Loan Status')

plt.xticks(rotation = 45)


# --------------
#Code starts here
graduate= data[data['Education'] == 'Graduate']

not_graduate = data[data['Education'] == 'Not Graduate']

graduate['LoanAmount'].plot(kind = 'density',label = 'Graduate')

not_graduate['LoanAmount'].plot(kind = 'density',label = 'Not Graduate')













#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here


# initialize figure and axis
fig,(ax_1,ax_2,ax_3) = plt.subplots(1,3, figsize=(20,20))

#create scatter plot for ApplicantIncome and LoanAmount
ax_1.scatter(data['ApplicantIncome'],data["LoanAmount"])
ax_1.set_title('Applicant Income')

#create and plot scatter plot for CoapplicantIncome and LoanAmount
ax_2.scatter(data['CoapplicantIncome'],data["LoanAmount"])
ax_2.set_title('Coapplicant Income')
#create new column 'Total Income'
data['TotalIncome']= data['ApplicantIncome']+data['CoapplicantIncome']
#scater plot between TotalIncome and LoanAmount
ax_3.scatter(data["TotalIncome"],data["LoanAmount"])
ax_3.set_title('Total Income')



