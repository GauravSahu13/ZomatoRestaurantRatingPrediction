import pymongo
import pandas as pd
import json
from pymongo import MongoClient
from rateZomato.config import mongo_client


client = pymongo.MongoClient("mongodb+srv://onShore:sahu9821@cluster0.a6ot5gp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.test

DATABASE_NAME=  client["RestaurantRating"]
COLLECTION_NAME= DATABASE_NAME["Zomato"]

if __name__=="__main__":
    df = pd.read_csv(r"C:\Users\sahus\OneDrive\Desktop\Gaurav\ZomatoRestaurantRatingPrediction\zomato_cleaned.xls")
    print(f"Rows and columns: {df.shape}")

    #Convert dataframe to json so that we can dump these record in mongo db
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    #insert converted json record to mongo db
    COLLECTION_NAME.insert_many(json_record)

    print("Data dumped in MongoDB")