import numpy as np
import pickle
import streamlit as st

# Load the saved model
loaded_model = pickle.load(open('best_model.sav', 'rb'))

# Mapping for categorical inputs
ethnicity_mapping = {
    'White': 0,
    'Black': 1,
    'Asian': 2,
    'Hispanic': 3,
    'Other': 4
}

country_mapping = {
    'India': 0,
    'United States': 1,
    'United Kingdom': 2,
    'Canada': 3,
    'Australia': 4,
    'Other': 5
}

relation_mapping = {
    'Self': 0,
    'Parent': 1,
    'Sibling': 2,
    'Other': 3
}

# Prediction function
def autism_prediction(input_data):
    """
    Predicts whether a person is autistic based on the given input data.
    """
    input_data_as_numpy_array = np.asarray(input_data).reshape(1, -1)
    prediction = loaded_model.predict(input_data_as_numpy_array)
    return 'The person is autistic' if prediction[0] == 1 else 'The person is not autistic'

def main():
    """
    Streamlit app for autism prediction.
    """
    # Apply custom CSS styling
    st.markdown("""
        <style>
            .main {background-color: #000000;}
            .stTextInput > label {color: #ffffff; font-weight: bold;}
            .stSelectbox > label {color: #2b547e; font-weight: bold;}
            .stNumberInput > label {color: #2b547e; font-weight: bold;}
            .stButton > button {background-color: #2b547e; color: white; border-radius: 10px; padding: 10px;}
            .stButton > button:hover {background-color: #4b86b4;}
        </style>
    """, unsafe_allow_html=True)

    # Title with styling
    st.markdown('<h1 style="color:#2b547e; text-align:center;">Autism Prediction Web App</h1>', unsafe_allow_html=True)
    st.markdown('<h3 style="color:#2b547e; text-align:center;">Predict autism spectrum based on input data</h3>', unsafe_allow_html=True)

    # Collect inputs
    with st.container():
        st.markdown('<h4 style="color:#2b547e;">Enter the following details:</h4>', unsafe_allow_html=True)
        try:
            A1_Score = st.number_input("A1 Score (0 or 1)", min_value=0, max_value=1, step=1)
            A2_Score = st.number_input("A2 Score (0 or 1)", min_value=0, max_value=1, step=1)
            A3_Score = st.number_input("A3 Score (0 or 1)", min_value=0, max_value=1, step=1)
            A4_Score = st.number_input("A4 Score (0 or 1)", min_value=0, max_value=1, step=1)
            A5_Score = st.number_input("A5 Score (0 or 1)", min_value=0, max_value=1, step=1)
            A6_Score = st.number_input("A6 Score (0 or 1)", min_value=0, max_value=1, step=1)
            A7_Score = st.number_input("A7 Score (0 or 1)", min_value=0, max_value=1, step=1)
            A8_Score = st.number_input("A8 Score (0 or 1)", min_value=0, max_value=1, step=1)
            A9_Score = st.number_input("A9 Score (0 or 1)", min_value=0, max_value=1, step=1)
            A10_Score = st.number_input("A10 Score (0 or 1)", min_value=0, max_value=1, step=1)
            gender = st.selectbox('Gender', ['Male', 'Female'])
            age = st.number_input('Age', min_value=0)
            ethnicity = st.selectbox('Ethnicity', list(ethnicity_mapping.keys()))
            jaundice = st.selectbox('Jaundice at birth', ['Yes', 'No'])
            autism_family = st.selectbox('Autism in family', ['Yes', 'No'])
            country_of_res = st.selectbox('Country of Residence', list(country_mapping.keys()))
            used_app_before = st.selectbox('Used app before', ['Yes', 'No'])
            result = st.number_input('AQ1-10 Screening Test Score', min_value=0.0)
            relation = st.selectbox('Relation to patient', list(relation_mapping.keys()))

            # Convert categorical inputs to numerical
            gender = 1 if gender == 'Male' else 0
            jaundice = 1 if jaundice == 'Yes' else 0
            autism_family = 1 if autism_family == 'Yes' else 0
            used_app_before = 1 if used_app_before == 'Yes' else 0
            ethnicity = ethnicity_mapping.get(ethnicity, ethnicity_mapping['Other'])
            country_of_res = country_mapping.get(country_of_res, country_mapping['Other'])
            relation = relation_mapping.get(relation, relation_mapping['Other'])

            input_data = [
                A1_Score, A2_Score, A3_Score, A4_Score, A5_Score,
                A6_Score, A7_Score, A8_Score, A9_Score, A10_Score,
                gender, age, ethnicity, jaundice, autism_family,
                country_of_res, used_app_before, result, relation
            ]

            # Prediction button
            if st.button("Predict"):
                diagnosis = autism_prediction(input_data)
                st.markdown(f'<h3 style="color:#4b86b4;">{diagnosis}</h3>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
