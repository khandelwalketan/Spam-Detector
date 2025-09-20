📧 Spam Detector
This project focuses on building an efficient Email Spam Detection System using Python and Machine Learning. The goal is to classify incoming emails as either Spam or Ham (Non-Spam), improving inbox management by filtering unwanted and potentially harmful emails.

## Live Demo
Check out the deployed Streamlit app here: [Live Demo](http://localhost:8501)


📝 Project Overview
The project follows a standard Data Science Workflow:

1️⃣ Data Loading
Utilized a dataset containing labeled examples of both spam and ham emails.

2️⃣ Data Preprocessing
Removed unnecessary characters.

Deduplicated records.

Handled missing values.

Transformed email text into a clean format.

3️⃣ Feature Extraction
Applied TF-IDF (Term Frequency-Inverse Document Frequency) to convert the email text into numerical vectors suitable for machine learning.

4️⃣ Model Training
Trained a Multinomial Naive Bayes model.

Performed hyperparameter tuning for optimization.

5️⃣ Evaluation
Evaluated using:

Accuracy

Precision

Recall

F1-Score

Confusion Matrix

6️⃣ Real-Time Prediction
Deployed the trained model using Streamlit.

Users can input any email message and instantly receive spam classification results.
