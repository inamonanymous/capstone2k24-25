from flask import Flask
from flask_restful import Api
from app.config import ApplicationConfig
from app.model import db
from app.ext import sess, cors
from app.resource.user import UserAuth, UserRegistration, UserData
from app.resource.super_admin import UserVerification 

def create_app():
    #create app instance
    app = Flask(__name__)
    app.config.from_object(ApplicationConfig)

    #objects initialization from app
    db.init_app(app)
    sess.init_app(app)
    api = Api(app)
    cors.init_app(app, resources={r"/api/*": {"origins": ["*"]}})

    #api resource routes
    api.add_resource(UserAuth, '/api/user/auth')
    api.add_resource(UserRegistration, '/api/user/registration')
    api.add_resource(UserData, '/api/user/data')
    api.add_resource(UserVerification, '/api/super_admin/verify')

    return app
    