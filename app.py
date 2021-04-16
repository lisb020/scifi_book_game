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
import numpy as np

winner = ""

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

def remove_nums(row):
  output = ''.join(c for c in str(row) if not c.isdigit())
  return(output)

def remove_multi_spaces(row):
  single_spaces = " ".join(str(row).split())
  return(single_spaces)

def remove_unicode(row):
  string_encode = str(row).encode("ascii", "ignore")
  return(string_encode.decode())


#create route that renders index.html template
@app.route("/", methods=["GET", "POST"])
def home():
    global winner
    return render_template("index.html", subgenre=winner)



# Send the user inputted data to the saved model
@app.route("/send", methods=["GET", "POST"])
def send():
    global winner
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
            print("successfully loaded tokenizer ", padded)

        # Load the model
        from tensorflow.keras.models import load_model
        subgenre_model = load_model("subgenre_trained.h5")
        print("successfully loaded file")
        
        pred = subgenre_model.predict(padded)
        labels = ['sf_aliens', 'sf_alternate_history', 'sf_alternate_universe','sf_apocalyptic', 'sf_cyberpunk', 'sf_dystopia', 'sf_hard','sf_military', 'sf_robots', 'sf_space_opera', 'sf_steampunk','sf_time_travel']
        winner = labels[np.argmax(pred)]
        print("prediction: " ,pred, labels[np.argmax(pred)])

        return redirect("/")

    return render_template("result.html", subgenre=winner)
    
    # return render_template("result.html", subgenre=pred)

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