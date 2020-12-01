from flask import Flask, request, render_template
import markdown.extensions.fenced_code
import json
import tools.getdata as get
import tools.postdata as pos


app = Flask(__name__)

@app.route("/")
def index():
    readme_file = open("index.md", "r")
    md_template_string = markdown.markdown(readme_file.read(), extensions=["fenced_code"])
    return md_template_string


@app.route("/reviews/<title>", methods=["GET"])
def total_reviews(title):
    critica = get.film_review(title)
    return json.dumps(critica)


@app.route("/sentiment/<title>", methods=["GET"])
def sentiment(title):
    feeling = get.sentiment(title)
    return json.dumps(feeling)


@app.route("/new_review", methods=["POST"])
def insert_review():
    title = request.form.get('title')
    review = request.form.get('reviews')

    pos.insert_review(title, review)

    return "Review successfully added"



app.run(debug=True)
