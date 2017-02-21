'''
class example

define class Robbot (init, method)
use it
'''

class Robot:
        """Represents a robot, with a name."""

        population=0

        def __init__(self, name):
                self.name = name
                print "(initializing {})".format(self.name)

                Robot.population += 1

        def die(self):
                print "{} is being destroyed!".format(self.name)

                Robot.population -=1

                if Robot.population == 0:
                        print "{} was the last one".format(self.name)
                else:
                        print "There are still {:d} robots working.".format(Robot.population)

        def say_hi(self):
                print "Greetings, my masters call me {}".format(self.name)

        @classmethod
        def how_many(cls):
                print "We have {:d} robots.".format(cls.population)


droid1 = Robot("R2-D1")
droid1.say_hi()
Robot.how_many()

droid2=Robot("C-384")
droid2.say_hi()
Robot.how_many()

print "Robots are destroied"
droid1.die()
droid2.die()
