import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

X_train=pd.read_csv("../Data/processed/X_train.csv")
y_train=pd.read_csv("../Data/processed/y_train.csv")
X_test=pd.read_csv("../Data/processed/X_test.csv")
y_test=pd.read_csv("../Data/processed/y_test.csv")

model=LinearRegression()
model.fit(X_train,y_train)

with open("../artifacts/model.pkl","wb") as f:
    pickle.dump(model,f)