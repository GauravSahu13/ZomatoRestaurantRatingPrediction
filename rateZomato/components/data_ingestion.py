import os
import sys
from rateZomato.exception import zomatoRating
from rateZomato.logger import logging
import pandas as pd
import numpy as np
from rateZomato import utils
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pymongo import MongoClient

'''
from rateZomato.components.data_transformation import DataTransformation
from rateZomato.components.data_transformation import DataTransformationConfig

from rateZomato.components.model_trainer import ModelTrainerConfig
from rateZomato.components.model_trainer import ModelTrainer'''
@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        self.client = MongoClient('mongodb+srv://onShore:sahu9821@cluster0.a6ot5gp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')  # Connect to MongoDB
        self.db = self.client['RestaurantRating']  
        self.collection = self.db['Zomato']  
    
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            ''' local directory reading
            df=pd.read_csv('notebook\data\zomato_cleaned.xls')
            
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)'''

            logging.info(f"Exporting collection data as pandas dataframe")
            # Query all documents from MongoDB collection
            cursor = self.collection.find()

            # Convert cursor to DataFrame
            df = pd.DataFrame(list(cursor))

            # Optional: Drop the '_id' field if you don't need it
            df.drop('_id', axis=1, inplace=True)

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Data read from MongoDB successfully")

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                df

            )
        except Exception as e:
            raise zomatoRating(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data,_=obj.initiate_data_ingestion()
    if train_data is not None:
    # Do something with train_data
        pass
    if test_data is not None:
    # Do something with test_data
        pass

    '''data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))'''

