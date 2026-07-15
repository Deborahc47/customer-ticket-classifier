# Customer Support Ticket Classifier
A machine learning application built with Python that automatically classifies customer support messages into different categories.

## Project Overview

This project uses Natrual Language Processing (NLP) and machine learning to analyse customer messages and predict the most appropriate ticket category.
The application can classify messages into categories such as:

- Billing
- Account Access
- Technical Issue
- Cancellation
- General Enquiry

## How it works

   1. Customer support messages are stored in a CSV dataset.
   2. TF-IDF vectorisation converts the text into numerical features that the machine learning model can understand.
   3. A Logestic Regression model is trained using the labelled customer support messages.
   4. The trained model predicts the categoryof new customer messages.
   5. The application displayes the predicted category and confidence score.

## Machine Learning Model

The project uses:

- **TF-IDF Vectorizer** for converting text into numerical features and giving importance to useful words.
- **Logrstic Regression** for classifying customer messages into predefined categories.
- **Scikit-learn** for training and evaluating the machine learning model.
- **Joblib** for saving and loading the trained model and vectoriser.

  ## Project Structure

  ## How to Run the Project
  Install the required packages:
  pip install -r requirements.txt
  Train the machine learning model:
  python train_model.py
  Run the application:
  python app.py

  ##Example
  Example customer message:
  "The discount was not applied to my bill"
  The machine learning model analyses the message and predicts the most appropriate customer support category as seen below:
  <img width="484" height="388" alt="image" src="https://github.com/user-attachments/assets/421a3d64-b333-4943-9a45-c04a995a2a72" />


  ##Technologies Used
  - Python
  - Scikit-learn
  - Pandas
  - TF-IDF
  - Logistic Regression
  - Joblib
  - Tkinter

  ## Future Imporvements

  Possible future improvements include:

  - Increasing the size of the training dataset
  - Improving classification accuaracy.
  - Usinf more advanced NLP models.
  - Deploying the application as a web application or API
 
    ## Author
    Deborah
  
