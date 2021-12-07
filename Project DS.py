#PyCharm
#Concept of Object Oriented Programming

#An object call person
#Stored characteristic of the "person" class.
class person:
    fever = 0
    breathing = 0
    cough = 0
    sore = 0
    diarrhea = 0
    number = 0

#A call function that refer to the object self and set the characteristic to a variable that we can store as data
    def __init__(self, fever, breathing, cough, sore, diarrhea, number):
        self.fever = fever
        self.breathing = breathing
        self.cough = cough
        self.sore = sore
        self.diarrhea = diarrhea
        self.number = number




#Input of data from each patient on our Excel sheet.
person1 = person(1, 1, 1, 1, 1, 1)
person2 = person(1, 1, 1, 1, 0, 2)
person3 = person(1, 1, 0, 0, 1, 3)
person4 = person(1, 1, 1, 0, 1, 4)
person5 = person(1, 1, 1, 0, 1, 5)
person6 = person(1, 1, 1, 1, 0, 6)
person7 = person(1, 1, 1, 0, 1, 7)
person8 = person(1, 1, 1, 0, 1, 8)
person9 = person(1, 1, 1, 0, 1, 9)
person10 = person(1, 1, 1, 0, 1, 10)
person11 = person(1, 1, 1, 0, 1, 11)
person12 = person(1, 1, 1, 0, 1, 12)
person13 = person(1, 1, 1, 0, 1, 13)
person14 = person(1, 1, 1, 0, 1, 14)
person15 = person(1, 1, 1, 0, 1, 15)
person16 = person(1, 1, 1, 0, 1, 16)
person17 = person(1, 1, 1, 0, 1, 17)
person18 = person(1, 1, 1, 0, 1, 18)
person19 = person(1, 1, 1, 0, 0, 19)
person20 = person(1, 1, 1, 0, 0, 20)
person21 = person(1, 1, 1, 0, 0, 21)
person22 = person(1, 1, 1, 0, 0, 22)
person23 = person(1, 1, 1, 0, 0, 23)
person24 = person(1, 0, 0, 0, 1, 24)
person25 = person(1, 0, 0, 0, 1, 25)
person26 = person(1, 0, 0, 0, 1, 26)
person27 = person(1, 0, 0, 0, 1, 27)
person28 = person(1, 0, 0, 0, 1, 28)
person29 = person(1, 0, 0, 0, 1, 29)

#Created a list for every single person in our data.
#Created a count system

peopleList = [person1, person2, person3,person4, person5, person6, person7, person8, person9, person10, person11, person12, person13, person14, person15, person16,person17, person18, person19, person20, person21, person22, person23, person24, person25, person26, person27, person28, person29]
feveramount = 0
breathingamount = 0
coughamount = 0
soreamount = 0
diarrheaamount = 0

#Conditional formatting.

for person in peopleList:
    symptomsamount = 0
    if person.fever == 1:
        feveramount += 1
        symptomsamount += 1
    if person.breathing == 1:
        breathingamount += 1
        symptomsamount += 1
    if person.cough == 1:
        coughamount += 1
        symptomsamount += 1
    if person.sore == 1:
        soreamount += 1
        symptomsamount += 1
    if person.diarrhea == 1:
        diarrheaamount +=1
        symptomsamount += 1
    if symptomsamount < 4:
        print("Patient number: "+str(person.number)+" does not have COVID.")
    if symptomsamount >= 4:
        print("Patient number: "+str(person.number)+" has COVID.")



