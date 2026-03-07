#print ("Hello World")
#print ("Hi, i'm Iron Man")
# <-- Così si fanno i commenti :D

#print ("I am Iron Man \n" + "No, i'm Tony Stark \n" + "No, i am poppy ")
#print ("I am Poppy \n" * 10)

#age = 36
#numeri interi sono "Int" (integer)
#numeri decimali sono "Float" (Floating point number)
#print (age)
#print (type(age)) #Ti dice la Classe (str, int, float) dell'elemento

#Create a barista

print ("Hello! Welcome to NetworkChuck Coffee!!!")

name = input("What is your name?\n")



if name.lower() == "ben":
    answare = input("Are you Evil?\n")

    if answare.lower() != "no":  
        print("get outta here" + name + "!")
        exit()
    else:
        print("Oh, you are the " + name + " i like!")
else:
    print("Hi " + name + "! Thank you for coming today.\n")
 
#Le liste si creano inserendo stringhe tra paresntesi quadre []
#Le liste sono "ordinate", e possimoa riferirsci agli elementi nella lista attraverso gli "index", che sono numeri da 0 a infinito:
#lo 0 equivale al primo elemento di una lista, se vogliamo riferirsci all'ultimo useremo -1 (meno uno) e così via

menu_list = ["coffee", "cappuccino", "latte", "gin"]


#AGGIUNGERE elementi/liste in una lista esistente:
menu_list.append("cornetto")
menu_list.extend(["rum", "latte macchiato"])
menu_list = menu_list + ["frappuccino"]

#AGGIUNGERE un elemento in una posizione definita, es. in cima alla lista useremo lo zero:
menu_list.insert(0, "pastarella") 

#Per ELIMINARE tutto il contenuto di una lista si usa clear()
    #menu_list.clear()

#per ELIMINARE solo un elemento alla volta:
    #menu_list.remove("elemento")

#Per ELIMINARE elementi usando l'index si usa .pop
    #menu_list.pop(0)
#Se usiamo print possiamo farci mostrare quale elemento è stato eliminato:
    #print(menu_list.pop(0)) oppure, per farci mostrare la richiesta: 
    #print("This item was just deleted:" +  menu_list.pop(0))

print ("So " + name + " , what do you want to drink? We have got\n" + str(menu_list))


# Chiediamo l'ordine e lo "puliamo" subito da maiuscole e spazi extra con .lower e .strip
#order = input().strip().lower()

#if order in menu_list:
 
    #price = 8
    #quantity = input("How many " + order + " do you want?\n")

    #total = price * int(quantity)

    #print ("Thank you " + name + ". Your total is: $" + str(total))

    #print ("Your " + str(quantity) + " " + order + " will be here in a minute!")

#else:
    #print("I'm sorry " + name + ", we only have " + str(menu_list) + "wanna choose some of this?\n")
    #order = input().strip().lower()
    
    #if order in menu_list:
 
        #price = 8
        #quantity = input("How many " + order + " do you want?\n")

        #total = price * int(quantity)

        #print ("Thank you " + name + ". Your total is: $" + str(total))

        #print ("Your " + str(quantity) + " " + order + " will be here in a minute!")
    
    #else:
        #print("I'm sorry " + name + ", we are not here to please you!")
        #exit()

# CICLO INFINITO
while True:
    order = input().strip().lower()


    if order in menu_list:
        # Se true usiamo 'break' per distruggere il ciclo e andare avanti
        break 
    else:
        # Diamo l'errore e il ciclo ricomincia in automatico da 'order = input...'
        print("I'm sorry " + name + ", we only have " + str(menu_list) + ". Please try again.")

# Se Python arriva a questa riga, significa che ha eseguito il 'break' ed è uscito dal ciclo.
# Ora siamo SICURI al 100% che 'order' sia una bevanda valida.

price = 8
quantity = input("How many " + order + " do you want?\n")

total = price * int(quantity)

print ("Thank you " + name + ". Your total is: $" + str(total))
print ("Your " + str(quantity) + " " + order + " will be here in a minute!")
