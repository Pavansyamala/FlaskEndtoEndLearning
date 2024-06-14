from flask import Flask , render_template , url_for , redirect , flash
from forms import SignupForm , LoginForm
from database_connecton import Connection

app = Flask(__name__) 
app.config["SECRET_KEY"] = "9347649447"


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html' , title = 'Home')

@app.route('/signup' , methods = [ 'GET' , 'POST'])
def signup():
    form = SignupForm()
    db = Connection()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        flash(f"Signup successful dear {form.username.data}")
        
        db.cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)" , (username, email, password))
        db.conn.commit()
        db.cursor.close()
        db.conn.close()
        return redirect(url_for('home')) 
    return  render_template('signup.html' , title = 'Signup' , form = form)

@app.route('/login' , methods = ['GET' , 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data 
        db = Connection()
        db.cursor.execute("SELECT * FROM users WHERE email LIKE %s AND password LIKE %s" , (email , password))
        if len(db.cursor.fetchall()) != 0 :
            flash(' Login Succesfull! ')
            db.cursor.close()
            db.conn.close()
            return redirect(url_for('home'))
        else :
            flash(' Login Failed! ')
    return render_template('login.html' , title = 'Login' , form = form)


if __name__ == '__main__':
    app.run(host = '0.0.0.0' , port = 5000 , debug=True)