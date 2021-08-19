'''This module is mainly for the Client class that works with the database "Games" '''

import time
from contextlib import contextmanager

import MySQLdb


class Client:
    '''Client to access and work with DB.

    The Client object connects database "Games". The access to DB meant to be set via _@contextmanager _access_db.
    '''
    def __init__(self):
        self.__host = "localhost"
        self.__user = "root"
        self.__password = "123"
        self.__db = "Games"

    def user_games(self, emails):
        """This method prints out games owned by user.

        If user with the email and password exists and have assigned games, they will be printed out.

        Args:
            email ([str]): unique user's email which will be checked in database.
        """
        select_q=f"""          
                SELECT users.name as Name, users.surname as Surname, users.email as Email,
                games.name as Game, games.price as price
                FROM users
                INNER JOIN users_games ON users.id=users_games.user_id
                INNER JOIN games ON users_games.game_id=games.id
                WHERE email='{emails}'
                """
        with self.__access_db() as cur:
            cur.execute(select_q)
            games = []
            for user_game in cur:
                games.append(user_game)
            return(games)

    def add_user(self, name, surname, email, password, add_ts):
        """This method adds the user to the database with the arguments

        Args:
            name ([str]): user's name
            surname ([str]): user's surname
            email ([str]): user's email which is set to be UNIQUE
            password ([str]): user's password
            add_ts ([int], optional): [description]. Defaults to current timestamp = int(time.time())
        """
        insert = "INSERT INTO users (name, surname, email, pass, time) VALUES(%s, %s, %s, %s, %s)"
        values = (name, surname, email, password, add_ts) 
        with self.__access_db() as cur:
            cur.execute(insert, values)

    def remove_users_before_date(self, ts):
        """This method removes users from the database if they were created before time module takes as parameter

        Args:
            ts ([int]): timestamp
        """
        with self.__access_db() as cur:
            cur.execute("DELETE FROM users WHERE time < %s""", (ts,))

    def remove_user(self, email):
        with self.__access_db() as cur:
            cur.execute("DELETE FROM users WHERE email=%s""", (email,))

    @contextmanager
    def __access_db(self):
        """It is context manager to access DB

        Yields:
            [cursor]: context manager yields the cursor to database
        """        
        try:
            db = MySQLdb.connect(self.__host, self.__user, self.__password, self.__db)
            mycursor = db.cursor()
            yield mycursor
        except Exception as error:
            print(error)
            raise
        else:
            db.commit()
        finally:
            db.close()


if __name__ == "__main__":
    a = Client()
    # try:
        
    #     a.add_user("a","a","2@email","a")
    # except MySQLdb._exceptions.IntegrityError:
    #     print("user already ex")
    emails = "1@email", "2@email", "3@email"
    a.user_games(emails)
    # ts = int(time.time()) 
    # print(ts)
    # a.remove_users_before_date(ts)

