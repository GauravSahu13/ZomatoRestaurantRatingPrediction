import sys
import pandas as pd
from ratZomato.exception import zomatoRating
from ratZomato.utils import load_object
import os

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
            print("Before Loading")
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise zomatoRating(e, sys)

class CustomData:
    def __init__(self, TakesOnlineOrders: int, hastablebooking: int, Rest_Type: int, Votes: int, Cuisines: int, Cost: int, Type: int, City: int): # type: ignore
        self.TakesOnlineOrders = TakesOnlineOrders
        self.hastablebooking = hastablebooking
        self.Rest_Type = Rest_Type
        self.Votes = Votes
        self.Cuisines = Cuisines
        self.Cost = Cost
        self.Type = Type
        self.City = City
    
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                "TakesOnlineOrders": [self.TakesOnlineOrders],
                "hastablebooking": [self.hastablebooking],
                "Rest_Type": [self.Rest_Type],
                "Votes": [self.Votes],
                "Cuisines": [self.Cuisines],
                "Cost": [self.Cost],
                "Type": [self.Type],
                "City": [self.City],
            }
            return pd.DataFrame(custom_data_input_dict)
        
        except Exception as e:
            raise zomatoRating(e, sys)
