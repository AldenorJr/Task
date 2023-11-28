import psycopg2

class Connection():
    connection = None
    def openConnection(self):
        if self.connection is None:
            self.connection = psycopg2.connect(
                database='postgres',
                host='database-1.c2jh1togke7v.sa-east-1.rds.amazonaws.com',
                user='postgres',
                password='Casa132132',
                port='5432'
            )
        return self.connection