import datetime
from App.Config.conection import app, db
from flask import Flask
from flask_peewee.auth import Auth
from flask_peewee.admin import Admin
from App.Config.database import creatTable
from App.Routes import routes
from flask_peewee.rest import RestAPI

# create an Auth object for use with our flask app and database wrapper
auth = Auth(app, db)
admin = Admin(app, auth)
routes(admin)
admin.setup()
api = RestAPI(app)
routes(api)
api.setup()
if __name__ == '__main__':
    auth.User.create_table(fail_silently=True)
    creatTable()
    #admin = auth.User(username='admin', email='', admin=True, active=True)
    #admin.set_password('admin')
    #admin.save()
    app.run()