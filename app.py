from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['Recipe-db']
collection = db['Recipe']

@app.route('/', methods=['GET'])
def index():
    query = request.args.get('query')
    if query:  # If there is a search query
        # Perform a case-insensitive search for recipes containing the query in their names
        recipes = list(collection.find({"RecipeName": {"$regex": query, "$options": "i"}}))
    else:
        # If no search query, fetch all recipes from the database
        recipes = list(collection.find())
    return render_template('index.html', recipes=recipes)

if __name__ == '__main__':
    app.run(debug=True)
