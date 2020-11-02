# Author: Saurav Bhattarai 

class Lead:
    
    weight_sex = 10
    weight_age = 10
    weight_credit_score = 10
    
    def __init__(self, name, age, sex, credit_score, email):
        self.name = name
        self.age = age
        self.sex = -1 if sex == 'M' else 1
        self.credit_score = credit_score
        self.email = email
        self.value = self.heuristics()
        
    def heuristics(self):
        '''takes in a lead and return a value greater than 0\
        where closer to 0 means unlikely to convert into a borrower
        and closer to infinity meaning very likely to convert'''
        
        return Lead.weight_sex * self.sex + Lead.weight_age * self.age\
            + Lead.weight_credit_score * self.credit_score
    
    def __lt__(self, other):
        return self.value < other.value

    def __str__(self):
        return self.name + ' ' + str(self.age) + ' ' + ('M' if self.sex == -1 else 'F')\
            + ' ' + str(self.credit_score) + ' ' + self.email +\
            ' ' + str(self.value) 
