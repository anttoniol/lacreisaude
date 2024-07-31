import mysql.connector

from api.properties import Properties


class Repository:
    __properties = Properties()

    def __init__(self):
        user = self.__properties.get_value("mysql", "user")
        password = self.__properties.get_value("mysql", "password")
        host = self.__properties.get_value("mysql", "host")
        port = int(self.__properties.get_value("mysql", "port"))

        self._db = mysql.connector.connect(host=host, port=port, user=user, password=password, database="clinica")

