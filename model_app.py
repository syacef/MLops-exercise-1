import streamlit as st
import joblib

if __name__ == "__main__":
    model = joblib.load("regression.joblib")
    st.title("House Price Prediction")
    st.number_input("Number of Rooms", min_value=1, value=3, key="nb_rooms")
    st.number_input("Size", min_value=1, value=25, key="size")
    st.number_input("Has Garden", min_value=0, max_value=1, value=0, key="garden")
    if st.button("Predict Price"):
        features = [[st.session_state.size, st.session_state.nb_rooms, st.session_state.garden]]
        prediction = model.predict(features)
        st.write(f"Predicted House Price: ${prediction[0]:,.2f}")