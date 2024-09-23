from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello AIDS Students</h1>"


@app.route('/home')
def home():
    return "<h1>Welcome to sistec bhopal</h1>"





if __name__  == "__main__":
    app.run(debug=True)