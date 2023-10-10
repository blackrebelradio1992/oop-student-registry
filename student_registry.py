class Student:
    def __init__(self, name="N/A", age=int(13), grade="12th"):
        self._name = name
        self._age = age
        self._grade = grade


    #getter for name
    @property
    def get_name(self):
        return self._name
    

    @get_name.setter
    def set_name(self, new_name):
        if (type(new_name) == str and new_name != new_name.isspace() and len(new_name) > 3):  #new name must be at least 3 characters
            self._name = new_name
        else:
            print("name must have at least 3 characters")

    @property
    def get_age(self):
        return self._age
    

    @get_age.setter
    def set_age(self, new_age):
        if (type(new_age) == int and new_age > 10 and new_age < 18): #new age must be and intiger & must be greater than 11 and lower than 18
            self._age = new_age
        else:
            return self._age == 13



    @property
    def get_grade(self):
        return self._grade

    def years_advanced(self):
        if (self._grade == "13th"):
            return f"{self._name} has advanced to the {self._grade}"

    @get_grade.setter
    def set_grade(self, new_grade):
        if (new_grade == "9th" or new_grade == "10th" or new_grade == "11th" or new_grade == "12th"):
            self._grade = new_grade
        else:
            return "Invalid grade"
        
        
    def __str__(self):
        return f"Student 1: {self._name}: Francisco, Age: {self._age}, Grade: {self._grade}"

    

