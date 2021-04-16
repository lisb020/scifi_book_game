# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
# model = load_model('rating_model')

#create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")


# Send the user inputted data to the saved model
@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        #bring in user input
        data = request.get_json()
        print("hello",data)
        # Load the model
        # from tensorflow.keras.models import load_model
        # rating_model = load_model("rating_model.h5")
        # description = request.form['']
        # model_loss, model_accuracy = rating_model.evaluate(description)
        return redirect("/", data)

    return redirect("/", code=302)

@app.route("/data", methods=["GET", "POST"])
def data():
    if request.method == "POST":
        #return data
        data = xxx
        return redirect("data.html", jsonify(data))

    return render_template("data.html")

@app.route("/about")
def about():
    
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)