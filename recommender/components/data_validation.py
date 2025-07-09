import os
import sys
import ast
import pandas as pd
import pickle
from recommender.logger.log import logging
from recommender.config.configuration import Configuration
from recommender.exception.exception_handler import AppException

class DataValidation:
    def __init__(self, app_config = Configuration()):
        try:
            self.data_validation_config = app_config.get_data_validation_config()
        except Exception as e:
            raise AppException(e, sys) from e
        
    def preprocess_data(self):
        try:
            ratings = pd.read_csv(self.data_validation_config.ratings_csv_file, sep=";", on_bad_lines="skip", encoding='latin-1')
            books = pd.read_csv(self.data_validation_config.books_csv_file, sep=";", on_bad_lines="skip", encoding='latin-1')
            
            logging.info(f" Shape of ratings data file: {ratings.shape}")
            logging.info(f" Shape of books data file: {books.shape}")

            books = books[['ISBN','Book-Title', 'Book-Author', 'Year-Of-Publication', 'Publisher','Image-URL-L']]
            books.rename(columns={"ISBN":"ISBN","Book-Title":'title','Book-Author':'author',"Year-Of-Publication":'year',"Publisher":"publisher","Image-URL-L":"image_url"},inplace=True)

            ratings.rename(columns={"User-ID":'user_id','Book-Rating':'rating'},inplace=True)

            x = ratings['user_id'].value_counts() > 150
            y = x[x].index
            ratings = ratings[ratings['user_id'].isin(y)]

            ratings_with_books = ratings.merge(books, on='ISBN')
            number_rating = ratings_with_books.groupby('title')['rating'].count().reset_index()
            number_rating.rename(columns={'rating':'num_of_rating'},inplace=True)
            final_rating = ratings_with_books.merge(number_rating, on='title')
            final_rating = final_rating[final_rating['num_of_rating'] >= 50]

            final_rating.drop_duplicates(['user_id','title'],inplace=True)
            logging.info(f"Shape of final clean dataset: {final_rating.shape}")
                        
            os.makedirs(self.data_validation_config.clean_data_dir, exist_ok=True)
            final_rating.to_csv(os.path.join(self.data_validation_config.clean_data_dir,'clean_data.csv'), index = False)
            logging.info(f"Saved data to {self.data_validation_config.clean_data_dir}")

            os.makedirs(self.data_validation_config.serialized_objects_dir, exist_ok=True)
            pickle.dump(final_rating,open(os.path.join(self.data_validation_config.serialized_objects_dir, "final_ratings.pkl"),'wb'))
            logging.info(f"Saved final_rating object to {self.data_validation_config.serialized_objects_dir}")

        except Exception as e:
            raise AppException(e, sys) from e
        
    def initiate_data_validation(self):
        try:
            logging.info(f"{'=' * 20} Data Validation {'=' * 20}")
            self.preprocess_data()
            logging.info(f"{'=' * 15} Data Validation Completed Successfully {'=' * 15} \n\n")
        except Exception as e:
            raise AppException(e, sys) from e