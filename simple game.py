import sqlite3
from datetime import datetime

class Player:
    
#constuctor where we initialize the starting stats    
    def __init__(self):
        self.strenght = 1
        self.constitution = 1
        self.intelligence = 1
        self.wisdom = 1
        self.charisma = 1
        self.dexterity= 1
        self.gold=100

# A function to pay gold in game       
    def paygold(self,amount):
        self.gold=self.gold-amount
        print("Ο χρυσός σου μειώθηκε κατα",amount,"και τωρα έχεις",self.gold)

# A function to gain gold in game
    def gaingold(self,amount):
        self.gold=self.gold+amount
        print("Ο χρυσός σου αυξήθηκε κατα",amount,"και τωρα έχεις",self.gold)

#A function to get bonus stats and special stat if you are a wizard
    def wizard(self):
        self.charisma = self.charisma + 2
        self.wisdom = self.wisdom + 3
        self.arcanemastery=1
        print("Arcanemastery=",self.arcanemastery)

#A function to get bonus stats and special stat if you are a paladin
    def paladin(self):
        self.stenght = self.strenght + 3
        self.constitution = self.constitution + 2
        self.holywrath=1
        print("Holy Wrath=",self.holywrath)

#A function to get bonus stats and special stat if you are a thief
    def thief(self):
        self.dexterity=self.dexterity+3
        self.intelligence = self.intelligence +2
        self.poisonshadow=1
        print ("Shadow Poison=",self.poisonshadow)

# some move functions
    def east(self):
        print (c,name,"decided to go East")
        
    def west(self):
        print (c,name,"decided to go West")
        
    def north(self):
        print (c,name,"decided to go North")
          
    def south(self):
        print (c,name,"decided to go South")

#A function to start the game
    def startgame(self):
        print ("Γεια σου τρανε Ηρωα",name,".Αποφάσισες να ακολουθήσεις")
        print ("τους τρόπους του,",c)
        print ("Η περιπέτεια σου στην Empire μολίς ξεκίνησε!")

#A function for starting zone
    def oldtown(self):
        print("Χαιρέ ",c,"",name,"είσαι στην Οldtown την πρωτεύουσα της Empire")
        print("Βορεία ειναι το μαγεμένο Δάσος 'Blackwood'")
        print("Νοτία η παραθαλάσσια πόλη 'Seagull'")
        print("Δυτικά βρίσκεται το Στοιχειωμένο Καστρό του Κόμη")
        print("Και τέλος στην Ανατολή η 'Έρημος της Αλεπούς'")

#Player gives his or her name and creation of the instance of Player Class
name= (str(input("Πως σε λένε τρανέ ήρωα?\n")))
name = name.strip()
player1 = Player()

#Some starting variables
numberofplayers = 1
score = 0
time = str(datetime.now())

#Player decides his/her class in game
while True:
    c = str(input ("Εισαί Paladin,Thief ή Wizard\n"))
    c = c.strip()
    if c == ("Paladin") or c == ("paladin"):
        print ("Τα αρχικά σου stats",name,"είναι")
        player1.paladin()
        c="Paladin"
        break
    elif c=="Thief"or c=="thief":
        print ("Τα αρχικά σου stats",name,"είναι")
        player1.thief()
        c="Thief"
        break
    elif c=="Wizard"or c=="wizard":
        print ("Τα αρχικά σου stats",name,"είναι")
        player1.wizard()
        c="Wizard"
        break
    else :
        print ("Μπορείς να είσαι μονο Paladin,Thief ή Wizard τρανέ",name)

#Player decides if he or she wants to register in the Database
p_answers=['ok','OK','ΝΑΙ','Ναι','Υ','Ν','YES','NO','Yes','No']

print("Αγαπητέ",name,"θέλετέ να καταγραφεί το σκόρ σας στο Hall of Fame?\n")
answer = str(input())
answer = answer.strip()

if answer in p_answers :
    try :
        conn = sqlite3.connect('players.db')
        c = conn.cursor()
        c.execute(''' CREATE TABLE HallOfFame
            (ID INT ,
             NAME TEXT NOT NULL,
             SCORE INT,
             TIME TEXT ,
             CLASS TEXT);''')
        
        c.execute("INSERT INTO HallOfFame (ID,NAME,SCORE,TIME) VALUES (?,?,?,?)",
            (numberofplayers,name,score,time))
        conn.commit()
        
        print ("Αγαπητέ",name,"καταχωρήθηκές επιτυχώς στο Hall of Fame")
        conn.close()
        
    except sqlite3.Error as e1  :
        print ("Υπήρξέ καποίο πρόβλημα παρακαλώ δοκιμάστε αργότερα")
            
    finally:
        pass

#Print the starting stats        
print ("strenght=",player1.strenght)
print ("constitution=",player1.constitution)
print ("intelligence=",player1.intelligence)
print ("wisdom=",player1.wisdom)
print ("charisma=",player1.charisma)
print ("dexterity=",player1.dexterity)
print ("gold=",player1.gold)

#Calling some functions
player1.startgame()
player1.oldtown()

#Navigation throught calling the right Directions given by player
while True :
    dd=str(input("Που θες να πάς?"))
    dd = dd.strip()
    if dd=='North' or dd=='north':
        player1.north()
        break
    elif dd=='South' or dd=='south':
        player1.south()
        break
    elif dd=='West' or dd=='west':
        player1.west()
        break
    elif dd=='East' or dd=='east':
        player1.east()
        break
    else:
         print("Μπορείς να πάς μονο North,South,West or East\n")

#Keeping the console open until Enter button is pressed
open_cmd = input('Πατήστε enter για να εξέλθετε\n')








        



        
        

        








    
        
        

    
