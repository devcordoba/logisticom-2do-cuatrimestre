import mysql.connector

class ConexionBaseDatos:
    def __init__(self):
        self.connection = None
        self.host = "localhost"
        self.database = "logisticom_db"
        self.user = "root"
        self.password = ""
    
    def conectar(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            return True
        except:
            print("Error al conectar a la base de datos")
            return False
    
    def desconectar(self):
        if self.connection:
            self.connection.close()
    
    def ejecutar_consulta(self, query, parametros=None):
        try:
            cursor = self.connection.cursor()
            
            if parametros:
                cursor.execute(query, parametros)
            else:
                cursor.execute(query)
            
            if "SELECT" in query:
                resultado = cursor.fetchall()
                cursor.close()
                return resultado
            else:
                self.connection.commit()
                cursor.close()
                return True

        except:
            print("Error al ejecutar consulta")
            return None
