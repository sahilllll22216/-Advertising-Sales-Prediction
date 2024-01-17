import streamlit as st
import joblib
import numpy as np 
import warnings
warnings.filterwarnings("ignore")

model=joblib.load("mymodel.joblib")

st.title("Sales prediction App")

tv=st.slider("TV advertising budget",max_value=500)
radio=st.slider("Radio advertising budget",max_value=500)
newspaper=st.slider("Newspaper advertising budget",max_value=500)

input_data=np.array([[tv,radio,newspaper]])

prediction=model.predict(input_data)

st.subheader(f"Predicted Sales : {prediction[0]:.2f}")

