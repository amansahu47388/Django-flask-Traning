from flask import Flask,redirect,url_for


app=Flask(__name__)

@app.route("/sucess/<int:score>")
def sucess(score):
    return "<h1>My 12th score is :</h1>"+str(score)+"<h1>pass </h1>"

@app.route("/fail/<int:score>")
def fail(score):
    return "<h1>My 12th score is :</h1>"+str(score)+"<h1>fail </h1>"


@app.route("/result/<int:marks>")
def result(marks):
    result = " "
    if marks < 50:
        result="sucess"
    else:
        result="fail"
    return redirect(url_for(result,score=marks))


if __name__  == "__main__":
    app.run(debug=True)