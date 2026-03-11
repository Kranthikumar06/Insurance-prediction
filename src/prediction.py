import pickle
class Insurance_prediction:
    def __init__(self):
        with open("artifacts/model.pkl","rb") as f:
            self.model=pickle.load(f)
        with open("artifacts/standard_scaler.pkl","rb") as f:
            self.scaler=pickle.load(f)
    def prediction(self,Age,Annual_Income_LPA,Policy_Term_Years,Sum_Assured_Lakhs):
        input_data = self.scaler.transform([[Age,Annual_Income_LPA,Policy_Term_Years,Sum_Assured_Lakhs]])
        result=self.model.predict(input_data)
        return result[0]