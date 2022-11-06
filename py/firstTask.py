import pandas as pd

#'age,sex,bmi,children,smoker,region,charges'

def getData():
    data = pd.read_csv("insurance.csv", sep=',')

    return data

#print(getData())