from recommender.components.data_ingestion import DataIngestion
from recommender.components.data_validation import DataValidation
from recommender.components.data_transformation import DataTransformation
from recommender.components.model_trainer import ModelTrainer
from recommender.config.configuration import Configuration

class TrainingPipeline:
    def __init__(self, app_config=Configuration()):
        self.data_ingestion = DataIngestion()
        self.data_validation = DataValidation()
        self.data_transformation = DataTransformation()
        self.model_trainer = ModelTrainer()

    def start_training_pipeline(self):
        try:
            self.data_ingestion.initiate_data_ingestion()
            self.data_validation.initiate_data_validation()
            self.data_transformation.initiate_data_transformation()
            self.model_trainer.initiate_model_trainer()
            print("Training pipeline completed successfully.")
        except Exception as e:
            print(f"An error occurred during the training pipeline: {e}")