# Import from preprocessing
from toolbox.preprocessing import NLPPreprocessor
import pytest

def test_punctuation_remover():
    # function that removes punctuation from a given text
    text = 'Did you %know this 359?'
    for punctuation in string.punctuation:
        text = text.replace(punctuation, '')
    assert text == 'Did you know this 359'

def num_remover():
    # removes numbers from a given text
    text = 'Did you know this 359'
    text = ''.join(char for char in text if not char.isdigit())
    assert text == 'Did you know this '

def to_lowercase():
    # function that makes all text lowercase
    text = 'Did you Know this'
    assert text.lower() == 'did you know this'

def stopword_remover():
    # removes stopwords from given text and returns text as list of words
    text = 'i am so very happy today'

    # english stopwords stored in variable stop_words
    stop_words = set(stopwords.words('english'))

    # splits text into list of words
    word_tokens = word_tokenize(text)

    # removes stopwords from text
    text_list = [word for word in word_tokens if not word in stop_words]

    # returns list of non-stopwords
    assert text_list == ['happy', 'today']

def list_concat():
    # converts list of words back into string
    text = ['i', 'am', 'so', 'very', 'happy', 'today']
    text = ' '.join(text_list)
    assert text = 'i am so very happy today'
