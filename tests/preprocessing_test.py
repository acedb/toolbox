# Import from preprocessing
from toolbox.preprocessing import NLPPreprocessor
import pytest

import string

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
    text = 'Did you Know This'
    assert text.lower() == 'did you know this'

def test_list_concat():
    # converts list of words back into string
    text_list = ['i', 'am', 'so', 'very', 'happy', 'today']
    text = ' '.join(text_list)
    assert text == 'i am so very happy today'
