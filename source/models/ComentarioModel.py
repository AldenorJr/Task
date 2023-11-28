class Comentario:
    def __init__(self, author, author_image, rating, comment, language, loja_id, date, id):
        self.author = author
        self.author_image = author_image
        self.rating = rating
        self.comment = comment
        self.language = language
        self.loja_id = loja_id
        self.date = date
        self.id = id

    @property
    def id(self):
        return self._id

    @property
    def loja_id(self):
        return self._loja_id

    @property
    def author(self):
        return self._author

    @property
    def author_image(self):
        return self._author_image

    @property
    def date(self):
        return self._date

    @property
    def comment(self):
        return self._comment

    @property
    def language(self):
        return self._language

    @property
    def rating(self):
        return self._rating
    
    @id.setter
    def id(self, id):
        self._id = id

    @loja_id.setter
    def loja_id(self, loja_id):
        self._loja_id = loja_id

    @author.setter
    def author(self, author):
        self._author = author

    @author_image.setter
    def author_image(self, author_image):
        self._author_image = author_image

    @date.setter
    def date(self, date):
        self._date = date

    @comment.setter
    def comment(self, comment):
        self._comment = comment

    @language.setter
    def language(self, language):
        self._language = language

    @rating.setter
    def rating(self, rating):
        self._rating = rating