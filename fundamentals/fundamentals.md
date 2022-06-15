#### method in python:

1) instance method
2) class method
3) static method

#### self keyword --> represent instance/object from a class

_________________________________________________________________________________________________


How to call method:

1)className.methodName(...) --> methodName(params .....) --> without "self" param

--> if has "self" param it will display type error: "missing 1 required positional argument: 'self'"

2)use self or object from that class, but your method must contain "self" parameter. Otherwise your first parameter
will contain reference object/instance from this class. or it will display "takes 0 positional arguments but 1 was given"

_________________________________________________________________________________________________
#### initialize empty function using lamda - sample 1

def someFunct():
    print("from some function")

a = False
f = lambda : ...


if a:
    f = someFunct

for x in list_of_attribs:
  f()

_________________________________________________ or _________________________________________________

#### initialize empty function using lamda - sample 2

def someFunct():
    print("from some function")

a = False
f = lambda : None


if a:
    f = someFunct

for x in list_of_attribs:
  f()

_________________________________________________________________________________________________


#### acces list item from backwards

list = [10, 12, 14, 13]

list[-1] --> 13
list[-2] --> 14

... dst


_________________________________________________________________________________________________

#### list comprehension( operation inside list )

val = [1,2,3,4,5] <br>
x_val = 4 <br>
new_val = [d for d in val if d != x_val] <br>

--> val = [1,2,3,5]

_________________________________________________________________________________________________

#### Error Handling -- with AttributeError

---------- without AttributeError ---------------

-->if code inside "try" run sys.exit() , it will not run sys.exit()
   but it will execute "except" code

try: 
    ---- some code with sys.exit()  ---
except:
    sys.exit("....some error message here ....")

-----------------------------------------------------


so we must use AttributeError in "except"


---------- with AttributeError ---------------
try: 
    ---- some code with sys.exit()  ---
except AttributeError:
    sys.exit("....some error message here ....")
    
-----------------------------------------------



