# SMS Spam Detection

This project uses machine learning to classify SMS messages as spam or not spam. The model is built using **Multinomial Naive Bayes** and trained on a dataset of labeled SMS messages. The process involves feature extraction using **TF-IDF Vectorizer** to convert text into numerical data for model training.

## Project Structure
- `app.py`: Flask web application for user interface and prediction.
- `spam_classifier_model.pkl`: Trained model file.
- `tfidf_vectorizer.pkl`: TF-IDF vectorizer for text transformation.
- `templates/index.html`: HTML file for front-end interface.

## Installation

1. Clone the repository.
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask app:
   ```bash
   python app.py
   ```

## Features
- Input an SMS message and classify it as spam or not spam.
- Simple and interactive UI built using Flask.

## Demo

![Not Spam](/readme_images/not_spam_demo.png)
![Spam Image](/readme_images/spam_demo.png)