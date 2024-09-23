from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configration 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Databse model
class user(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    meg = db.Column(db.String(120), nullable=True)

with app.app_context():
    db.create_all()

# post data in database
@app.route("/contact",methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            email = request.form.get('email')
            phone = request.form.get('phone')
            message = request.form.get('message')
           
            # Adding data in database
            entry = user(name=name,email=email,phone_num=phone,meg=message)
            db.session.add(entry)
            db.session.commit()
            print("Data is successfully add")
        except Exception as e:
            print("faild in database", e)

    return render_template('contact.html')


# Get Data from database
@app.route('/contacts')
def contacts():
    all_contacts = user.query.all()
    return render_template('contacts.html',contacts= all_contacts ) 








if __name__=="__main__":
    app.run(debug=True)

