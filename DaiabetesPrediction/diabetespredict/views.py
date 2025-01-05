from django.shortcuts import render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Create your views here.
def home(request):
    return render(request, "diabetespredict/home.html")

def predict(request):
    return render(request, "diabetespredict/predict.html")

def result(request):
    # Make sure to update this path to the correct CSV file location
    data = pd.read_csv(r"C:\Users\Manik\Downloads\archive_2\diabetes.csv")  # Use the correct path

    x = data.drop("Outcome", axis=1)
    y = data["Outcome"]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    model = LogisticRegression()
    model.fit(x_train, y_train)

    result1 = "No Prediction"  # Default result if POST method isn't used

    if request.method == "POST":
        val1 = float(request.POST["pregnancies"])
        val2 = float(request.POST["glucose"])
        val3 = float(request.POST["blood_pressure"])
        val4 = float(request.POST["skin_thickness"])
        val5 = float(request.POST["insulin"])
        val6 = float(request.POST["bmi"])
        val7 = float(request.POST["dpf"])
        val8 = float(request.POST["age"])

        pred = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])

        # Debugging step to check if the result is being set correctly
        print(f"Prediction: {pred}")  # Check prediction value in the console
        
        result1 = "Positive" if pred == [1] else "Negative"

    return render(request, "diabetespredict/predict.html", {"result2": result1})
