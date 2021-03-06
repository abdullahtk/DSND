import sys
from sqlalchemy import create_engine
import pandas as pd
import re
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
nltk.download('wordnet')
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from nltk.tokenize import word_tokenize
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV
import pickle


def load_data(database_filepath):
    """
    The function to load data from a database file 
  
    Parameters: 
        database_filepath: The database file that contains the messages to be analyzed.

    Returns:
        X: Dataframe that contains the messages (Featuers) 
        Y: Dataframe that contains the categories (Targets)
        Y.columns.values: List of categories names 

    """

    engine = create_engine('sqlite:///'+database_filepath)
    df = pd.read_sql('SELECT * FROM messageCategory', engine)
    X = df['message']
    Y = df.drop(['message', 'genre', 'id'], axis=1)
    return X, Y, Y.columns.values


def tokenize(text):
    """
    The function to tokenize, lemmatize and stem text string 
  
    Parameters: 
        text: The string that needs to be processed.

    Returns:
        clean_words: The tokenized, lemmatized and stemmed text

    """

    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9]", " ", text) 
    text = text.strip()
    words = word_tokenize(text) 
    words = [w for w in words if w not in stopwords.words("english")]
    clean_words = [WordNetLemmatizer().lemmatize(w) for w in words]
    return clean_words


def build_model():
    """
    The function to build model based on GridSearchCV

    Returns:
        model: The GridSearchCV with the optimal parameters

    """

    pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer = tokenize)),
        ('tfidf', TfidfTransformer()),
        ('clf', MultiOutputClassifier(RandomForestClassifier()))
    ])
    parameters = {
    'tfidf__smooth_idf': [False],
    'tfidf__use_idf': [False],
    'clf__estimator__n_estimators':[20]
    }

    model = GridSearchCV(pipeline, param_grid=parameters, n_jobs=4, verbose=3)    
    return model


def evaluate_model(model, X_test, y_test, category_names):
    """
    The function to report the precision, recall and f1 score on test set 
  
    Parameters: 
        model: The model that already fitted and used for prediction.
        X_test: Test features
        y_test: Test target
        category_names: list of categories

    """

    y_prediction = model.predict(X_test)
    y_prediction_df = pd.DataFrame(y_prediction, columns=y_test.columns)
    for column in category_names:
        print(column)
        print(classification_report(y_test[column],y_prediction_df[column]))

def save_model(model, model_filepath):
    """
    The function to pack a model
  
    Parameters: 
        model: The model that needs to be packed
        model_filepath: The file name/path for the packed model

    """
    pickle.dump(model, open(model_filepath,'wb'))


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()