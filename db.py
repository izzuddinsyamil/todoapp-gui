import sqlite3

class DB:
    def __init__(self):
        self.init_db()

    def init_db(self):

        conn = sqlite3.connect('todo_db')

        query = '''
        CREATE TABLE IF NOT EXISTS todos
        (id INTEGER PRIMARY KEY NOT NULL, name TEXT NOT NULL);
        '''

        conn.execute(query)
        conn.close()

    def insert_todo(self, todo):
        conn = sqlite3.connect('todo_db')
        query = '''
        INSERT INTO todos (name)
        VALUES ("{todo_name}")
        '''.format(todo_name=todo)

        conn.execute(query)
        conn.commit()
        conn.close()

    def list_todo(self):
        conn = sqlite3.connect('todo_db')
        query = '''
        SELECT name FROM todos;
        '''

        cursor = conn.execute(query)
        todos = []

        for row in cursor:
            todos.append(row[0])
        
        conn.close()
        return todos
    
    def delete_todo(self, todo):
        conn = sqlite3.connect('todo_db')
        query = '''
        DELETE FROM todos where name = "{todo_name}"
        '''.format(todo_name = todo)

        conn.execute(query)
        conn.commit()
        conn.close()
