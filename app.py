import streamlit as st
import os
import joblib
from model.data_preprocessing import preprocess_input
from model.feature_extraction import extract_features
from model.load_models import load_model, make_prediction

# Set up the title of the web app
st.title('Diabetes Prediction App')

# Model selection
MODEL_DIR = 'saved_models/'
model_files = os.listdir(MODEL_DIR)
model_choices = [filename for filename in model_files if filename.endswith('.joblib')]
selected_model_name = st.selectbox('Select a model for prediction:', model_choices)

# User input for prediction
user_input = st.text_area("Enter the text data for diabetes prediction:", "")

# Preprocess and extract features when 'Predict' button is clicked
if st.button('Predict'):
    if user_input:
        # Preprocessing the input
        preprocessed_text = preprocess_input(user_input)
        
        # Extracting features
        features = extract_features([preprocessed_text])  # Adjust according to your feature extraction function

        # Loading the selected model and making a prediction
        model = load_model(os.path.join(MODEL_DIR, selected_model_name))
        prediction = make_prediction(model, features)
        
        # Displaying the prediction
        st.write(f'Prediction: {prediction["prediction"]}')
        if 'probability' in prediction:
            st.write(f'Probability: {prediction["probability"]:.2f}')
    else:
        st.write("Please enter text data for prediction.")
