# Spam-Detector
This project is focused on building an efficient Email Spam Detector using Python and popular Machine Learning techniques. The objective is to train a model capable of classifying incoming emails as either Spam or Ham (Non-Spam), improving inbox management by filtering unwanted and potentially harmful emails.

The project follows a standard data science pipeline:

Data Loading:

A dataset containing labeled spam and ham emails is used as the foundation for training and evaluation.

Data Preprocessing:

Cleaning unnecessary characters, deduplication, handling missing values, and transforming the text into a usable format.

Feature Extraction:

Using TF-IDF (Term Frequency-Inverse Document Frequency) to convert the email text into numerical vectors suitable for machine learning models.

Model Training:

Applied algorithms like Multinomial Naive Bayes.

Fine-tuned using hyperparameter optimization techniques.

Evaluation:

Model performance is assessed with metrics such as Accuracy, Precision, Recall, F1-score, and Confusion Matrix.

Real-Time Prediction:

Deployed using Streamlit for real-time spam detection where users can input any email text and get immediate classification.

