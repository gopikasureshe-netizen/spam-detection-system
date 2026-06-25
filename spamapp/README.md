# Smart Spam Detection System
A Machine Learning-powered web application built using Django that classifies text messages as Spam or Ham (Not Spam).

The system provides real-time spam prediction, confidence scores, prediction history tracking, and an administrator dashboard for managing stored predictions.

📌 Features
* Message Classification
Detects whether a message is Spam or Ham.
Uses a trained Machine Learning model for prediction.
* Confidence Score
Displays prediction confidence percentage.
Helps users understand model certainty.
* Prediction History
Stores recent predictions in the database.
Displays the latest prediction results on the homepage.
* Admin Dashboard
Built using Django Admin.
View, add, update, and delete prediction records.
Manage application data securely.
* User-Friendly Interface
Clean and responsive design.
Character counter for messages.
Instant prediction results.
 
## Technologies Used

* Python
* Django
* Scikit-Learn
* HTML
* CSS
* SQLite3

## Project Structure

```
spamDetectionProject/
│
├── spamapp/
├── spamproject/
├── templates/
├── manage.py
├── train_model.py
├── spam_model.pkl
├── vectorizer.pkl
└── db.sqlite3


## Installation

```bash
git clone <repository-url>
cd spamDetectionProject

pip install django scikit-learn pandas numpy

python manage.py migrate
python manage.py runserver
```

## Usage

1. Enter a message.
2. Click Predict.
3. The system classifies the message as:

   * Spam
   * Ham (Not Spam)

## Future Enhancements

* User Authentication
* Email Spam Detection
* Real-Time API Integration
* Deep Learning Models

## Author

Gopika
