from flask import Flask, render_template, request
from model import prediction

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        age = int(request.form["age"])
        spending_score = int(request.form["spending_score"])
        annual_income = float(request.form["annual_income"])
        
        # Use the prediction function
        cluster = prediction(age, annual_income, spending_score)
        
        # Display the result to the user
        return render_template("result.html", cluster=cluster)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
