# -*- coding: utf-8 -*-
"""Python Project - Employee Attrition Brikena.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yOkccIHjW93biBc0Da9wn2j52toR6bV_

# Analyse Employee Attrition

## Task

Uncover the factors that lead to employee attrition.

1. Have a look at the variables, understand what they are.
2. Which variables are associated with attrition? For which groups of employees
does this association hold (`Department`, `JobLevel`, etc.)? Formulate several hypotheses.
3. Explore each hypothesis.
    - Make plots and/or compute statistics.
    - Write a short conclusion, refer to the justifications you found in the data.

##Employee attrition

Employee attrition is the departure of employees from the company for any reason(voluntary or involuntary), including resignation, termination, death or retirement.


> There are five types of employee attrition:

1. Attrition due to retirement (people who choose to retire)
2. Voluntary attrition (employees decide to quit the job)
3. Involuntary attrition (company initiates the employee exit)
4. Internal attrition (employees decide to move from one department to another within the company)
5. Demographic specific attrition (employees leave the company due to specific factors eg. women.)

Companies should minimize employee attrition as this factor is essential to improve business profitability.

## Dataset

_Source: https://www.kaggle.com/datasets/whenamancodes/hr-employee-attrition_

This is a fictional data set created by IBM data scientists. It contains data about employees in a company.

Encoding of some of the columns:

```
Education
1 'Below College'
2 'College'
3 'Bachelor'
4 'Master'
5 'Doctor'

EnvironmentSatisfaction
1 'Low'
2 'Medium'
3 'High'
4 'Very High'

JobInvolvement
1 'Low'
2 'Medium'
3 'High'
4 'Very High'

JobSatisfaction
1 'Low'
2 'Medium'
3 'High'
4 'Very High'

PerformanceRating
1 'Low'
2 'Good'
3 'Excellent'
4 'Outstanding'

RelationshipSatisfaction
1 'Low'
2 'Medium'
3 'High'
4 'Very High'

WorkLifeBalance
1 'Bad'
2 'Good'
3 'Better'
4 'Best'
```

## Analysis
"""

import pandas as pd
import seaborn as sns

# From https://drive.google.com/file/d/1TGVkYpXg9efkuh-N3UCaahBtCQhs65vy/view
df = pd.read_csv(
    "https://drive.google.com/uc?id=1TGVkYpXg9efkuh-N3UCaahBtCQhs65vy",
    true_values=["Yes"],
    false_values=["No"],
)
df

df.shape

df.info()

df.describe().T

df.isnull().values.any()

df.nunique()

df.drop(['EmployeeCount', 'EmployeeNumber', 'Over18', 'StandardHours'], axis="columns", inplace=True)
df.shape

"""####**Conslusion:** The data conntains 1470 rows and 35 coulmns. The type of data is numerical (26), bool (2) and categorical (7). There is no null value. With the unique value function I noticed that 'EmployeeCount', 'Over18', 'StandardHours' have only one unique value and 'EmployeeNumber' has 1470 unique values. These features aren't useful so I drop these columns and now my data shape is 1470, 31.

##Data visualization (General info)
"""

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(13,6))
plt.subplot(121)
df['Attrition'].value_counts().plot.pie(autopct = '%1.0f%%' , colors=['lightgreen','tomato'],startangle = 60, wedgeprops={"linewidth":2 , "edgecolor":"k"}, shadow=True)
plt.title("Distribution of Turnover")
plt.show()

sns.countplot(x='Gender', hue='Attrition', data=df, palette='prism_r')
plt.show()

sns.countplot(x='MaritalStatus', hue='Attrition', data=df, palette='prism_r')
plt.show()

plt.figure(figsize=(15,6))
sns.countplot(x='Age', hue='Attrition', data=df, palette='hot')
plt.show()

sns.countplot(x='BusinessTravel', hue='Attrition', data=df, palette='prism_r')
plt.show()

sns.countplot(x='Department', hue='Attrition', data=df, palette='prism_r')
plt.show()

plt.figure(figsize=(8,5))
sns.countplot(x='JobRole', hue='Attrition', data=df, palette='prism_r')
plt.xticks(rotation=90)
plt.show()

sns.countplot(x='OverTime', hue='Attrition', data=df, palette='prism_r')
plt.show()

plt.figure(figsize=(15,6))
sns.countplot(x='DistanceFromHome', hue='Attrition', data=df, palette='hot')
plt.show()

"""###Observations

1. Attrition rate: Attrition rate of the company is 16%
2. Gender: Male employees quit more than female employees
3. Marital Status: Employees who are single tend to quit their jobs more than the married or divorced.
4. Age: Young employees quit their jobs more than the older ones.
5. Business Travel: The employees who travel rarely are more likely to leave than other employees.
6. Department: Research and Development employees don't quit their jobs as much as the other departments.
7. Job Role: Sales Executives, Laboratory Technicians and Research Scientists are more likely to quit than other employees.
8. Over Time: Employees who do over time, quit more.
9. Employees who travel more than 10 kms to reach office, are more likely to quit.

##Correlation Matrix
"""

