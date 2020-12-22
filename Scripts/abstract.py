from abc import ABCMeta, abstractmethod, ABC
import sqlite3
from sqlite3 import Error

class MyClass(metaclass = ABCMeta):
      def __init__(self):
        _name = ""
        _surname = ""

        @property
        @abstractmethod
        def name(self):
            raise NotImplementedError()

        @name.setter
        @abstractmethod
        def name(self,value):
            raise NotImplementedError()

        @property
        @abstractmethod
        def surname(self):
            raise NotImplementedError()


        @surname.setter
        @abstractmethod
        def surname(self,value):
            raise NotImplementedError()

        @abstractmethod
        def setData(self):
            raise NotImplementedError()

class Base(MyClass):
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value

    def setData(self):
        try:
            con = sqlite3.connect('../DA/HRDatabase.db')
            cur = con.cursor()

            query = "INSERT INTO employeeTable (name,surname,phone,email,picture,salary,gender,address,position,startDate) VALUES(?,?,?,?,?,?,?,?,?,?)"
            cur.execute(query,(self._name,self._surname,"00","00","00",1000,"00","00","00","00"))
            con.commit()
        except Error as e:
            print(e)
        finally:
            con.close()


if __name__ == "__main__":
    xx = Base()
    xx.name = "Mohamed0"
    xx.surname = "Traore0"
    xx.setData()


