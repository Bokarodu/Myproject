import streamlit as st
import pickle
import numpy as np


model = pickle.load(open('./model/model.pkl','rb'))

gender = [0,1]

st.title('Calorie Prediction App')

Gender = st.selectbox('Gender ( 0: female, 1: male)',gender)

col1,col2,col6 = st.columns(3)
with col1:
    Age = st.number_input('Age')
with col2:
    Height = st.number_input('Height')
with col6:
    Weight = st.number_input('Weight')

col3,col4,col5 = st.columns(3)

with col3:
    Duration = st.number_input('Exercise duration (in mins)')
with col4:
    Heart_Rate = st.number_input('Heart Rate')
with col5:
    Body_Temp = st.number_input('Body Temp (in Celsius)')

if st.button('Predict'):
    input_data = np.array([Gender,Age,Height,Weight,Duration,Heart_Rate,Body_Temp])
    input_df = input_data.reshape(1,-1)
    result = model.predict(input_df)
    st.header(f' You will burn {int(result[0])} Calories')


