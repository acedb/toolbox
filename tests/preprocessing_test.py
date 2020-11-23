# Import from preprocessing
from toolbox.preprocessing import NLPPreprocessor
import pytest

import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def test_punctuation_remover():
    # function that removes punctuation from a given text
    text = 'Did you %know this 359?'
    for punctuation in string.punctuation:
        text = text.replace(punctuation, '')
    assert text == 'Did you know this 359'

def test_num_remover():
    # removes numbers from a given text
    text = 'Did you know this 359'
    text = ''.join(char for char in text if not char.isdigit())
    assert text == 'Did you know this '

def test_to_lowercase():
    # function that makes all text lowercase
    text = 'Did you Know this'
    assert text.lower() == 'did you know this'

def test_stopword_remover():
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

def test_list_concat():
    # converts list of words back into string
    text_list = ['i', 'am', 'so', 'very', 'happy', 'today']
    text = ' '.join(text_list)
    assert text == 'i am so very happy today'
