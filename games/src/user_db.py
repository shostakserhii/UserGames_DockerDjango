"""This module is mainly for the Users class """

import time

import MySQLdb

from games.src.client import Client


MONTH = 2629800

class Users: #rename to users_manager
    """Object Users gives opportunity to:
            -add user to database,
            -show games for the list of users
            -delete old users
    """

    def __init__(self):
        self.db_client = Client()

    def add_users(self, name, surname, email, passwd, add_ts=int(time.time())):
        """This method adds user to database

        It takes arguments and passes them to Client's add_user method via db_client obj

        Args:
            name ([str]): name for new user
            surname ([str]): surname for new user
            email ([str], UNIQUE): email for new user
            passwd ([str]): password for new user
            add_ts ([int], optional): [description]. Defaults to None.

        Returns:
            [str]: 'Success' - everything worked well
                   'User with this login is already exists' - when email already exists
                   'Failed' - in case of any other error
        """        
        result = ''
        try:
            self.db_client.add_user(name, surname, email, passwd, add_ts)
            result = "Success"
        except MySQLdb._exceptions.IntegrityError:
            result = "User with this login is already exists"
        except Exception as e:
            print(f"Failed to connect DB \n{e}")
            result = "Failed"
        finally:
            return result

    def games_for_users(self, emails):
        """This method prints games for the users

        Takes list with the users' and show games assigned to them

        Args:
            logins_list ([list(str)]): list of the tuples(user email)
        """        
        self.db_client.user_games(emails)

    def delete_old_users(self, ts=int(time.time())- MONTH):
        """Deletes all the users from database that were created earlier ts

        Args:
            ts ([int]): time stamp, Default: 1 month ago
        """        
        print(ts)
        self.db_client.remove_users_before_date(ts)


if __name__ == "__main__":
    login_list = '4@email', '1@email', '2@email' 
    u = Users()
    u.add_users("s" ,"s" ,"c" , "d", 1623245857-13629743)
    u.games_for_users(login_list)
    u.delete_old_users()