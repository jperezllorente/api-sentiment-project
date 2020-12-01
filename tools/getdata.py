from configuration.config import collection
import tools.extraction as ext

def film_review(title):
    '''
    This function allows to select a title from the mongodb collection, and returns a list with the title we are
    interested in and the reviews of that title. Remember, it can be a movie or a tv show.

    It only takes as arguments the title we are interested in.
    '''

    query = {"title":f"{title}"}
    print(query)
    reviews = list(collection.find(query,{"_id":0}))
    return reviews


def sentiment(title):

    '''
    The beginning of this function is the same as the film_review function, as we are interested in obtaining information
    from the mongodb database. However, in this case we also exclude the title field.

    As each title will hopefully have more than 15 reviews, it would not be useful to get the sentiment analysis of all
    reviews. Instead, this function differentiates between polarities (negative, positive, neutral) and returns the
    percentage of each. This way we can get a quick look at how users value each title

        - lower than -0.35 -> negative polarity
        - gretaer than 0.35 -> positive polarity
        - betweem -0.35 and 0.35 -> neutral polarity

    '''


    query = {"title":f"{title}"}
    print(query)
    reviews = list(collection.find(query,{"_id":0, "title":0}))

    r = reviews[0]["reviews"]

    negative = 0

    positive = 0

    neutral = 0

    lista = [i for i in r]

    sentiment = [ext.sentimentAnalysis(i) for i in lista]

    for i in sentiment:

        if i < -0.35:

            negative += 1

        elif i > 0.35:

            positive += 1

        else:

            neutral += 1

    pos = round(positive / len(sentiment) * 100, 2)

    neg = round(negative / len(sentiment) * 100, 2)

    neu = round(neutral / len(sentiment) * 100, 2)

    result = [f'positive = {pos}%', f'negative = {neg}%', f'neutral = {neu}%']

    return result




