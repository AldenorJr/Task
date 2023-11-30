import psycopg2

class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Connection(metaclass=SingletonMeta):
    _connection = None

    def openConnection(self):
        if self._connection is None:
            self._connection = psycopg2.connect(
                database='postgres',
                host='database-1.c2jh1togke7v.sa-east-1.rds.amazonaws.com',
                user='postgres',
                password='Casa132132',
                port='5432'
            )
        return self._connection