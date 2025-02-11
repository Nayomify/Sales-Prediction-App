import streamlit as st
import pickle
import numpy as np
import pandas as pd
import sklearn

# to read the model from the pickle file
model=pickle.load(open('model_lr.pkl','rb'))

# Streamlit UI
st.title('Sales Prediction App')
st.write('Enter advertising budgets to predict sales.')

# User input fields
TV=st.number_input('TV Advertising Budget ($)')
radio=st.number_input('Radio Advertising Budget ($)')
newspaper=st.number_input('Newspaper Advertising Budget ($)')


# Convert the user input to a dataframe
user_data=pd.DataFrame({'TV':TV,
'radio':radio,
'newspaper':newspaper}, index=[0])

# predict the house price
prediction=model.predict(user_data)

if st.button('Predict Sales'):
    st.write(f'Estimated is {prediction[0]}')
