from flask import Flask , render_template , url_for , redirect , flash
from forms import SignupForm , LoginForm
from database_connecton import connection

app = Flask(__name__) 
app.config["SECRET_KEY"] = "9347649447"


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html' , title = 'Home')

@app.route('/signup' , methods = [ 'GET' , 'POST'])
def signup():
    form = SignupForm()
    db = connection()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        flash(f"Signup successful dear {form.username.data}")
        document = {"username":username,"email":email,"password":password}
        db.coll.insert_one(document)
        return redirect(url_for('home')) 
    return  render_template('signup.html' , title = 'Signup' , form = form)

@app.route('/login' , methods = ['GET' , 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data 
        db = connection()
        record = db.coll.find({"$and":[{"email":email} , {"password" : password}]})
        count = 0 
        for i in record :
            count += 1 
        if count != 0 :
            flash('Login Successful')
            return redirect(url_for('home'))
        else :
            flash('Login Failed')
            return render_template('login.html' , title = 'Login' , form = form)
    return render_template('login.html' , title = 'Login' , form = form)


if __name__ == '__main__':
    app.run(host = '0.0.0.0' , port = 10000 , debug=True)