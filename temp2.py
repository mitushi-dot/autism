# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model=pickle.load(open('/Users/mitushisingh/Downloads/best_model.sav','rb'))

#creating a function for prediction

def autism_prediction(input_data):
    
    #changing input data to numpy array
    input_data_as_numpy_array=np.asarray(input_data)
    
    #reshape the array as we are predicting for one instance
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    
    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    if(prediction[0]==0):
        return 'the person is not autistic'
    else:
        return'the person is autistic'
        
        
        
def main():
    
    #giving title
    st.title=('Autism Prediction Web App')
    
    #getting the input data from the user
    
    Aq_Score - st.text_input("Score based on Autism Spectrum Quotient (AQ)")
    gender=st.text_input('what is your gender?')
    age=st.text_input('what is your age?')
    ethnicity=st.text_input('what is your ethnicity')
    jaundice -st.text_input(" Whether the patient had jaundice at the time of birth")
    autism - st.text_input("Whether an immediate family member has been diagnosed with autism")
    contry_of_res - st.text_input("Country of residence of the patient")
    used_app_before - st.text_input("Whether the patient has undergone a screening test before")
    result -st.text_input(" Score for AQ1-10 screening test")
    relation - st.text_input("Relation of patient who completed the test")
    
    #code for prediction

    diagnosis=""
    
    #creating a button for prediction
    
    if st.button("Autism Test Result"):
        diagnosis=autism_prediction([Aq_Score,gender,age,ethnicity,jaundice,autism,contry_of_res,used_app_before, result,relation])
        
    st.success(diagnosis)
    
    
    if __name__=="__main__":
        main()
    
    