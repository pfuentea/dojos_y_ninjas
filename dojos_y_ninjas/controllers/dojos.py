from dojos_y_ninjas import app
from flask import request,flash,render_template,redirect,session 
from dojos_y_ninjas.models.dojo import Dojo



@app.route('/dojos')
def index():
    dojos=Dojo.get_all() #listado de dojos 
    return render_template("dojos.html",dojos=dojos)