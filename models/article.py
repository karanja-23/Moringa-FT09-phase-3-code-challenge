from database.connection import get_db_connection
class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self._title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id
    @property
    def title (self):
        return self._title
    @title.setter
    def title (self, title):
        if hasattr(self, '_title'):
            raise AttributeError("Cannot reassign title after instancialization")
        if isinstance(title, str) and (len(title) >= 5 and len(title) <= 50):
            self._title = title
    

    def author (self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT authors.* FROM authors INNER JOIN articles ON authors.id = articles.author_id WHERE articles.id = ?', (self.id,))
        author_data = cursor.fetchone()
        return  author_data["name"]
    
    
    def magazine (self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT magazines.* FROM magazines INNER JOIN articles ON magazines.id = articles.magazine_id WHERE articles.id = ?', (self.id,))
        magazine_data = cursor.fetchone()
        return  magazine_data["name"]

    def __repr__(self):
        return f'<Article {self.title}>'

