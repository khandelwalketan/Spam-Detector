import streamlit as st
import joblib  # <-- Use joblib instead of pickle

# Load trained model and vectorizer
model = joblib.load('spam_classifier_model.pkl')  # Correct way to load
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Streamlit UI
st.title("📧 Real-Time Spam Email Detector")

st.write("Paste your email message below:")

user_input = st.text_area("Email Message:")

if st.button("Predict"):
    if user_input:
        # Preprocess & vectorize
        input_data = vectorizer.transform([user_input])
        
        # Prediction
        prediction = model.predict(input_data)[0]
        
        if prediction == 1:
            st.success("✅ This email is **NOT Spam** (Ham)!")
        else:
            st.error("🚫 This email is **Spam**!")
    else:
        st.warning("Please enter a message.")
