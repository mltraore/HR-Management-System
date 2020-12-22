from abc import ABCMeta, abstractmethod, ABC
import sqlite3
class AbstractClass(metaclass = ABCMeta):
    def __init__(self):
        self._identity  = ""
        self._name      = ""
        self._surname   = ""
        self._phone     = ""
        self._email     = ""
        self._picture   = ""
        self._salary    =  0
        self._gender    = ""
        self._address   = ""
        self._position  = ""
        self._startDate = ""
        super().__init__()

    # identity getter and setter
    @property
    @abstractmethod
    def identity(self):
        raise NotImplementedError()

    @identity.setter
    @abstractmethod
    def identity(self,value):
        raise NotImplementedError()

    # name getter and setter
    @property
    @abstractmethod
    def name(self):
        raise NotImplementedError()

    @name.setter
    @abstractmethod
    def name(self,value):
        raise NotImplementedError()

    # surname getter and setter
    @property
    @abstractmethod
    def surname(self):
        raise NotImplementedError()

    @surname.setter
    @abstractmethod
    def surname(self,value):
        raise NotImplementedError()

    # phone getter and setter
    @property
    @abstractmethod
    def phone(self):
        raise NotImplementedError()

    @phone.setter
    @abstractmethod
    def phone(self,value):
        raise NotImplementedError()

    # email getter and setter
    @property
    @abstractmethod
    def email(self):
        raise NotImplementedError()

    @email.setter
    @abstractmethod
    def email(self,value):
        raise NotImplementedError()

    # picture getter and setter
    @property
    @abstractmethod
    def picture(self):
        raise NotImplementedError()

    @picture.setter
    @abstractmethod
    def picture(self,value):
        raise NotImplementedError()

    # salary getter and setter
    @property
    @abstractmethod
    def salary(self):
        raise NotImplementedError()

    @salary.setter
    @abstractmethod
    def salary(self,value):
        raise NotImplementedError()

    # gender getter and setter
    @property
    @abstractmethod
    def gender(self):
        raise NotImplementedError()

    @gender.setter
    @abstractmethod
    def gender(self,value):
        raise NotImplementedError()

    # address getter and setter
    @property
    @abstractmethod
    def address(self):
        raise NotImplementedError()

    @address.setter
    @abstractmethod
    def address(self,value):
        raise NotImplementedError()

    # position getter and setter
    @property
    @abstractmethod
    def position(self):
        raise NotImplementedError()

    @position.setter
    @abstractmethod
    def position(self,value):
        raise NotImplementedError()


    # startDate getter and setter
    @property
    @abstractmethod
    def startDate(self):
        raise NotImplementedError()

    @startDate.setter
    @abstractmethod
    def startDate(self,value):
        raise NotImplementedError()


    #########################        Database Operations         ###########################


    @abstractmethod
    def insertEmployee(self):
        try:
            con = sqlite3.connect('../DA/HRDatabase.db')
            cur = con.cursor()
            query = "INSERT INTO employeeTable (identity,name,surname,phone,email,picture,salary,gender,address,position,startDate) VALUES(?,?,?,?,?,?,?,?,?,?,?)"
            cur.execute(query, (self._identity,self._name, self._surname, "00", "00", "00", 3000, "00", "00", "00", "00"))
            con.commit()
        except sqlite3.Error as e:
            print(e)
            return False
        finally:
            con.close()
            return True


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

# class Base(MyClass):
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, value):
#         self._name = value
#
#     @property
#     def surname(self):
#         return self._surname
#
#     @surname.setter
#     def surname(self, value):
#         self._surname = value
#
#     def setData(self):
#         try:
#             con = sqlite3.connect('../DA/HRDatabase.db')
#             cur = con.cursor()
#
#             query = "INSERT INTO employeeTable (name,surname,phone,email,picture,salary,gender,address,position,startDate) VALUES(?,?,?,?,?,?,?,?,?,?)"
#             cur.execute(query,(self._name,self._surname,"00","00","00",1000,"00","00","00","00"))
#             con.commit()
#         except Error as e:
#             print(e)
#         finally:
#             con.close()
#
#
# if __name__ == "__main__":
#     xx = Base()
#     xx.name = "Mohamed0"
#     xx.surname = "Traore0"
#     xx.setData()


