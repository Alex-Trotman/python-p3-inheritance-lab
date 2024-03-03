#!/usr/bin/env python

from user import User

class Student(User):
    
    def learn(self, str):
        self.knowledge.append(str)