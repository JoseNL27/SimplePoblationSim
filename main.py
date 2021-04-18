#A very simple poblation simulator made to study what happen when a society reaches the food-consumption limit.
#Made by ElBarto27. Feel free to reproduce this script giving the correspondent credits.
from scipy.stats import norm
import random

#Opening and clearing the file where the code will write how many people are alive each day.
file = open("poblation.txt","r+")
file.truncate(0)
file.close()

peopleDictionary = []
x= 0
y = 0
startingPob = 10

#Setting up the class.
class Person():
    def __init__(self):
        self.age = int((norm.rvs(size=1,loc=0.5,scale=0.15)[0]*10).round(0))            #Using a Gaussian distribution to randomize with accuracy the starter age for eacch gen0 member.
        self.death = False                                                              #Obviously each member will start alive.
        self.hunger = 1                                                                 #Defining the starter hunger for each member.

def start():                                                                            #Function who adds the gen0 individuals to the dictionary.
    for x in range(0,startingPob):  
         person = Person()
         peopleDictionary.append(person)

def day():                                                                              #Function for each day rutine.
    if len([person for person in peopleDictionary if person.death == False]) > 500:     #It sets the food limit.
        food = 400  
    else:                                                                               #If the food limit isn´t reached there´ll be food for the 75% of the poblation.
        food = int(len([person for person in peopleDictionary if person.death == False])*0.75) 

    for person in [person for person in peopleDictionary if person.death == False]:     #Starts each member functions.
        #print("#",peopleDictionary.index(person))
        if person.hunger >= 2 and food > 0:
            person.hunger = person.hunger - 2
            food = food - 1
        if person.hunger <= 1 and len([person for person in peopleDictionary if person.death == False]) > 1 and person.age in range (2,8):
            bornRate = random.randint(0,100)
            if bornRate < 56:
                newBorn()
        person.age += 1
        person.hunger += 1
        if person.age > 10:
            person.death = True
            peopleDictionary.remove(person)
        if person.hunger > 5:
            person.death = True
            peopleDictionary.remove(person)

def newBorn():
    person = Person()
    peopleDictionary.append(person)
    person.age = 0

start()

for y in range(0,300):
    day()
    print("DAY", y)
    print("|||",len([person for person in peopleDictionary if person.death == False]))
    saveFile1 = open("poblation.txt", "a")
    write1 = str(len([person for person in peopleDictionary if person.death == False])) + "\n"
    saveFile1.write(write1)
    saveFile1.close()
    y + 1
