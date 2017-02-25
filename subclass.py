class SchoolMember:
    '''Represents any school member'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print '(initialized School member: {}).'.format(self.name)


    def tell(self):
        print 'hi~ my name is {} and I\'m {} years old'.format(self.name, self.age)

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print '(initialized teacher: {})'.format(self.name)

    def tell(self):
        SchoolMember.tell(self)
        print 'My salary is "{:d}"'.format(self.salary)

class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks= marks
        print '(inistialized student: {})'.format(self.name)

    def tell(self):
        SchoolMember.tell(self)
        print 'My marks is "{:d}"'.format(self.marks)


t = Teacher('Kim MJ', 50, 30000)
s = Student('Lee JW', 30, 94)

members = [t,s]
for member in members:
    member.tell()