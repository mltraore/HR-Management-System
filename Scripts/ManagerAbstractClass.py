from abc import ABCMeta, abstractmethod, ABC
import sqlite3


class ManagerAbstractClass(metaclass=ABCMeta):
    def __init__(self):
        self._identity = ""
        self._name = ""
        self._surname = ""
        self._phone = ""
        self._email = ""
        self._password = ""
        self._picture = ""
        self._salary = 0
        self._gender = ""
        self._address = ""
        self._position = ""
        self._startDate = ""
        super().__init__()

    # identity getter and setter
    @property
    @abstractmethod
    def identity(self):
        raise NotImplementedError()

    @identity.setter
    @abstractmethod
    def identity(self, value):
        raise NotImplementedError()

    # name getter and setter
    @property
    @abstractmethod
    def name(self):
        raise NotImplementedError()

    @name.setter
    @abstractmethod
    def name(self, value):
        raise NotImplementedError()

    # surname getter and setter
    @property
    @abstractmethod
    def surname(self):
        raise NotImplementedError()

    @surname.setter
    @abstractmethod
    def surname(self, value):
        raise NotImplementedError()

    # phone getter and setter
    @property
    @abstractmethod
    def phone(self):
        raise NotImplementedError()

    @phone.setter
    @abstractmethod
    def phone(self, value):
        raise NotImplementedError()

    # email getter and setter
    @property
    @abstractmethod
    def email(self):
        raise NotImplementedError()

    @email.setter
    @abstractmethod
    def email(self, value):
        raise NotImplementedError()

    @property
    @abstractmethod
    def password(self):
        raise NotImplementedError()

    @password.setter
    @abstractmethod
    def password(self, value):
        raise NotImplementedError()

    # picture getter and setter
    @property
    @abstractmethod
    def picture(self):
        raise NotImplementedError()

    @picture.setter
    @abstractmethod
    def picture(self, value):
        raise NotImplementedError()

    # salary getter and setter
    @property
    @abstractmethod
    def salary(self):
        raise NotImplementedError()

    @salary.setter
    @abstractmethod
    def salary(self, value):
        raise NotImplementedError()

    # gender getter and setter
    @property
    @abstractmethod
    def gender(self):
        raise NotImplementedError()

    @gender.setter
    @abstractmethod
    def gender(self, value):
        raise NotImplementedError()

    # address getter and setter
    @property
    @abstractmethod
    def address(self):
        raise NotImplementedError()

    @address.setter
    @abstractmethod
    def address(self, value):
        raise NotImplementedError()

    # position getter and setter
    @property
    @abstractmethod
    def position(self):
        raise NotImplementedError()

    @position.setter
    @abstractmethod
    def position(self, value):
        raise NotImplementedError()

    # startDate getter and setter
    @property
    @abstractmethod
    def startDate(self):
        raise NotImplementedError()

    @startDate.setter
    @abstractmethod
    def startDate(self, value):
        raise NotImplementedError()

    #########################        Database Operations         ###########################

    @abstractmethod
    def insertEmployee(self):
        try:
            con = sqlite3.connect('../DA/HRDatabase.db')
            cur = con.cursor()
            query = "INSERT INTO managersTable (identity,name,surname,phone,email,password,picture,salary,gender,address,position,startDate) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)"
            cur.execute(query, (
            self._identity, self._name, self._surname, self._phone, self._email, self._password, "", self._salary,
            self._gender, self._address, self._position, self._startDate))
            con.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False
        finally:
            con.close()

    @abstractmethod
    def login(self):
        try:
            con = sqlite3.connect('../DA/HRDatabase.db')
            cur = con.cursor()
            query = "SELECT email, password FROM managersTable"
            employees = cur.execute(query).fetchall()
            for employee in employees:
                if employee[0] == self._email and employee[1] == self._password:
                    return True
            return False
        except sqlite3.Error as e:
            print(e)
            return False
        finally:
            con.close()

        # # Update employee
        # @abstractmethod
        # def updateEmployee(self):
        #     raise NotImplementedError()
        #
        #
        # # load data for corresponding identity
        # @abstractmethod
        # def loadData(self, identity):
        #     raise NotImplementedError()
        #
        # # Delete employee  by identity
        # @abstractmethod
        # def deleteEmployeeById(self,identity):
        #     raise NotImplementedError()
        #
        # # Delete employee  by name
        # @abstractmethod
        # def deleteEmployeeByName(self,name):
        #     raise NotImplementedError()
        #
        # # Get Employee  single  by identity
        # @abstractmethod
        # def getEmployeeByName(self,identity):
        #     raise NotImplementedError()
        #
        # # Get Employee  single  by Full name
        # @abstractmethod
        # def getEmployeeByName(self,name):
        #     raise NotImplementedError()
