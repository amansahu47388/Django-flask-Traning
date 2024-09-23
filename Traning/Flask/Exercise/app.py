from flask import Flask

app=Flask(__name__)

@app.route('/')
def sistec():
    return  "<marquee><h1 style=color:red>Sagar Group of Institutions  </h1></marquee>  <image src=https://www.sistec.ac.in/assets/upload/home-sliders/home-slider-380478892.jpg style=height:500px; weight:100%></image>"
            


@app.route('/home')
def home():
    return "<h1>Welcome to sistec bhopal</h1>"





if __name__  == "__main__":
    app.run(debug=True)