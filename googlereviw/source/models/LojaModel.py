class Loja:
    def __init__(self, name, nota, avaliacoes, id):
        self._id = id
        self._name = name
        self._nota = nota
        self._avaliacoes = avaliacoes

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def nota(self):
        return self._nota

    @property
    def avaliacoes(self):
        return self._avaliacoes

    @id.setter
    def id(self, id):
        self._id = id

    @name.setter
    def name(self, name):
        self._name = name

    @nota.setter
    def nota(self, nota):
        self._nota = nota

    @avaliacoes.setter
    def avaliacoes(self, avaliacoes):
        self._avaliacoes = avaliacoes