from abc import ABC

from ManagerAbstractClass import ManagerAbstractClass
import sqlite3


class HRManager(ManagerAbstractClass):
    @property
    def identity(self):
        return self._identity

    @identity.setter
    def identity(self, value):
        self._identity = value

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

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def picture(self):
        return self._picture

    @picture.setter
    def picture(self, value):
        self._picture = value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    @property
    def startDate(self):
        return self._startDate

    @startDate.setter
    def startDate(self, value):
        self._startDate = value

    def insertEmployee(self):
        super().insertEmployee()

    def login(self):
        return super(HRManager, self).login()


        


# if __name__ == "__main__":
#     xx = HRManager()
#     xx.identity = 500000000
#     xx.name = "xx"
#     xx.surname = "xx"
#     xx.email = "xx"
#     xx.phone = "+905556664433"
#     xx.picture = ""
#     xx.address = "Turkey/ISTANBUL"
#     xx.position = "HR Manager"
#     xx.gender = "male"
#     xx.startDate = "10/10/2015"
#     xx.salary = 10000
#     xx.password = "xx"
#     xx.insertEmployee()

    #print(xx.login())

# malick.mintha17@gmail.com
