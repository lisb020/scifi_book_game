from keras.preprocessing.text import Tokenizer as kerasTokenizer
from keras.preprocessing.sequence import pad_sequences

def remove_nums(row):
  output = ''.join(c for c in str(row) if not c.isdigit())
  return(output)

def remove_multi_spaces(row):
  single_spaces = " ".join(str(row).split())
  return(single_spaces)

def remove_unicode(row):
  string_encode = str(row).encode("ascii", "ignore")
  return(string_encode.decode())


data = "why are you not working? jlakdsjfoi90"
print("data ",data)
data = data.lower()
data = remove_nums(data)
data = remove_multi_spaces(data)
data = remove_unicode(data)
data = [data]
print("clean ", data)

tokenizer = kerasTokenizer()
tokenizer.fit_on_texts(data)
seq = tokenizer.texts_to_sequences(data)
padded = pad_sequences(seq, maxlen=250)
print("working!: ", padded)