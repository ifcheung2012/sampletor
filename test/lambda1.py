# -*- coding: utf-8 -*-
__author__ = 'ifcheung'
class People:
    age=0
    gender='male'
    def __init__(self, age, gender):
        self.age = age
        self.gender = gender
    def toString(self):
        return 'Age:'+str(self.age)+'\tGender:'+self.gender

List=[People(21,'male'),People(20,'famale'),People(34,'male'),People(19,'famale')]
print 'Befor sort:'
for p in List:
    print p.toString()

List.sort(lambda p1,p2:cmp(p1.age,p2.age))
print '\nAfter ascending sort:'
for p in List:
    print p.toString()

List.sort(lambda p1,p2:-cmp(p1.age,p2.age))
print '\nAfter descending sort:'
for p in List:
    print p.toString()


if __name__ == '__main__':
    pass