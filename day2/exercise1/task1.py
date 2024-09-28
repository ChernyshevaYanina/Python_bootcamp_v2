import time
import asincio

class Student:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.score = 0
        self.status = 'Queue'
        
class Examiner:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.