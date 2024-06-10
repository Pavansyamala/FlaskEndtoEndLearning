from flask_wtf import FlaskForm  # type: ignore
from wtforms import StringField , SelectField , DateField , PasswordField , SubmitField , BooleanField
from wtforms.validators import DataRequired , Length  , Email , Optional , EqualTo 

class SignupForm( FlaskForm):
    username = StringField(
        "User Name" , 
        validators= [DataRequired() , Length(3 , 26)]
    )
    email = StringField(
        "Email Address" , 
        validators= [DataRequired() , Email()]
    )
    gender = SelectField(
        "Gender" , 
        choices= ['male','female' , 'Other'],
        validators= [Optional()]
    ) 
    DOB = DateField(
        "Date Of Birth" , 
        validators= [Optional()]
    )
    password = PasswordField(
        "Password" , 
        validators= [DataRequired() , Length(8 , 15)]
    ) 
    confirmPassword = PasswordField(
        "Confirming Password" , 
        validators= [DataRequired() , Length(8 , 15) , EqualTo("password")]
    )
    submit_button = SubmitField(
        "SignUp"
    )
class LoginForm( FlaskForm) :
    email = StringField(
        "Email Address" , 
        validators= [DataRequired() , Email()]
    ) 
    password = PasswordField(
        "Password" , 
        validators= [DataRequired() , Length(8 , 15)]
    )
    remember_me = BooleanField("Remember Me" , 
                               validators=[DataRequired() , ])
    submit_button = SubmitField(
        "Login"
    )