# scifi_book_game
## Project Background
After months of stressful participation in the KU Data Analytics Bootcamp, we wanted to escape into a good scifi book. If we were ambitious enough, we might even write a scifi book.

Goal: Make predictions on scifi books based on the plot description from the Kaggle data set

We have developed a web page which uses machine learning to predict the success of a book and the subgenre based on the plot description.

## Group Members
- Jaime Jimenez: Machine Learning; CSS; HTML
- Mary Mays: Data aquisition, cleaning; Machine Learning; Jupyter notebook; 
- Lisa Stroh: Machine Learning; Flask; python; JavaScript; CSS; Deployment

## Product Design
- Pulled and transformed csv files in jupyter notebook
- Removed stopwords, further cleaned, and tokenized book descriptions
- Ran machine learning models in jupyter notebook
- Exported ML models to h5 files and exported tokenizer to pickle file
- Created flask app to run models based on user input 
- Used axios in javascript for click event of submit button and posted to flask app which then returned ML predictions
- Display was completed using html and javascript
- Graphs done with matplotlib
- Bootstrap and css for design
- Deployed to Heroku

### Machine Learning Models
- We created 2 sequential recurrent neural network (RNN) models with TensorFlow, Subgenre and Rating.
- The data is cleaned by removing double spaces, numbers, special characters, and names. 
- The data is tokenized using Keras. 
- The models are fed using the tokenized book descriptions, and the hot encoded subgenres. 
- The ratings were split into 3 categories and then hot encoded and fed into the model. The categories are: 
  - 4 - 5 rating is "Great Read" 
  - 3.75 - 4 rating is "Average Rating"
  - Less than 3.75 rating is "Room for improvement"
- The tokenizer is exported as a .pickle file
- The two models (subgenre and rating) are exported as .h5 files
- The machine learning models and tokenizer are used within the flask app when the "submit" button is pressed on the website

#### Subgenre RNN Model
- 30 epochs
- 4 layers
- Adamax Optimizer - used since we have natural language categorization
- Long Short-Term Memory (LSTM)
- Dropout Rate = 0.2 to help reduce overfitting

The subgenre model accuracy and loss graphs

![Subgenre Accuracy](/static/images/subgenre_model_acc.png)
![Subgenre Loss](/static/images/subgenre_model_loss.png)

#### Rating RNN Model
- 5 epochs
- 4 layers
- Adam Optimizer
- Long Short-Term Memory (LSTM) - Included activity_regularizer to help reduce overfitting
- Dropout Rate = 0.45 to help reduce overfitting

The rating model accuracy and loss graphs

![Rating Accuracy](/static/images/rating_model_acc.png)
![Rating Loss](/static/images/rating_model_loss.png)

## Deployment
This app is deployed to Heroku [here](https://scifybook.herokuapp.com/about)

## Presentation
This project was presented with this [presentation](https://github.com/lisb020/scifi_book_game/blob/main/scifi%20Books%20Presentation.pdf)
