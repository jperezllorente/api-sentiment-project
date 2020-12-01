import pandas as pd
from bs4 import BeautifulSoup
import requests
import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from textblob import TextBlob
import spacy
from spacy import displacy


def sentimentAnalysis(sentence):
    '''
    This function receives a sentence as argument, and returns a list with the compound sentiment analysis. This
    result will tell us if the sentence is either negatively, positively or neutraly polarized.

    This function on its own wont be useful to us, but it will be necessary for the next one.
    '''

    sia = SentimentIntensityAnalyzer()
    pol = sia.polarity_scores(sentence)
    polarity = pol["compound"]
    return polarity


def extract_critics_fa(url, title):
    '''
    This funciton allows us to create a dataframe of the reviews users have made of a certain movie or tv show with just putting
    the url of the site and the corresponding title

    No two websites are the same, so it is important to remember that this funciton will only work for the Filmaffinity site,
    and only if we enter in the "Show - more reviews", which can be found at the end of the first reviews available. Once inside
    the site, we copy the url and insert it in the function.

    It is also importan to point out that with this method we will only get a limited number of reviews. In order to get all of
    them we would have to use Selenium, which will allow us to interact with the clicks in the website
    '''

    response = requests.get(url)

    soup = BeautifulSoup(response.content)

    test = soup.find_all('a', title="ver fuente")

    nueva = []

    for i in test:
        nueva.append(i.text.strip())

    FA = [re.sub(r'\w*\ó\w\:\s\★*\½?\s\(\w*\s\w\)', '', i) for i in nueva]

    fa = pd.DataFrame(FA)

    fa['title'] = pd.Series([title for x in range(len(fa.index))])

    fa.columns = ["review", "title"]

    return fa


def extract_critics_imdb(url, title):

    '''
    This function is fulfills the same functions as the previous one, but with the
    link of the IMDB website. In this case, have to use as argument the url of the
    site of all reviews.
    '''

    response = requests.get(url)

    soup = BeautifulSoup(response.content)

    test = soup.find_all('a', class_="title")

    IMDB = []

    for i in test:
        IMDB.append(i.text.strip())

    imdb = pd.DataFrame(IMDB)

    imdb['title'] = pd.Series([title for x in range(len(imdb.index))])

    imdb.columns = ["review", "title"]

    return imdb


def insert_object(review, title):
    '''
    This function inserts all the information from the dataframe we created with the previous function as a Mongodb object.
    This object will have two field: title (name of the film or show) and reviews (array with all the reviews users have made)
    '''

    test = [i for i in review]

    datos = {'title': title,
             'reviews': test}

    films.insert_one(datos)

    return "Film reviews succesfully added"