columns = list(df.columns)
categorical = [data for data in columns if df[data].dtype=='object']
categorical

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
for feat in categorical:
    df[feat] = le.fit_transform(df[feat].astype(str))
print (df.info())

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(18,9))
sns.heatmap(df.corr(method="kendall"), annot=True, fmt=".3f", ax=ax);

# Correlation Coeficient Range [-1 - 1]
#-1 is perfectly negative Correlation
#1 is perfect positive correlation

"""###**Conclusion:** In this section, I transformed all the data types in numerical by using LabelEncoder function and created a correlation matrix. As there are many features in the dataset it seems that the correlation matrix can give us just some insights that I should use for further analysis. In the first picture of this matrix table I can confirm that age, job involvement, job level, marital status, monthly income, overtime, stock option level, total working years, years at the company, years in current role and years with the current manager are the features that are more correlated with attrition than the rest.

##H1: Male employee are quiting the job more often that women
"""

#This code was working I'm not sure why it shows an error now. I am checking the documentation but nothing appears there.
fig, ax =plt.subplots(1,2)
sns.countplot(x='Gender', hue='Attrition', data=df[df['Gender']=='Male'], palette='prism_r', ax=ax[0]).set(title='Male')
sns.countplot(x='Gender', hue='Attrition', data=df[df['Gender']=='Female'], palette='prism_r', ax=ax[1]).set(title='Female')
fig.show()

fig, ax =plt.subplots(1,2)
sns.countplot(x='MaritalStatus', hue='Attrition', data=df[df['Gender']=='Male'], palette='prism_r', ax=ax[0]).set(title='Male')
sns.countplot(x='MaritalStatus', hue='Attrition', data=df[df['Gender']=='Female'], palette='prism_r', ax=ax[1]).set(title='Female')
fig.show()

fig, ax =plt.subplots(1,2)
sns.countplot(x='MaritalStatus', hue='Attrition', data=df[df['Gender']=='Male'], palette='prism_r', ax=ax[0]).set(title='Male')
sns.countplot(x='MaritalStatus', hue='Attrition', data=df[df['Gender']=='Female'], palette='prism_r', ax=ax[1]).set(title='Female')
fig.show()

fig, ax =plt.subplots(1,2)
sns.countplot(x='Education', hue='Attrition', data=df[df['Gender']=='Male'], palette='prism_r', ax=ax[0]).set(title='Male')
sns.countplot(x='Education', hue='Attrition', data=df[df['Gender']=='Female'], palette='prism_r', ax=ax[1]).set(title='Female')
fig.show()

"""###**Conclusion:** The data do not support the hypothesis, the attrition rate between females and males is almost the same. However there is a similarity behave between males an females based on marital status and education. The employees that are single and educatated level 3 are more likely to quit the job.

## H2: Employees that are satisfied with the job they are doing are staying longer in the company
"""

sns.countplot(x='JobLevel', hue='Attrition', data=df, palette='prism_r')
plt.show()

sns.countplot(x='YearsInCurrentRole', hue='Attrition', data=df, palette='prism_r')
plt.show()

sns.countplot(x='JobSatisfaction', hue='Attrition', data=df, palette='prism_r')
plt.show()

sns.countplot(x='EnvironmentSatisfaction', hue='Attrition', data=df, palette='prism_r')
plt.show()

sns.countplot(x='RelationshipSatisfaction', hue='Attrition', data=df, palette='prism_r')
plt.show()

sns.countplot(x='WorkLifeBalance', hue='Attrition', data=df, palette='prism_r')
plt.show()

"""###**Conclusion:** Job Satisfaction, Environment Satisfaction and Relationship Satisfaction do not give any insight to understanding the employees' attrition, so the data do not support the hypothesis. However, employees with low Job Level and have a few years in the company are quiting the jobs. Work life balance results are difficult to interpret, I would like to go in further details

##H3: Employees with less income are more likely to quit the company than the others
"""

sns.countplot(x='PercentSalaryHike', hue='Attrition', data=df, palette='prism_r')
plt.show()

sns.countplot(x='StockOptionLevel', hue='Attrition', data=df, palette='prism_r')
plt.show()

sns.countplot(x='YearsSinceLastPromotion', hue='Attrition', data=df, palette='prism_r')
plt.show()

plt.figure(figsize=(15,6))
sns.countplot(x='TotalWorkingYears', hue='Attrition', data=df, palette='prism_r')
plt.show()

"""###**Conclusion:** The data suppoort the main hypothesis, employees with less monthly income, stock option level and are less promoted than the others are quiting the job. """