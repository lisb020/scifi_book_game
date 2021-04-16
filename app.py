# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
from keras.preprocessing.text import Tokenizer as kerasTokenizer
from keras.preprocessing.sequence import pad_sequences
import pickle

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
# model = load_model('rating_model')

#create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

def remove_nums(row):
  output = ''.join(c for c in str(row) if not c.isdigit())
  return(output)

def remove_multi_spaces(row):
  single_spaces = " ".join(str(row).split())
  return(single_spaces)

def remove_unicode(row):
  string_encode = str(row).encode("ascii", "ignore")
  return(string_encode.decode())

# Send the user inputted data to the saved model
@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        #bring in user input
        data = request.get_json()
        print("data ",data)
        data = data.lower()
        data = remove_nums(data)
        data = remove_multi_spaces(data)
        data = remove_unicode(data)
        data = [data]
        
        with open('tokenizer.pickle', 'rb') as handle:
            tokenizer = pickle.load(handle)
            seq = tokenizer.texts_to_sequences(data)
            padded = pad_sequences(seq, maxlen=250)

        # Load the model
        from tensorflow.keras.models import load_model
        # subgenre_model = load_model("subgenre_trained.h5")
        # model_loss, model_accuracy = rating_model.evaluate(description)
        return redirect("/")

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