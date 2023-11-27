from Connection import Connection
from models.ComentarioModel import Comentario

class ComentarioDatabase:
    def createTable():
        connection = Connection().openConnection()
        cursor = connection.cursor()
        cursor.execute(
             """
                CREATE TABLE IF NOT EXISTS Comentarios (
                    id serial PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    img VARCHAR(255) NOT NULL,
                    nota VARCHAR(255) NOT NULL,
                    avaliacoes VARCHAR(255) NOT NULL,
                    leguage VARCHAR(20) NOT NULL,
                    loja_id INTEGER,
                    FOREIGN KEY (loja_id) REFERENCES loja(id)
            );
            """
        )
        connection.commit()
        cursor.close()
        connection.close()
    def insertComentario(comentario: Comentario):
        connection = Connection().openConnection()
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO Comentarios (name, nota, avaliacoes, loja_id)
            VALUES (%s, %s, %s, %s);
            """,
            (comentario.name, comentario.nota, comentario.avaliacoes, comentario.loja_id)
        )
        connection.commit()
        cursor.close()
        connection.close()
    def getComentariosByLoja(loja_id: int):
        connection = Connection().openConnection()
        cursor = connection.cursor()
        cursor.execute(
            """
                SELECT * FROM Comentarios WHERE loja_id = %s;
            """,
            (loja_id,)
        )
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        if result is not None:
            comentarios = []
            for row in result:
                comentarios.append(Comentario(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[0]))
            return comentarios
        return None