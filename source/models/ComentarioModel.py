class Comentario:
    def __init__(self, author, author_image, date, comment, language, rating):
        self._author = author
        self._author_image = author_image
        self._date = date
        self._comment = comment
        self._language = language
        self._rating = rating

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