# MOVIE & TV SHOWS REVIEWS API

In this project I did during the Ironhack bootcamp I created an API that is linked to a Mongodb
collection and from which we can extract reviews from movies and tv shows, and get a picture of 
what is the general opinion of users (sentiment analysis) towards a certain title. 

Before explaining the endpoints available, I wanted to point out that in order to fill the collection with lots of 
reviews from different titles, I have used two a series of functions that can be found in the jupyter notebook. 

Inside the API users can find two types of endpoints that can be accessed depending on the interests of the 
individual. 

# @GET 
In this section there are two endpoints users can use to extract information from the database.

The first one is the [total_reviews](http://locaclhost:5000/total_reviews/<title>) endpoint, that allows the 
user to extract all the reviews of a certain title available in the database. 

Example: 

url = http://locaclhost:5000/total_reviews/<title>

title = "Salvar al soldado Ryan"

The second endpoint, [sentimen](http://localhost:5000/sentiment/<title>), allows the user to extract the sentiment
 analysis of the reviews available in the database. As obtaining the results from all the reviews would be pointless,
 the result is a list with the percentage of each polarity (positive, negative, neutral). 
 
 Example: 
 
 url = http://locaclhost:5000/sentiment/<title>
 
 title = "Vengadores: Infinity War"
 
 #POST 
 For administrators, the API counts with the [new_review](http://localhost:5000/new_review)  endpoint that allows the user to, with the permission of the administrator, update the reviews of a certain title, or add
 a new one to the database. The information we want to add should be given in a dictionary format, as shown in the example:
 
url = http://localhost:5000/new_review
 
lista = ["Increible película"] (The reason for this list is that I set database to store all reviews of one title in just one object as an array)
 
datos = {'title': "El señor de los anillos: La comunidad del anillo", 
        'reviews': lista}
        

# Improvements to be made

The way I extract the information from the websites is by scraping, and even though the result has been positive, if there are more than one page of reviews the process becomes inefficient. For this reason, it would be 
a better option to use another library like Selenium. 

In reference to eh field available in the collection, it could be a good idea to add other fields like rating or source, in order to enrich the database.

