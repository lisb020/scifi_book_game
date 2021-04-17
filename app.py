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

stop_words = []

with open('stopwordlist.txt', 'r') as filehandle:
    stop_words = [word.rstrip() for word in filehandle.readlines()]

print(stop_words)

def filter_stop_words(row, stop_words):
    desc_list = [word for word in row.lower().split() if word not in stop_words] 
    return ' '.join(desc_list) 

#create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

# Send the user inputted data to the saved model
@app.route("/send", methods=["GET","POST"])
def send():
    global stop_words
    if request.method == "POST":
        #bring in user input
        data = request.get_json()
        # data = "hello"
        print("data ",data["description"])
        print("type",type(data))
        data = data["description"]
        data = data.lower()
        data = remove_nums(data)
        data = remove_multi_spaces(data)
        data = remove_unicode(data)
        data = filter_stop_words(data, stop_words)
        print("data", data)
        data = [data]
        
        # Load the tokenizer
        with open('tokenizer.pickle', 'rb') as handle:
            tokenizer = pickle.load(handle)
            seq = tokenizer.texts_to_sequences(data)
            padded = pad_sequences(seq, maxlen=250)
            print("successfully loaded tokenizer ")

        # Load the subgenre model
        from tensorflow.keras.models import load_model
        subgenre_model = load_model("subgenre_trained.h5")
        print("successfully loaded subgenre file")
        
        # Load the rating model
        rating_model = load_model("rating_trained.h5")

        # Predict subgenre
        pred_subgenre = subgenre_model.predict(padded)
        labels = ['aliens', 'alternate history', 'alternate universe','apocalyptic', 'cyberpunk', 'dystopia', 'hard','military', 'robots', 'space opera', 'steampunk','time travel']
        winner_subgenre = labels[np.argmax(pred_subgenre)]
        print("prediction subgenre: " ,pred_subgenre, winner_subgenre)

        # Predict rating
        pred_rating = rating_model.predict(padded)
        labels_rating = ['Great read', 'Average rating', 'Room for improvement']
        winner_rating = labels_rating[np.argmax(pred_rating)]
        print("prediction rating: " ,pred_rating, winner_rating)
        
        return {"body":[winner_subgenre, winner_rating]}
    
    return redirect("/")

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