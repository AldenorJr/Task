from Connection import Connection
from models.LojaModel import Loja

class LojaDataBase:
    def createTable():
        connection = Connection().openConnection()
        cursor = connection.cursor()
        cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS loja (
                    id serial PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    nota VARCHAR(255) NOT NULL,
                    avaliacoes VARCHAR(255) NOT NULL
            );
            """
        )
        connection.commit()
        cursor.close()
        connection.close()
    def insertLoja(loja: Loja):
        connection = Connection().openConnection()
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO loja (name, nota, avaliacoes)
            VALUES (%s, %s, %s);
            """,
            (loja.name, loja.nota, loja.avaliacoes)
        )
        connection.commit()
        cursor.close()
        connection.close()
    def hasLoja(loja: Loja):
        connection = Connection().openConnection()
        cursor = connection.cursor()
        cursor.execute(
            """
                SELECT * FROM loja WHERE id = %s;
            """,
            (loja.id,)
        )
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        return result is not None
    # recuperar a loja pelo noem
    def getLojaByName(name: str):
        connection = Connection().openConnection()
        cursor = connection.cursor()
        cursor.execute(
            """
                SELECT * FROM loja WHERE name = %s;
            """,
            (name,)
        )
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        if result is not None:
            return Loja(result[1], result[2], result[3], result[0])
        return None