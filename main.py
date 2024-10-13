from flask import Flask
app = Flask(__name__)

myname = "Nig"
@app.route('/')
def hello_world():
    return 'Hello, ger! from ' + myname

if __name__ == '__main__':
    app.run(debug=True)

print("test")