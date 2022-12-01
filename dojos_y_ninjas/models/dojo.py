from  dojos_y_ninjas.config.mysqlconnection import * 

class Dojo:  
    db_name="dojos_and_ninjas2" 

    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']

    @classmethod # Dojo.get_all()
    def get_all(cls):
        solicitud = "SELECT * FROM dojos ;"
        resultado = connectToMySQL(cls.db_name).query_db(solicitud)
        #validar si el resultado contiene algo
        todas_los_dojos = []
        for user in resultado:
            todas_los_dojos.append(cls(user))
        return todas_los_dojos