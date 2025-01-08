# -*- coding: utf-8 -*-
import numpy as np
import pickle
import streamlit as st

# Load the saved model
loaded_model = pickle.load(open('best_model.sav', 'rb'))

# Create a function for prediction
def autism_prediction(input_data):
    """
    Predicts whether a person is autistic based on the given input data.

    Args:
        input_data: A list containing the following features:
            - Aq_Score: Score based on Autism Spectrum Quotient (AQ)
            - gender: Gender of the person
            - age: Age of the person
            - ethnicity: Ethnicity of the person
            - jaundice: Whether the patient had jaundice at the time of birth
            - autism: Whether an immediate family member has been diagnosed with autism
            - contry_of_res: Country of residence of the patient
            - used_app_before: Whether the patient has undergone a screening test before
            - result: Score for AQ1-10 screening test
            - relation: Relation of patient who completed the test

    Returns:
        A string indicating whether the person is autistic or not.
    """

    # Convert input data to NumPy array
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshape the array for single instance prediction
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 0:
        return 'The person is not autistic'
    else:
        return 'The person is autistic'

def main():
    """
    Creates the Streamlit web app for autism prediction.
    """

    st.title('Autism Prediction Web App')

    # Get input data from the user
    Aq_Score = st.text_input("Score based on Autism Spectrum Quotient (AQ)")
    gender = st.text_input('Gender')
    age = st.text_input('Age')
    ethnicity = st.text_input('Ethnicity')
    jaundice = st.text_input("Jaundice at birth (Yes/No)")
    autism_family = st.text_input("Autism in family (Yes/No)")
    country_of_res = st.text_input("Country of residence")
    used_app_before = st.text_input("Used app before (Yes/No)")
    result = st.text_input("AQ1-10 screening test score")
    relation = st.text_input("Relation to patient")

    diagnosis = ""

    # Create a button for prediction
    if st.button("Predict"):
        try:
            # Convert input data to appropriate format
            input_data = [
                float(Aq_Score),
                gender,
                int(age),
                ethnicity,
                jaundice,
                autism_family,
                country_of_res,
                used_app_before,
                float(result),
                relation
            ]
            diagnosis = autism_prediction(input_data)
        except ValueError:
            diagnosis = "Invalid input. Please enter valid values."

    st.success(diagnosis)

if __name__ == "__main__":
    main()