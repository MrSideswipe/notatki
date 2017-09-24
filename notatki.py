i = 1

while i < 10 :
	print(i)
	i+=1

print()
for j in range (1,10):
	print(j)
else:
	print("end of for loop")

print()
for k in [1,4,6]:
	print(k)

print()
list(enumerate(['a', 'b', 'c']))
for i, e in enumerate(['a', 'b', 'c']):
	print(i, e)

#listy - mutable
print()
l = list()
print(l)

l = ['a', 2, ['b', 3]]
print(l)
print(l[1])
print(l[2][1])

print()
ll = [[]] * 3 
print(ll)

ll[1].append(3)
print(ll)

ll[2].append(1)
print(ll)

# krotka - immutable
print()
t = tuple()
print(t)

t = ('a', 10, ('b', 20))
print(t)

print()
tt = (1,)
print(tt)

ttt = tt + ('b',)
print(ttt)
print(ttt[0])
print(ttt[1])

#ttt[1] = 'a' - immutable, nie zadziala

a, b = ttt
print("a =", a)
print("b =", b)

print()
a, b = b, a
print("a =", a)
print("b =", b)

print()
word = "python"
print(word[1:3])
print(word[3:])
print(word[:3])
print(word[-3:])
print(word[:-3])
print(word[0:4:2])
print(word[1:4:2])
print(word[0:4:1])
print(word[0:4:3])

#slownik - mutable
print()
print({'a': 2, 'b': 4})
print(dict(a=2, b=4))
print(dict(zip(('a', 'b'), (2,4))))

for thing in zip(('a', 'b'), (2,4)):
	print(thing)

a = {'a': 2, 'b': 4}
print(a.items())

print(a.keys())

print(a['a'])

print('a' in a)

print(len(a))

a['c'] = 6
print(a)


#zbiory - mutable
print()
print(set([1,2,3,4]))


#funkcje
def sayXTimes(message, times = 2):
	print((message + ' ') * times)

sayXTimes('python')
sayXTimes('python', 1)
sayXTimes(times = 1, message = 'python')

def sayXTimesV2(*args, **kwargs):
	print(args)
	print(kwargs)

sayXTimesV2(1,2,3,4,5, a=2, b=4)

a = 1
def adding (variable, value):
	variable += value
	print("Inside function variable is", variable)

print(a)
adding(a, 2)
print(a)

#dynamiczne typowanie
x = 5
print(x, type(x), repr(x))
x = "5"
print(x, type(x), repr(x))

a = 'a'
a =+ 3 #a zmienilo sie na 3
print(a)


#duck typing
print()

class Car:
    def engine(self): 
        print("Wrrrrr!")
    def body(self): 
        print("The car is red.")
 
class Person:
    def engine(self):
        print("The person imitates a car.")
    def body(self): 
        print("The person is crazy and decided to paint himself red color.")

def onTheRoad(something):
    something.engine()
    something.body()

def game():
    corvette = Car()
    john = Person()
    onTheRoad(corvette)
    onTheRoad(john)

game()

#listy ciag dalszy
print()
l = [1,2,4]
l.extend([3,5,6])
print(l)

del l[1]
print(l)

del l[0:2]
print(l)

del l
#print(l) # l is not defined

#stos
print()
l = [1,2,3,4]
l.pop()
print(l)
l.append(5)
print(l)

#kolejka
print()
l = [1,2,3]
l.pop(1)
print(l)
l.append(5)
print(l)


#list compehension
print()
print([x**3 for x in range(5)])

print([(x,y) for x in [1,2,3] for y in [3,4,5,6] if x != y])

a = { x*2 for x in range(5)}
b = { x**2 for x in range(5)}
print(a)
print(b)
print(a&b)


#lamba wyrazenia
print()
operatorPotegi = lambda x, y: x**y
print(operatorPotegi(2,3))

lambdaIf = lambda x: "mniejsze od 5" if x < 5 else "wieksze od badz rowne 5"
print(lambdaIf(4))
print(lambdaIf(5))

# sortowanie
print()
s = (3,2,6,3)
print(sorted(s))

print()
l = [4,2,6,8,4,3]
print(l)
l.sort(reverse=True)
print(l)
l.sort(reverse=False)
print(l)


#domkniecia
print()
def outer():
    x = 137
    def inner():
        print(x)
    inner()

outer()

print()
def mult(x,y):
	return x*y
def fxy(f,x,y):
	return(f(x,y))
print(fxy(mult,2,4))

print()
def outerV2():
    x = 137
    def inner():
        nonlocal x
        print("inner",x)
        x = 0
    print("outer pre",x)
    inner()
    print("outer post",x)

outerV2()


#dekoratory
print()
def printV2(n):
	print("Message: %d" % n)


