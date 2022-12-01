from dojos_y_ninjas import app
from flask import request,flash,render_template,redirect,session 
from dojos_y_ninjas.models.ninja import Ninja
from dojos_y_ninjas.models.dojo import Dojo

@app.route('/ninjas')
def get_ninjas():
    ninjas=Ninja.get_all()
    dojos=Dojo.get_all()
    return render_template("ninjas.html",ninjas=ninjas, dojos=dojos)

@app.route('/crear_ninja', methods=['POST'])
def new_ninja():
    data={
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'age': int(request.form['age']),
        'dojo_id': int(request.form['dojo_id']),
    }

    Ninja.create(data)
    return redirect('/ninjas')