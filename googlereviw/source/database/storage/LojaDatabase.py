from database.Connection import Connection
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
    def saveLoja(loja: Loja):
        connection = Connection().openConnection()
        cursor = connection.cursor()
        cursor.execute(
            """
                UPDATE loja SET nota = %s, avaliacoes = %s WHERE id = %s;
            """,
            (loja.nota, loja.avaliacoes, loja.id)
        )
        connection.commit()
        cursor.close()
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
        return LojaDataBase.getLojaByName(loja.name)
    def hasLojaByName(name: str):
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
        return result is not None
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
        if result is not None:
            return Loja(result[1], result[2], result[3], result[0])
        return None