def enhanced(newFunction):
	def tmp(y):
		print("Enhanced version")
		return newFunction(y)
	return tmp

printV2(1)
printV2 = enhanced(printV2)
print()
printV2(1)


#obiektowosc
print()

class MyClass(object):
	def method1(self,x):
		print("Method1 ->", x, self.number)

	@classmethod
	def someclassmethod(cls,x):
		print(cls)
		print(x)

	def __init__(self):
		self.number = 100


MyClass.someclassmethod(1) #metoda statyczna, mozna wywolywac bez stworzenia instancji klasy

m = MyClass()
m.someclassmethod(2)

m.method1(5)
#MyClass.method1(5) nie wykona sie, gdyz metoda pobiera rowniez instacje klasy, ktorej w tym przypadku nie podaje

#mozna rowniez rozwijac klase po jej stworzeniu
print()
class Car:
	pass

samochod = Car()
samochod.name = 'Corvette'
samochod.color = "yellow"

print(samochod.name, samochod.color)


#Context Manager
print()
class MyContextManager():
    
    def __enter__(self): 
        print("Context prepared")
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Context closed ", exc_type, exc_value, traceback)

        
with MyContextManager() as f:
    print("Hello", f)
#przed kazdym wywolaniem klasy wywola sie funkcja __enter__, potem konretna czynnosc (tutaj print) i na koncu __exit__
#przydatna konstrukcja zwlaszcza przy laczeniu z baza danych

#metody specjalne
print()
class A:
	pass

print([A(), A(), A()])
print(repr(A()))
print(str(A()))


print()
print(bool(None)) #false
print(bool(0)) #false
print(bool([1,2,3])) #true
print(bool("")) #false

print()
y = 1
x = 'a'
print("x =", x)
print("y =", y)
print("x jest klasy", x.__class__)
print("y jest klasy", y.__class__)
print("x jest klasy", type(x))
print("y jest klasy", type(y))


#porownania
print()
a = 100
b = 100
print(a == b)
print(a is b)

print()
class B:
	pass
a = B()
b = B()
c = a 
print(a==b) #inna instancja klasy
print(a==c) #referencja do tej samej instancji klasy


print()
class Quad():
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def surface(self):
		return self.x*self.y

q1 = Quad(2,3)
print(q1.surface())

#dynamiczne tworzenie klas
print()
def personOrThing(name):
	if name == 'person':
		class Person():
			pass
		return Person
	else:
		class Thing():
			pass
		return Thing

print(personOrThing('person'))
print(personOrThing('else'))

print()
print(type(1))


class MyShinyClass():
    pass
print(MyShinyClass)
print(type('MyShinyClass', (), {}))

class Foo():
    bar = True

class FooChild(Foo):
    baz = False
print()
FooChild = type('FooChild', (Foo,), {'baz': False}) 
#w () co klasa pobiera, czyli klase rodzicielska
#w {}przypisanie zmiennych bedacych w srodku klasy, czyli atrybuty
print(FooChild)



#modul abc
print()
from collections.abc import Container

class MyList(Container):
	pass
print(dir(MyList)) #jakie zawiera metody


from abc import ABCMeta
from abc import abstractmethod

print()

class MyInterface(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass
    
    @abstractmethod
    def boo(self):
        pass


class MyImpl():
    pass

MyInterface.register(MyImpl)
o = MyImpl()
print(o)


class MyImpl2(MyInterface):
    pass

#o2 = MyImpl2()
#print(o2) nie zadziala, bo sa abstrakcyjne metody

#w pythonie proste warunki powinno sie pisac jak najproscie, wytlumaczenie na przykladach nizej
print()
car = 'Corvette'
owner = 'Jakub'
if car and owner:
	print(owner, "own", car)
#zamiast
if car != '' and len(owner) > 0:
	print(owner, "own", car)

if 'a' in owner:
	print("Owner has 'a' in his name")
#zamiast
if owner.find('a') != -1:
	print("Owner has 'a' in his name")

text = ['a', 'n', 'n', 'a']
name = ''.join(text)
print(name)
#zamiast
nameV2 = ''
for char in text:
	nameV2 += char
print(nameV2)

numbers = [1,3,6,8,9]
result = [x**2 for x in numbers if x < 9]
print(result)
#zamiast
resultV2 = []
for x in numbers:
	if x < 9:
		resultV2.append(x**2)
print(resultV2)


#mapowanie
print()
def p(*args):
   print([str(x) for x in args])
list(map(p, [1,2,3,4],[100]))

list(map(p, [1,2,3], [4,5,6]))

#range
print()
print(range(10))
#print(xrange(10))

#zip
print()
list1 = [1,2,3]
list2 = ['a', 'b', 'c']
print(list1)
print(list2)
list3 = zip(list1, list2)
for a, b in list3:
	print (a, b)

print()
