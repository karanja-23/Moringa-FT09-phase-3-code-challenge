from database import get_db_connection
class Author:
    def __init__(self, id, name):
        self._id = id
        self._name = name
    @property
    def id(self):
        return self._id
    @id.setter
    def id (self,id):
        if isinstance(id, int):
            self._id = id
    @property 
    def name(self):
        return self._name
    @name.setter
    def name (self, name):
        if hasattr(self,'_name'):
            raise AttributeError("Cannot reassign name after instancialization")
        if isinstance(name, str) and len(name) >0:
            self._name = name
    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT articles.title FROM articles INNER JOIN authors ON authors.id = articles.author_id WHERE authors.id = ?', (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return articles
   
    def magazines(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT magazines.name FROM magazines INNER JOIN authors ON authors.id = magazines.author_id WHERE authors.id = ?', (self.id,))
        magazines = cursor.fetchall()
        conn.close()
        return magazines
    def __repr__(self):
        return f'<Author {self.name}>'
