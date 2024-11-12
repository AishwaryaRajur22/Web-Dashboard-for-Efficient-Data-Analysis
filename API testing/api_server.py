from flask import Flask, request #I modified this line


app = Flask(__name__)

books = {
    "Eragon": {
        "Author": "Paolini"
    },
    "Tavi": {
        "Author": "Butcher"
    }
}


@app.get("/books")
def get_books():
    return books

@app.get("/book/<string:name>")
def get_book(name):
    return books[name]

@app.put("/book/<string:name>")
def add_book(name):
    request_data = request.get_json()
    books[name] = request_data
    return books[name], 200

@app.delete("/book/<string:name>")
def delete_book(name):
    del books[name]
    return "Success", 200
        
app.run()