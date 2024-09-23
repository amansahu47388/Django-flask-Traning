from flask import Flask,redirect,url_for,render_template,request


app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template('index.html')




# @app.route("/result/<int:marks>")
# def result(marks):
#     result = " "
#     if marks> 50:
#         result="pass"
#     else:
#         result="fail"
#     return render_template( 'result.html', res=result)
@app.route("/result/<int:age>")
def result(age):
    result = " "
    if age>= 18:
        result="You are elegible for vote"
    else:
        result="You are not elegible for vote"
    return render_template( 'result.html', res=result)





# @app.route("/submit", methods= ['POST','GET'])
# def submit():
#     total_score=0
#     if request.method=='POST':
#         english= float(request.form['english'])
#         python= float(request.form['python'])
#         math= float(request.form['math'])
#         django= float(request.form['django'])
#         total_score=(english+math+python+django)/4

#     return redirect(url_for('result',marks=total_score))

@app.route("/submit", methods= ['POST','GET'])
def submit():
    if request.method=='POST':
        name= str(request.form['name'])
        age= int(request.form['age'])
    return redirect(url_for('result',age=age))





if __name__=="__main__":
    app.run(debug=True)

