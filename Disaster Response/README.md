# Disaster Response Pipeline Project

# Project Description

The purpose of the project is to analyze messages during emergency situations and build multiclass classification model. Each message has been assosiated with a category such as earthquake or food. 

## Libraries
The following Libraries were used in this project:
* numpy
* pandas
* matplotlib
* sklearn
* sqlalchemy
* nltk
* flask
* plotly

## Folders and Files
There are three folders:
- data: contains four files:
    * disaster_messages.csv: The messages that needs to be analyzed
    * disaster_categories.csv: The categories for the messages
    * process_data.py: ETL pipeline that must be run first to load and clean the data then create a database file for the data to be used in machine learning pipeline
    * DisasterResponse.db: The database that will be used in the machine learning pipeline

- models: contains one file:
    * train_classifier.py: ML pipeline that read data from database file, tokenize text, build fit, and evaluate model, and finally pack the model

- app: contains one file and one folder:
    * run.py: Flask web application
    * templates: contains two HTML files for the web application


## Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/


## License
The datasets used in this analysis were acquired from Figure Eight. The template code were given by Udacity.