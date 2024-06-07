import numpy as np
import pickle
import streamlit as st

#load saved models
loaded_model = pickle.load(open('C:\VS Code/VS code for DAA assigmnent/trained_model.sav', 'rb'))
  
# giving a title
st.title('Heart Disease Prediction Web Application')
# page title
st.title('Heart Disease Prediction using ML')

#getting input from user
col1, col2, col3 = st.columns(3)
with col1:
        age = st.text_input('Age')

with col2:
        sex = st.text_input('Sex')

with col3:
        cp = st.text_input('Chest Pain types')

with col1:
        trestbps = st.text_input('Resting Blood Pressure')

with col2:
        chol = st.text_input('Serum Cholesterol in mg/dl')

with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

with col1:
        restecg = st.text_input('Resting Electrocardiographic Results')

with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')

with col3:
        exang = st.text_input('Exercise Induced Angina')

with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

with col1:
        thal = st.text_input('Status of heart (thal): 0 = normal; 1 = fixed defect; 2 = reversable defect')
      
# code for Prediction
heart_diagnosis = ''
    
#button for Prediction
if st.button('Prediction Result'):
        user_input= ([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
        
user_input = [float(x) for x in user_input]
    
heart_prediction = loaded_model.predict([user_input])
print(heart_prediction)

if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having a heart disease'
else:
            heart_diagnosis = 'The person does not have any heart disease'
        
st.success(heart_diagnosis)
    

    






