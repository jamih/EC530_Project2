from flask import Flask
from user.models import User
from app import app


@app.route('/user/signup', methods=['GET'])
def signup():
    return User().signup()
