# This program takes in text from a csv file, selects only the reviews from the summary column, then tokenizes, stems, and lemmatizes it.

import nltk
from nltk.stem.porter import PorterStemmer as PS
from nltk.stem.lancaster import LancasterStemmer as LS
from nltk.stem.snowball import SnowballStemmer as SS
from nltk.stem.wordnet import WordNetLemmatizer as WNL
import pandas as pd

"""
This function imports the csv and identifies the column titles. It takes the values from the summary column and turns it into a string
then it generates a word, casual, and sentence token from this string
"""

def get_tokens():
    col_list = ['reviewerID', 'asin', 'reviewerName',
            'helpful', 'reviewText', 'overall', 'summary', 
            'unixReviewTime', 'reviewTime']

    df = pd.read_csv('Musical_instruments_reviews.csv', usecols = col_list)

    stem = df['summary']
    word_list = 0

    for i in range(len(stem)):
        if word_list == 0:
            word_list = stem[i]
        else:
            word_list = word_list + ' ' + stem[i]

    wtokens = nltk.word_tokenize(word_list)
    ctokens = nltk.casual_tokenize(word_list)
    stokens = nltk.sent_tokenize(word_list)
    return wtokens, ctokens, stokens

# Takes word tokens and creates different stem versions of that list

def do_stemming(filtered):
    stemmed_PS = []
    stemmed_LS = []
    stemmed_SS = []
    for f in filtered:
        stemmed_PS.append(PS().stem(f))
        stemmed_LS.append(LS().stem(f))
        stemmed_SS.append(SS('english').stem(f))
    return stemmed_PS, stemmed_LS, stemmed_SS

# Takes word tokens and creates lemmas from it

def do_lemma(filtered):
    lemmize = []
    for f in filtered:
        lemmize.append(WNL().lemmatize(f, 'v'))
    return lemmize

# Implements code

if __name__ == '__main__':
    wtokens, ctokens, stokens = get_tokens()
    print('word tokens = ', wtokens)
    print('casual tokens = ', ctokens)
    print('sentence tokens = ', stokens)
    stemmed_PS, stemmed_LS, stemmed_SS = do_stemming(wtokens)
    lem_tokens = do_lemma(wtokens)
    result_stem_PS = dict(zip(wtokens,stemmed_PS))
    result_stem_LS = dict(zip(wtokens,stemmed_LS))
    result_stem_SS = dict(zip(wtokens,stemmed_SS))
    print('{tokens:stemmed} = ', result_stem_PS)
    print('{tokens:stemmed} = ', result_stem_LS)
    print('{tokens:stemmed} = ', result_stem_SS)
    result_lem = dict(zip(wtokens,lem_tokens))
    print('{tokens:lemmas} = ', result_lem)