from django.shortcuts import render
import pickle
from .models import Prediction

model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def home(request):

    prediction = ""
    probability = 0

    if request.method == "POST":

        message = request.POST.get("message", "").strip()

        if message:

            vector = vectorizer.transform([message])

            prediction = model.predict(vector)[0]

            probability = max(
                model.predict_proba(vector)[0]
            ) * 100

            Prediction.objects.create(
                message=message,
                result=prediction
            )

    history = Prediction.objects.all().order_by('-created_at')[:10]

    total_predictions = Prediction.objects.count()

    total_spam = Prediction.objects.filter(
        result='spam'
    ).count()

    total_ham = Prediction.objects.filter(
        result='ham'
    ).count()

    return render(
        request,
        "index.html",
        {
            "prediction": prediction,
            "probability": round(probability, 2),
            "history": history,
            "total_predictions": total_predictions,
            "total_spam": total_spam,
            "total_ham": total_ham
        }
    )

def about(request):
    return render(request, "about.html")