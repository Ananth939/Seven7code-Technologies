# -*- coding: utf-8 -*-
"""Titanic_Classification

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T9X_wTLHt7CCW6yNl658Pqtq-FhUDjFe
"""

import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

df = pd.read_csv("Titanic-Dataset.csv")
df.head()

df.info()

df.describe()

df.drop(["PassengerId","Name","Ticket","Fare","Cabin","Parch"], inplace=True, axis=1)

sns.heatmap(df.isnull())

df['Age'].unique()

int(df[df["Pclass"] == 1]["Age"].dropna().mean())

int(df[df["Pclass"] == 2]["Age"].dropna().mean())

int(df[df["Pclass"] == 3]["Age"].dropna().mean())

def set_age(row):
    Pclass = row[0]
    Age = row[1]

    if np.isnan(Age):
        if Pclass == 1:
            return 38
        elif Pclass == 2:
            return 29
        else:
            return 25
    else:
        return Age

df["Age"] = df[["Pclass", "Age"]].apply(set_age, axis=1)

sns.heatmap(df.isnull())

sns.countplot(df, x="Pclass", hue="Survived")

sns.countplot(df, x="Sex", hue="Survived")

age_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
age_labels = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100']

df['Age_Group'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels)

# Create countplot
sns.countplot(data=df, x="Age_Group", hue="Survived")

sns.countplot(df, x="SibSp", hue="Survived")

sns.countplot(df, x="Embarked", hue="Survived")

Pclass = pd.get_dummies(df["Pclass"], drop_first=True, dtype="int")
Sex = pd.get_dummies(df["Sex"], drop_first=True, dtype="int")
SibSp = pd.get_dummies(df["SibSp"], drop_first=True, dtype="int")
Embarked = pd.get_dummies(df["Embarked"], drop_first=True, dtype="int")
df.drop(["Pclass","Sex","SibSp","Embarked"], axis=1, inplace=True)
df = pd.concat([df, Pclass, Sex, SibSp, Embarked], axis=1)

df.columns = df.columns.astype(str)

df

Y = df["Survived"]
X = df.drop("Survived", axis=1)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=42)

model = LogisticRegression()

model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

sns.heatmap(confusion_matrix(Y_test, Y_pred), annot=True)

accuracy = accuracy_score(Y_test, Y_pred)
accuracy

#accuracy percentage
accuracy * 100

