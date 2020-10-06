import random
import os
import sys

print("Hello")

# this is a comment


name = "Derek"
print(name)
name = "Numbers Strings Lists Tuples Dictionary/Map"

name = "+ - * / % ** //"

print(name, 1 + 2)

quote = "\"Always remember backslash on both sides for quotes\""
print(quote)

multi_line_quote = ''' for new 
python programmers'''
new_string = quote + multi_line_quote

print("%s %s %s" % ('I like the quote', quote, multi_line_quote))

print("I dont like ", end="")
print("newlines")

grocery_list = ['Juice', 'Tomatoes', 'Potatoes',
                'Bananas']
print('First Item', grocery_list[0])
print('fourth Item', grocery_list[3])
grocery_list[0] = 'Green Juice'
print('New First Item', grocery_list[0])
print(grocery_list[1:3])
other_events = ['Wash car', 'Pick up kids', 'Cash check']
to_do_list = [other_events, grocery_list]
print(to_do_list)
print((to_do_list[1][1]))
grocery_list.append('Onions')
print(to_do_list)
grocery_list.insert(1, "Pickle")
grocery_list.remove("Pickle")
grocery_list.sort()
grocery_list.reverse()

del grocery_list[4]

print(to_do_list, "Im here")

to_do_list2 = other_events + grocery_list

print(len(to_do_list2))
print(min(to_do_list2))
print(max(to_do_list2))

# tuples are like lists but they cannot be changed after creation

pi_tuple = (3, 1, 4, 5, 9)
new_tuple = list(pi_tuple)
new_list = tuple(new_tuple)

len(new_list)
min(new_tuple)
max(new_tuple)

super_villians = {'Fiddler': "Isaac Bowin",
                  'Captain Cold': 'Leonard Snart',
                  "Weather Wizard": " mark mardon",
                  "Mirror Master": "Sam Scudder",
                  'Pied Piper': 'Thomas Peterson'}
print(super_villians['Captain Cold'])

del super_villians['Fiddler']

super_villians['Pied Piper'] = 'Hartley Rathaway'

print(len(super_villians))
print(super_villians.get("Pied Piper"))
print(super_villians.keys())
print(super_villians.values())

# conditionals section if else elif

age = 30
if age > 16:
    print('You are old enough to drive')
else:
    print('Youa re not old enough')

if age >= 21:
    print('You are old enough to drive a plane')
elif age >= 16:
    print('You are old enough to drive a car 2')
else:
    print('You are not old enough to drive')

# and or not

if ((age >= 1) and (age <= 18)):
    print("You get a birthday")
elif (age == 21) or (age >= 65):
    print("You get a birthday")
elif not (age == 30):
    print("You dont get a birthday")
else:
    print("You get a birthday party yeah")

# looping

# for loops
for x in range(0, 10):
    print(x, ' ', end='')
print('\n')
for y in grocery_list:
    print(y)
for x in [2, 4, 6, 8]:
    print(x)
num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]

for x in range(0, 3):
    for y in range(0, 3):
        print(num_list[x][y])

# while loops

random_num = random.randrange(0, 100)

while (random_num != 15):
    print(random_num)
    random_num = random.randrange(0, 100)

i = 0;

while (i <= 20):
    if (i % 2 == 0):
        print(i)
    elif (i == 9):
        break
    else:
        i += 1
        continue
    i += 1


# functions

def addNumber(fNum, lNum):
    sumNum = fNum + lNum
    return sumNum


print('\n', addNumber(1, 4))

# name= sys.stdin.readline()

# print('Hello', name)

long_string = "I'll catch you if you fall - The Floor"
print(long_string[0:4])
print(long_string[-5:])
print(long_string[:-5])

print("%c is my %s letter and my number %d number is %.5f" %
      ('X', 'favorite', 1, .14))
print(long_string.capitalize())

#case sensitive
print(long_string.find("Floor"))
#tests string if all are letters
print(long_string.isalpha())
#tests string if all numbers
print(long_string.isalnum())
#length
print(len(long_string))
#replace a word with another
print(long_string.replace("Floor", "Ground"))
#strip white space
print(long_string.strip())
#split string into a list
quote_list = long_string.split(" ")
print(quote_list)

#FileIO

test_file = open("test.txt", "wb")

print(test_file.mode)

print(test_file.name)

test_file.write(bytes("write me to the file\n", 'UTF-8'))

test_file.close()

test_file = open('test.txt', 'r+')

text_in_file = test_file.read()
print(text_in_file)

os.remove("test.txt")

#Objects

class Animal:
    #two underscores signifies private
    __name = None
    __height = 0
    __weight = 0
    __sound = 0
    def set_name(self, name):
        self.__name == name
    def get_name(self):
        return self.__name
    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height == height
        self.__weight = weight
        self.__sound = sound