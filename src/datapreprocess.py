import pandas as pd
from sklearn.model_selection import train_test_split
 
def load_and_Split_data():
    data=pd.read_csv("../Data/raw/insurance.csv")
    X=data[['Age','Annual_Income_LPA','Policy_Term_Years','Sum_Assured_Lakhs']]
    y=data['Annual_Premium_Thousands']
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
    return X_train,X_test,y_train,y_test