import turtle

import another_module

print(another_module.another_variable)

timmy = turtle.Turtle() #Fetched a class turtle; constructed an object and saved it into timmy

#from turtle import Turtle
#timmy = Turtle()
#print(timmy) gives address 0f the object

my_screen = turtle.Screen()
my_screen.canvheight #an attribute
print(my_screen.canvheight)
my_screen.exitonclick() #a method


#car.stop() ; Here stop is a method
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

#Using a python package
#prettytable(already installed here)
#install a python package to use it
#then we can import .... 

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("name",["A", "B", "C", "D", "E", "F"])
table.add_column("value", ["a", "b", "c", "d", "e", "f"])
#We get a table formatted in ASCII

#Can manually change styles like align, border etc...