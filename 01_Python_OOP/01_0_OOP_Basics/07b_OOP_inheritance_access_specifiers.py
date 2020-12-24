"""
Access Modifiers implemented in Python
    To control the access of variables and methods in OOP, Python incorporates 
the implementation of access modifiers.(Public, Private, Protected)
"""



#####################################################################################################
class Student:
    """
    Protected Access Modifier:(_variablename)
        - It uses Single Underscore(_)
        - Public Attributes cannot be accessed directly from the object.
        - Public Member Functions can be accessed directly from the object.
        - During Inheritance, the derived class can access the super class's, member functions,
          but cannot access the protected attributes.
    
    This allows to the sub class to use the super class's functions while protecting the data being 
    stored in the super class variables. 
    """
    #Protected Class Attribute 
    _name = None
    _roll = None
    _branch = None

    #Super Class Constructor
    def __init__(self, name, roll, branch):
        self._name = name
        self._roll = roll
        self._branch =  branch
    
    #Protected member function
    def _displayRollandBranch(self):
        print("Roll: ",self._roll)
        print("Branch: ",self._branch)

class Geek(Student):
    def __init__(self,name,roll,branch):
        Student.__init__(self,name,roll,branch)
    
    def displayDetails(self):

        print("Name: ",self._name)
        self._displayRollandBranch()


protec_obj_test_1 = Student('Arka','15MIS0345','it')
protec_obj_test_1._displayRollandBranch()

"""
Test if you can access the super class's protected attributes.
protec_obj_test_1._roll
protec_obj_test_1._name 
"""

protec_obj_test =Geek('Amritanshu','15MIS0222','cse')
protec_obj_test.displayDetails()
protec_obj_test._displayRollandBranch()

"""
Test if you can use the protected attributes by calling them via sub class object.
protec_obj_test._name
protec_obj_test._roll
"""



#######################################################################################################
class Education:
    """
    Private Access Modifier:(__variablename)
        - It uses Double Underscore(__)
        - Private Attributes cannot be accessed outside the class directly.
        - Private Methods cannot be accessed outside the class directly.
        - Private Attributes and Methods cannot be accessed in the Derived class.
    
    The only way to access the private attributes and methods, is to create public or protected method,
    which will indirectly access the attributes and methods. This allows the code to be secure and protected,
    as using the object, the user can never know, which private methods and attributes are being invoked. 

    """
    #Private Class Attributes
    __name = None
    __rollno = None
    __branch = None
    
    #Constructor
    def __init__(self, name, rollno,branch):
        self.__name = name
        self.__rollno = rollno
        self.__branch = branch

    #Private Member Functions
    def __displayDetails(self):
        print("Name of Student: ",self.__name)
        print("Roll No: ",self.__rollno)
        print("Branch of Student: ",self.__branch)

    #Public Member Function
    def access_private_function(self):
        self.__displayDetails()


#obj_test =Education('Amritanshu','15MIS0222','CSE')
#obj_test.access_private_function()

"""
Test if you can access the private attributes or methods.
obj_test.__name
obj_test.__rollno
obj_test.__displayDetails()
"""

#####################################################################################################################        

