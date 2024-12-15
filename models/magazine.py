from database.connection import get_db_connection
class Magazine:
    def __init__(self, id, name, category):
        self._id = id
        self.name = name
        self.category = category

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        if isinstance(id, int):
            self._id = id
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and (len(name) >= 2 and len(name) <= 16):
            self._name = name
    @property 
    def category(self):
        return self._category   
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
    
    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT articles.title FROM articles INNER JOIN magazines ON magazines.id = articles.magazine_id WHERE magazines.id = ?', (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return articles
     
    def contributors(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT authors.name FROM authors INNER JOIN magazines ON magazines.id = authors.magazine_id WHERE magazines.id = ?', (self.id,))
        contributors = cursor.fetchall()
        conn.close()
        return contributors
    def artticles_title(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT articles.title FROM articles INNER JOIN magazines ON magazines.id = articles.magazine_id WHERE magazines.id = ?', (self.id,))
        articles = cursor.fetchall()
        conn.close()
        if len(articles) == 0:
            return None
        return articles
    def contributing_authors(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT authors.name FROM authors INNER JOIN magazines ON magazines.id = authors.magazine_id WHERE magazines.id = ?', (self.id,))
        authors = cursor.fetchall()
        conn.close()
        if len(authors) == 0:
            return None
        return authors
    
    def __repr__(self):
        return f'<Magazine {self._name}>'
