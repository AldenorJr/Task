from database.Connection import Connection
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
                    date VARCHAR(255) NOT NULL,
                    rating VARCHAR(20) NOT NULL,
                    comment VARCHAR(3000) NOT NULL,
                    leguage VARCHAR(20) NOT NULL,
                    loja_id INTEGER,
                    FOREIGN KEY (loja_id) REFERENCES loja(id)
            );
            """
        )
        connection.commit()
        cursor.close()
    def insertComentario(comentario: Comentario):
        connection = Connection().openConnection()
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO Comentarios (name, img, rating, comment, leguage, date, loja_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
            """,
            (
                comentario.author, comentario.author_image, comentario.rating, comentario.comment,
             comentario.language, comentario.date, comentario.loja_id
            )
        )
        connection.commit()
        cursor.close()
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
        if result is not None:
            comentarios = []
            for row in result:
                comentarios.append(Comentario(row[1], row[2], row[4], row[5], row[6], row[7], row[3], row[0]))
            return comentarios
        return None