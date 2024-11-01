from flask import Blueprint

auth = Blueprint("auth", __name__)

# @auth.route("/")
# def home():
#     return "<h1>Test</h1>"

@auth.route("/login")
def login():
    return "<p>login</p>"

@auth.route("/logout")
def logout():
    return "<p>logout</p>"

@auth.route("/sign_up")
def sign_up():
    return "<p>Sign up</p>"