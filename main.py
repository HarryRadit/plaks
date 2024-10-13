from flask import Flask, render_template
app = Flask(__name__)

title = "my ever book list"
books={
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
}
@app.route('/')
def hello_world():
   return render_template('block_list.html', title=title)

if __name__ == '__main__':
    app.run(debug=True)

