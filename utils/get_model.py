import os

MODEL_DIR = 'C:/Users/User/Documents/uni/FYP/DiabetesTypePredictionGitHub/Diabetes-Type-Prediction/saved_models/'

def get_model_choices():
    model_files = os.listdir(MODEL_DIR)
    model_choices = [(filename, 'Model ' + filename.split('.')[0]) for filename in model_files if filename.endswith('.joblib')]
    return model_choices
