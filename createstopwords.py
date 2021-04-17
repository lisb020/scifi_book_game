import nltk
import pandas as pd

nltk.download('stopwords')
stop_words = nltk.corpus.stopwords.words("english")
namesurl = 'names_data.csv'
names_df = pd.read_csv(namesurl)

list_of_names = names_df['name'].to_list()
name_list = []
for name in list_of_names:
    name_list.append(name.lower())

stop_words.extend(name_list)
number_words =["one","two","three","four","five","six","seven","eight","nine","ten"]
stop_words.extend(number_words)

with open('stopwordlist.txt', 'w') as filehandle:
    filehandle.writelines("%s\n" % word for word in stop_words)