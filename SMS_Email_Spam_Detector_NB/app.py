from flask import Flask, request, render_template
import joblib

model = joblib.load('spam_classifier_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  

@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    transformed_message = vectorizer.transform([message])
    prediction = model.predict(transformed_message)
    result = 'Spam' if prediction[0] == 1 else 'Not Spam'
    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)