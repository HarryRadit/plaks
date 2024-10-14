from flask import Flask, render_template
app = Flask(__name__)

title = "my ever book list"
books=[
    {
        'id':1,
        'title': "Harry potter",
        'author': "rio",
        'year': 2001,
        'description': "some description about the book harry potter"
    },
    {
        'id': 2,
        'title': "doraemon",
        'author': "hayakawa",
        'year': 2011,
        'description': "nobita meet doraemon"
    },
    {
        'id': 3,
        'title': "naruto",
        'author': "Rafli",
        'year': 2011,
        'description': "sinobi meet naruto in village"
    }
]
@app.route('/')
def hello_world():
   return render_template('block_list.html', title=title, books=books)

@app.route('/book/<int:book_id>')
def book_detail(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return render_template('book.detail.html', title=book['title'], book=book)
    else:
        return 'Book not found', 404
if __name__ == '__main__':
    app.run(debug=True)

