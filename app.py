import streamlit as st
import joblib
import pandas as pd

model = joblib.load("flower_model.pkl")

st.title("🌸 Flower Prediction App")
st.write("Enter flower mesurements to predict its type.")
sepal_length = st.number_input(
    "Sepal Length (cm)",0.0,10.0,5.0
)
sepal_width = st.number_input(
    "Sepal Width (cm)",0.0,10.0,3.0
)
petal_length = st.number_input(
    "Petal Length (cm)",0.0,10.0,1.5
)
petal_width = st.number_input(
    "Petal Width (cm)",0.0,10.0,0.2
)
if st.button("Predict Flower"):

    input_data = pd.DataFrame(
        [[sepal_length,sepal_width,
          petal_length,petal_width]],
        columns=[
            "sepal length (cm)",
            "sepal width (cm)",
            "petal length (cm)",
            "petal width (cm)",
        ]
    )
    prediction = model.predict(input_data)
    st.success("Predicted Flower:" + prediction[0])