import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            id int NOT NULL, 
            name varchar(255) NOT NULL,
            fullname varchar(255),
            location varchar(255),
            phone varchar(15), 
            sell_products varchar(5000),
            PRIMARY KEY (id)
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, name: str):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, tabrik_ism) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(id, name) VALUES(?, ?)
        """
        self.execute(sql, parameters=(id, name), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update_user_location(self, location, id):
        sql = """
        UPDATE Users SET location=? WHERE id=?
        """
        return self.execute(sql, parameters=(location, id), commit=True)



    # def update_user_mintaqa(self, user_mintaqa, user_mintaqa_nomi, id):
    #     # SQL_EXAMPLE = "UPDATE Users SET tabrik_ism=mail@gmail.com WHERE id=12345"

    #     sql = f"""
    #     UPDATE Users SET user_mintaqa=?, user_mintaqa_nomi = ? WHERE id=?
    #     """
    #     return self.execute(sql, parameters=(user_mintaqa, user_mintaqa_nomi, id), commit=True)

    # def update_check_sub(self, check_sub, id):
    #     # SQL_EXAMPLE = "UPDATE Users SET tabrik_ism=mail@gmail.com WHERE id=12345"

    #     sql = f"""
    #     UPDATE Users SET check_sub=? WHERE id=?
    #     """
    #     return self.execute(sql, parameters=(check_sub, id), commit=True)

    # def update_user_tabrik_ism(self, tabrik_ism, id):
    #     # SQL_EXAMPLE = "UPDATE Users SET tabrik_ism=mail@gmail.com WHERE id=12345"

    #     sql = f"""
    #     UPDATE Users SET tabrik_ism=? WHERE id=?
    #     """
    #     return self.execute(sql, parameters=(tabrik_ism, id), commit=True)

    # def update_user_tabrik_tr(self, tabrik_tr, id):
    #     # SQL_EXAMPLE = "UPDATE Users SET tabrik_tr=mail@gmail.com WHERE id=12345"

    #     sql = f"""
    #     UPDATE Users SET tabrik_tr=? WHERE id=?
    #     """
    #     return self.execute(sql, parameters=(tabrik_tr, id), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)


def logger(statement):
    pass
#     print(f"""
# _____________________________________________________        
# Executing: 
# {statement}
# _____________________________________________________
# """)
