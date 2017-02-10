#exersise 1
if __name__ == '__main__':
    print 'This program is being run by itself'
else:
    print 'I am being importedfrom another module'

#exersise 2
import mymodule

mymodule.say_hi()
print 'Version', mymodule.__version__
print dir(mymodule)

#from mymodule import say_hi, __version__ --> not recommended
#from mymodule import * --> not import __version__