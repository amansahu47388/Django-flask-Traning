from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configration 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/Aman'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Databse model
class person(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    passward = db.column(db.string(20), nullable=False)
with app.app_context():
    db.create_all()



# # post data in database
# @app.route("/registration",methods=['GET','POST'])
# def contact():
#     if request.method == 'POST':
#         try:
#             name = request.form.get('name')
#             email = request.form.get('email')
#             passward = request.form.get('passward')
           
#             # Adding data in database
#             entry = user(name=name,email=email,passward=passward)
#             db.session.add(entry)
#             db.session.commit()
#             print("Data is successfully add")
#         except Exception as e:
#             print("faild in database", e)

#     return render_template('registration.html')









if __name__=="__main__":
    app.run(debug=True)

