import mysql.connector
import os
from dotenv import load_dotenv


class ConexionBaseDatos:
    def __init__(self):
        load_dotenv()

        self.connection = None
        self.host = os.getenv("DB_HOST", "localhost")
        self.database = os.getenv("DB_NAME", "db")
        self.user = os.getenv("DB_USER", "root")
        self.password = os.getenv("DB_PASSWORD", "")

    def conectar(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            return True
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")
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

            if query.strip().upper().startswith("SELECT"):
                resultado = cursor.fetchall()
                cursor.close()
                return resultado
            else:
                self.connection.commit()
                cursor.close()
                return True

        except Exception as e:
            print(f"Error al ejecutar consulta: {e}")
            return None

