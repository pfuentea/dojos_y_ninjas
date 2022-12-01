from  dojos_y_ninjas.config.mysqlconnection import * 

class Ninja:
    db_name="dojos_and_ninjas2"

    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
    
    @classmethod # Dojo.get_all()
    def get_all(cls):
        solicitud = "SELECT * FROM ninjas ;"
        resultado = connectToMySQL(cls.db_name).query_db(solicitud)
        #validar si el resultado contiene algo
        todas_los_ninjas = []
        for user in resultado:
            todas_los_ninjas.append(cls(user))
        return todas_los_ninjas

    @classmethod  # User.create(data)
    def create(cls,data):
        solicitud = """INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at)
        VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(), NOW()); """
        return connectToMySQL(cls.db_name).query_db(solicitud,data)