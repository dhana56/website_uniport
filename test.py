from app import app
from flask import current_app

# print(current_app.name)

#seeting up the application context
cont = app.app_context()
cont.push()
print(current_app.name)