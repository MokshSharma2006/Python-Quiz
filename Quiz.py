from prettytable import PrettyTable    # To create a table of candidate performence

from playsound import playsound       # To playsound in the end of the program

import qrcode as code   # To create a qrcode of total marks obtained

import camelcase  # To do animation

import keyword  # To tell correct answer if the answer is wrong

import image  # To save & create the image of qrcode

import time  # To give specific time in some area of the code

import sys  # To give text animation

import os  # To clear the terminal after code execution

x=camelcase.CamelCase()

print()

write='The creator of this test welcomes you '          # Starting of the program

total=60

password = "concern"    # Password to enter the test

attempts = 3   # Password attempts

duration = 0  # Time for the program to run

def effect(text):                               # Typewritter animation in text
    for char in(text):
        print(char,end='')
        sys.stdout.flush()
        time.sleep(0.1)
effect(write)

print()

playsound(' Add the required file path that you have saved in yout disk PSK.mp3')      # Audio file

print()

# Passkey Attempts

while attempts > 0:          # Passkey attempts code
    user_password = input("\033[34mPasskey :- \033[0m")
    if user_password.lower() == password:
        print("\033[32mAccess Granted \033[0m")
        playsound('Add the required file path that you have saved in yout disk AG.mp3')       # Audio file
        break                   # Code will break after the correct password
    else:
        attempts -= 1     # Or it will minus the number of attempts given
        playsound('Add the required file path that you have saved in yout disk IC.mp3')       # Audio file
        print("\033[36mIncorrect passkey\033[0m")
        print()
        print("\033[33mAttempts left :- \033[0m",attempts)

print()

if attempts == 0:   # If attempts will be zero the program will exit automatically 
    print("\033[31mAccess Denied \033[0m")
    playsound('Add the required file path that you have saved in yout disk AD.mp3')       # Audio file

if attempts == 0:  
    playsound('Add the required file path that you have saved in yout disk PSKC.mp3')     # Audio file
    time.sleep(3)
    quit()      # Program will get quit after 0 passkey attempts

print()

os.system('cls' if os.name == 'nt' else 'clear')      # Clear the terminal after the upper code execution

playsound('Add the required file path that you have saved in yout disk audio0.mp3')      # Give's instruction in audio type

# Information gathering of the candidate

name=input('Enter your valid name :- ')  

print()

rollno = input('Enter your valid rollno :- ')

print()

division = input('Enter your valid Class :- ')

print()

section = input('Enter your valid section :- ')

print()

subject = input('Enter the valid subject :- ')


time.sleep(2)

os.system('cls' if os.name == 'nt' else 'clear')      # Clear the terminal after the upper code execution

a='welcome to the test'

b='your test is loading...'

print('1')
time.sleep(0.1)
print('2')
time.sleep(0.1)
print()
print(x.hump(a))

print()

print(x.hump(b))

z= "Correct 👌"

time.sleep(2)

os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal after the upper code execution

#Instruction to write the test

print()

print('Instructions :')

print()

print('Time Duration 1 Hour')

print()

print('This test contains 60 question')

print()

print('Do not give space after writting the answer otherwise it will cross it ')

print()

print('Passing marks will be 40')

print()

time.sleep(5)

# Asking the user if he had read the instruction or not

ask=input("\033[31mDid you read the instruction :- \033[0m")

while ask.lower() <= 'yes':
    break

while ask.lower() != 'yes':
    time.sleep(5)
    print()
    break

if ask.lower() == 'yes':
    print()
else:
    print()

os.system('cls' if os.name == 'nt' else 'clear')    # Clear the terminal after the upper code execution

score = 0   # Score will increase after every correct answer

score1 = 60  # Score will decrease after every wrong answer

print("\033[36m Test is going to start in... \033[0m")

print("\033[31m 1... \033[0m")

time.sleep(1)

print("\033[33m 2... \033[0m")

time.sleep(1)

print("\033[32m 3... \033[0m")

print()

print("\033[32m GO! \033[0m")

time.sleep(1)

os.system('cls' if os.name == 'nt' else 'clear')   # Clear the terminal after the uper code execution

playsound('Add the required file path that you have saved in yout disk audio1.mp3')      # Announcment of test start in audio type

print()

#Question & Answers

q1="Question no 1 > Which function is used to accept data from user ? "
print(q1)
print()
a1=input('Answer :- ')

if a1.lower() == 'input':
    print(z)
    score += 1
    score1 -= 1
elif a1.lower() == 'input()':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')
    

print()

q2="Question no 2 > Keys of dictionary must be : "
print(q2)
print()
a2=input('Answer :- ')

if a2.lower() == 'unique':
    print(z)
    score +=1
    score1 -= 1
else:
    print('Wrong')

print()

q3="Question no 3 > Proccessed data is called "
print(q3)
print()
a3=input('Answer :- ')

if a3.lower() == 'information':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q4="Question no 4 > Which data model uses tables ?"
print(q4)
print()
a4=input('Answer :- ')

if a4.lower() == 'relational':
    print(z)
    score += 1
    score1 -= 1
elif a4.lower() == 'rdbms':
    print(z)
    score += 1
    score1 -= 1
elif a4.lower() == 'relational database managment system':
    print(z)
    score += 1
    score1 -= 1
elif a4.lower() == 'relational-database-managment-system':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q5="Question no 5 > Is true an invalid keyword in python ?"
print(q5)
print()
a5=input('Answer :- ')

if a5.lower() == 'no':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')
    print('These are keywords')
    print(keyword.kwlist)
    time.sleep(0)

print()

q6="Question no 6 > In python which mode allows user to save and edit the file? "
print(q6)
print()
a6=input('Answer :- ')

if a6.lower() == "script":
    print(z)
    score += 1 
    score1 -= 1
elif a6.lower() == 'compiler':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q7= "Question no 7 > In SQL which clause eliminate the duplicate rows ?"
print(q7)
print()
a7=input('Answer :- ')

if a7.lower() == 'distinct':
    print(z)
    score += 1 
    score1 -= 1
else:
    print('Wrong')

print()

q8="Question no 8 > Which command will remove all the data from dictionary ?"
print(q8)
print()
a8=input('Answer :- ')

if a8.lower() == 'clear':
    print(z)
    score += 1
    score1 -= 1
elif a8.lower() == 'clear()':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q9="Question no 9 > Which type of memory is ROM? | volatile or non-volatile"
print(q9)
print()
a9=input('Answer :- ')

if a9.lower() == 'non-volatile':
    print(z)
    score += 1
    score1 -= 1
elif a9.lower() == 'non-volatile memory':
    print(z)
    score += 1
    score1 -= 1
elif a9.lower() == 'non volatile':
    print(z)
    score += 1
    score1 -= 1
elif a9.lower() == 'nonvolatile':
    print(z)
    score += 1
    score1 -= 1
elif a9.lower() == 'nonvolatilememory':
    print(z)
    score += 1
    score -= 1
elif a9.lower() == 'non volatile memory':
    print(z)
    score += 1
    score1 -= 1
elif a9.lower() == 'non':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q10="Question no 10 > Does cache memory saves data permanently ? "
print(q10)
print()
a10=input('Answer :- ')

if a10.lower() == 'no':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q11="Question no 11 > In which year python was created ?"
print(q11)
print()
a11=input('Answer :- ')

if a11.lower() == '1991':
    print(z)
    score1 -= 1
    score +=1 
else:
    print('Wrong')

print()

q12="Question no 12 >Python file is saved by which type of extension "
print(q12)
print()
a12=input('Answer :- ')

if a12.lower() == 'py,pyw':
    print(z)  
    score += 1
    score1 -= 1
elif a12.lower() == 'py':
    print(z)
    score1 -= 1
    score+= 1
elif a12.lower() =='pyw':
    print(z)
    score1 -= 1
    score += 1
elif a12.lower() == '.py':
    print(z)
    score += 1
    score1 -= 1
elif a12.lower() == '.pyw':
    print(z)
    score1 -= 1
    score += 1
elif a12.lower() == '.py,.pyw':
    print(z)
    score += 1
    score1 -= 1
elif a12.lower() == 'pyw,py':
    print(z)
    score += 1
    score1 -= 1
elif a12.lower() == '.pyw,.py':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q13="Question no 13 > Which type of python mode execute code immidiately "
print(q13)
print()
a13=input('Answer :- ')

if a13.lower() == 'interactive':
    print(z)
    score += 1
    score1 -= 1
elif a13.lower() == 'interpreter':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q14='Question no 14 > Three greater sign in python are called '
print(q14)
print()
a14=input('Answer :- ')

if a14.lower() == 'command prompt':
    print(z)
    score += 1
    score1 -= 1
elif a14.lower() == 'commandprompt':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q15="Question no 15 > Single line comment in python begins with "
print(q15)
print()
a15=input('Answer :- ')

if a15.lower() == '#':
    print(z)
    score += 1
    score1 -= 1
elif a15.lower() =='hashtag':
    print(z)
    score += 1
    score1 -= 1
elif a15.lower() == 'hash tag':
    print(z)
    score += 1
    score1 -= 1
elif a15.lower() == 'hash-tag':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q16="Question no 16 > How many indented space python take after declaration of function |"
q161 ='option 4 or 5'
print(q16,q161)
print()
a16=input('Answer :- ')

if a16.lower() == '4':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q17="Question no 17 > The reserved word used by python interpreter to recognize the structure of a program is termed as "
print(q17)
print()
a17=input('Answer :- ')

if a17.lower() == 'keyword':
    print(z)
    score += 1
    score1 -= 1
elif a17.lower() == 'keywords':
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q18="Question no 18 > What is the sign of floor division"
print(q18)
print()
a18=input('Answer :- ')

if a18.lower() == '//':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q19="Question no 19 > What type of symbol is used to end if statement "
print(q19)
print()
a19=input('Answer :- ')

if a19.lower() == ':':
    print(z)
    score += 1
    score1 -= 1
elif a19.lower() == 'colon':
    print(z)
    score += 1
    score1 -= 1
elif a19.lower() == 'colon(:)':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q20="Questionno 20 > Which type of brackets are used to created dictionary"
print(q20)
print()
a20=input('Answer :- ')

if a20.lower() == '{}':
    print(z)
    score +=  1
    score1 -= 1
elif a20.lower() == 'curly braces':
    print(z)
    score += 1
    score1 -= 1
elif a20.lower() == 'curly braces{}':
    print(z)
    score += 1
    score1 -= 1
elif a20.lower() == 'curlybraces':
    print(z)
    score += 1
    score1 -= 1
elif a20.lower() == 'curlybraces{}':
    print(z)
    score += 1
    score1 -= 1
elif a20.lower() == 'curly brackets':
    print(z)
    score += 1
    score1 -= 1
elif a20.lower() == 'curlybrackets':
    print(z)
    score += 1
    score1 -= 1
elif a20.lower() == 'curly brackets {}':
    print(z)
    score += 1
    score1 -= 1
elif a20.lower() == 'curlybrackets{}':
    print(z)
    score += 1
    score1 -= 1
elif a20.lower() == 'curly bracket':
    print(z)
    score += 1
    score1 -= 1
elif a20.lower() == 'curlybracket':
    print(z)
    score += 1
    score1 -= 1
elif a20.lower() == 'curly bracket{}':
    print(z)
    score += 1
    score1 -= 1
elif a20.lower() == 'curlybracket{}':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q21="Question no 21 > Which command is used to modify table "
print(q21)
print()
a21=input('Answer :- ')

if a21.lower() == 'update':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q22="Question no 22 > Which type of delete function is used to show the deleted item "
print(q22)
print()
a22=input('Answer :- ')

if a22.lower() == 'pop':
    print(z)
    score += 1 
    score1 -= 1
elif a22.lower() == 'pop()':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q23="Question no 23 > Which command allows you to perform data defination tasks "
print(q23)
print()
a23=input('Answer :- ')

if a23.lower() == 'ddl':
    print(z)
    score += 1 
    score1 -= 1
elif a23.lower() == 'ddl command':
    print(z)
    score += 1  
    score1 -= 1
elif a23.lower() == 'data definition language':
    print(z)
    score += 1
    score1 -= 1
elif a23.lower() == 'datadefinitionlanguage':
    print(z)
    score += 1
    score1 -= 1
elif a23.lower() == 'data-definition-language':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q24="Question no 24 >Which command allows you to perform data manipulation tasks "
print(q24)
print()
a24=input('Answer :- ')

if a24.lower() == 'dml':
    print(z)
    score += 1 
    score1 -= 1
elif a24.lower() == 'dml command':
    print(z)
    score += 1
    score1 -= 1
elif a24.lower() == 'data manipulation language':
    print(z)
    score += 1
    score1 -= 1
elif a24.lower() =='datamanipulationlanguage':
    print(z)
    score += 1
    score1 -= 1
elif a24.lower() == 'data-manipulation-task':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q25="Question no 25 > Which command help to use the database"
print(q25)
print()
a25=input('Answer :- ')

if a25.lower() == 'use':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q26="Question no 26 > Which command help to fetch data from table"
print(q26)
print()
a26=input('Answer :- ')

if a26.lower() == 'select':
    print(z)
    score += 1
    score1 -= 1
elif a26.lower() == 'select command':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q27="Question no 27 > Which Command shows the list of database"
print(q27)
print()
a27=input('Answer :- ')

if a27.lower() == 'show databases;':
    print(z)
    score +=1
    score1 -= 1
elif a27.lower() == 'show':
    print(z)
    score += 1
    score1 -= 1
elif a27.lower() == 'show;':
    print(z)
    score += 1
    score1 -= 1
elif a27.lower() == 'show ;':
    print(z)
    score += 1
    score1 -= 1
elif a27.lower() == 'show database':
    print('Use show databases add an s after the database')
    print(z)
    score += 1
    score1 -= 1
elif a27.lower() == 'showdatabases':
    print(z)
    score += 1
    score1 -= 1
elif a27.lower() == 'showdatabases;':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q28="Question no 28 > Full form of RAM"
print(q28)
print()
a28=input('Answer :- ')

if a28.lower() == 'random access memory':
    print(z)
    score += 1
    score1 -= 1
elif a28.lower() == 'randomaccessmemory':
    print(z)
    score += 1
    score1 -= 1
elif a28.lower() == 'random-access-memory':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q29="Question no 29 > Full form of ROM"
print(q29)
print()
a29=input('Answer :- ')

if a29.lower() == 'read only memory':
    print(z)
    score +=1 
    score1 -= 1
elif a29.lower() == 'readonlymemory':
    print(z)
    score += 1
    score1 -= 1
elif a29.lower() == 'read-only-memory':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q30 = "Question no 30 > Is cache memory faster than primary memory (RAM)"
print(q30)
print()
a30=input('Answer :- ')

if a30.lower() == 'yes':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q31="Question no 31 > Which part of cpu perform mathematical calculation,write its short form."
print(q31)
print()
a31=input('Answer :- ')

if a31.lower() == 'alu':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q32 ="Question no 32 > Is Ubuntu an operating system ?"
print(q32)
print()
a32=input('Answer :- ')

if a32.lower() =='yes':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q33="Question no 33 > Collection of 4 bits are called "
print(q33)
print()
a33=input('Answer :- ')

if a33.lower() == 'nibble':
    print(z)
    score1 -= 1
    score += 1 
else:
    print('Wrong')

print()

q34="Question no 34 > Is python a case sensitive language ?"
print(q34)
print()
a34=input('Answer :- ')

if a34.lower() == 'yes':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

a35="Question no 35 > Which key is used to run the command in python"
print(a35)
print()
a35=input('Answer :- ')

if a35.lower() == 'f5':
    print(z)
    score += 1 
    score1 -= 1
else:
    print('Wrong')

print()

q36="Question no 36 > How many ASCII and Unicode character are there in python charcter sets | option 256 or 356"
print(q36)
print()
a36=input('Answer :- ')

if a36.lower() == '256':
    print(z)
    score += 1 
    score1 -= 1
else:
    print('Wrong')

print()

q37="Question no 37 > Are dicionary mutable ?"
print(q37)
print()
a37=input('Answer :- ')

if a37.lower() == 'yes':
     print(z)
     score += 1 
     score1 -= 1
else:
    print('Wrong')

print()

q38="Question no 38 > What is the sign of not equal too in python"
print(q38)
print()
a38=input('Answer :- ')

if a38.lower() == '!=':
    print(z)
    score += 1 
    score1 -= 1
elif a38.lower() == '<>':
    print(z)
    score += 1
    score1 -= 1
elif a38.lower() == '!=,<>':
    print(z)
    score += 1
    score1 -= 1

elif a38.lower() == '<>,!=':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q39="Question no 39 > Does iteration repeats a statement ?"
print(q39)
print()
a39=input('Answer :- ')

if a39.lower() == 'yes':
    print(z)
    score += 1 
    score1 -= 1
else:
    print('Wrong')

print()

q40='Question no 40 > What does astrick (*) means ?'
print(q40)
print()
a40=input('Answer :- ')

if a40.lower() == 'all':
    print(z)
    score += 1 
    score1 -= 1
else:
    print('Wrong')

print()

q41="Question no 41 > Can we add multi line comments in python ?"
print(q41)
print()
a41=input('Answer :- ')

if a41.lower() == 'yes':
    print(z)
    score += 1 
    score1 -= 1
else:
    print('Wrong')

print()

q42="Question no 42 > Is _init_ a function or variable"
print(q42)
print()
a42=input('Answer :- ')

if a42.lower() == 'function':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')
    
print()

q43="Question no 43 > Is text editor a utility software "
print(q43)
print()
a43=input('Answer :- ')

if a43.lower() == 'yes':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q44="Question no 44 > Which software creates a wall between the user and the computer"
print(q44)
print()
a44=input('Answer :- ')

if a44.lower() == 'os':
    print(z)
    score += 1 
    score1 -= 1
elif a44.lower() == 'operating system':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')
    
print()

q45="Question no 45 > Does binary number system has digit 0 and 1"
print(q45)
print()
a45=input('Answer :- ')

if a45.lower() == 'yes':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q46="Question no 46 > 1 kilo byte is equivlent to how many bytes "
print(q46)
print()
a46=input('Answer :- ')

if a46.lower() == '1024':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q47="Question no 47 > Which input device is used to provide audio data to computer"
print(q47)
print()
a47=input('Answer :- ')

if a47.lower() == 'microphone':
    print(z)
    score +=1
    score1 -= 1
else:
    print('Wrong')
    
print()

q48="Question no 48 > From which number does indexing start"
print(q48)
print()
a48=input('Answer :- ')

if a48.lower() == '0':
    print(z)
    score += 1
    score1 -= 1
elif a48.lower() == 'zero':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')
    
print()

q49="Question no 49 > Are 'in' and 'not in' membership operator "
print(q49)
print()
a49=input('Answer :- ')

if a49.lower() == 'yes':
    print(z)
    score1 -= 1
    score += 1
else:
    print('Wrong')

print()

q50="Question no 50 > 3**1**3 what will be the answer ? " 
print(q50)
print()
a=input('Answer :- ')

if a.lower() == '3':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q51="Question no 51 > What does cardinality represent"
print(q51)
print()
a51=input('Answer :- ')

if a51.lower() == 'rows':
    print(z)
    score += 1
    score1 -= 1
elif a51.lower() == 'record':
    print(z)
    score += 1
    score1 -= 1
elif a51.lower() == 'records':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q52="Question no 52 > What does degree represent"
print(q52)
print()
a52=input('Answer :- ')


if a52.lower() == 'column':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q53='Question no 53 > Name the place where python was invented'
print(q53)
print()
a53=input('Answer :- ')

if a53.lower() == 'netherland':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q54='Question no 54 > Full form of IP'
print(q54)
print()
a54=input('Answer :- ')

if a54.lower() == 'informationpractices':
    print(z)
    score += 1
    score1 -= 1
elif a54.lower() == 'information practices':
    print(z)
    score += 1
    score1 -= 1
elif a54.lower() == 'information practice':
    print(z)
    score += 1
    score1 -= 1
elif a54.lower() == 'informationpractice':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q55='Question no 55 > Is CMOS battery is important'
print(q55)
print()
a55=input('Answer :- ')

if a55.lower() == 'yes':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q56='Question no 56 > From which bracket does list start'
print(q56)
print()
a56=input('Answer :- ')

if a56.lower() == '[]':
    print(z)
    score += 1
    score1 -= 1
elif a56.lower() == 'square bracket':
    print(z)
    score += 1
    score1 -= 1
elif a56.lower() == 'square bracket[]':
    print(z)
    score += 1
    score1 -= 1
elif a56.lower() == 'squarebracket[]':
    print(z)
    score += 1
    score1 -= 1
elif a56.lower() == 'squary bracket':
    print(z)
    score += 1
    score1 -= 1
elif a56.lower() == 'squary bracket[]':
    print(z)
    score += 1
    score1 -= 1
elif a56.lower() == 'squarybracket[]':
    print(z)
    score += 1
    score1 -= 1
elif a56.lower() == 'square brackets':
    print(z)
    score += 1
    score1 -= 1
elif a56.lower() == 'squary brackets':
    print(z)
    score += 1
    score1 -= 1
elif a56.lower() == 'squarebracket':
    print(z)
    score += 1
    score1 -= 1
elif a56.lower() == 'squarybracket':
    print(z)
    score += 1
    score1 -= 1
elif a56.lower() == 'squarebrackets':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q57= 'Question no 57 > Sign of modulous'
print(q57)
print()
a57= input('Answer :- ')

if a57.lower() == '**':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q58= 'Question no 58 > Name the most popular opertaing system which is used for hacking'
print(q58)
print()
a58= input('Answer :- ')

if a58.lower() == 'kali linux':
    print(z)
    score += 1
    score1 -= 1
elif a58.lower() == 'kali':
    print(z)
    score += 1
    score1 -= 1
elif a58.lower() == 'parrot':
    print(z)
    score += 1
    score1 -= 1
elif a58.lower() == 'parrot os':
    print(z)
    score += 1
    score -= 1
elif a58.lower() == 'parrot-os':
    print(z)
    score += 1
    score -= 1
elif a58.lower() == 'kalilinux':
    print(z)
    score += 1
    score1 -= 1
elif a58.lower() == 'kali-linux':
    print(z)
    score += 1
    score -=1 
else:
    print('Wrong')

print()

q59= 'Question no 59 > Do we need an Graphic card (GPU) to start a PC'
print(q59)
print()
a59=input('Answer :- ')

if a59.lower() == 'yes':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

q60= ' Question no 60 > Name the factor which comes after the gigabyte(GB)'
print(q60)
print()
a60=input('Answer :- ')

if a60.lower() == 'tera byte':
    print(z)
    score += 1
    score1 -= 1
elif a60.lower() == 'terabyte':
    print(z)
    score += 1
    score1 -= 1
elif a60.lower() == 'tb':
    print(z)
    score += 1
    score1 -= 1
else:
    print('Wrong')

print()

time.sleep(duration)  # Time in which a candidate have to complete it 

time.sleep(2)

os.system('cls' if os.name == 'nt' else 'clear')    # Clear the terminal after the upper code execution

print("\033[31m Time Over \033[0m")

playsound('Add the required file path that you have saved in yout disk audio2.mp3')  # Says Time over in audio type

time.sleep(5)

os.system('cls' if os.name == 'nt' else 'clear')   # Clear the terminal after the upper code execution

Total=print("Total = "+str(score)+"Question Correct")    # Shows total correct answer given

print()

Percentage=print("You Got :"+str((score/60)*100)+"%")  # Takes out the percentage out of 100 of total correct question

print()

if score >= 40 :   # If the score is above 40 or equal to 40. The candidate is pass
    print('Pass 😊')
    print()
else:
    print('Please bhai padhai krle')
    print()

if score == 100:
    print('You scored total 100 marks')

time.sleep(1)

def create_table(data):   # Creating table of candidate performence and total correct & incorrect questions
    table = PrettyTable(data[0])
    for row in data[1:]:
        table.add_row(row)
    return table

data=[('Rollno','Name','Class','Section','Subject','Correct','Incorrect','Total'), 
      (rollno,name,division,section,subject,score,score1,total)]  # Creation of table

table= create_table(data)  

print(table)    # Printing the table in terminal

marks='Total marks obtained',score,'/60'

image=code.make(marks)      # Creation of qrcode of candidate marks

image.save('marks.jpeg')   # Saving of the qrcode

image.show('marks.jpeg')  # Shows qrcode 

print()

print()

print(os.listdir())   # Print the existing files in the folder

time.sleep(10)

print('Program will be ending in 1 minute')

time.sleep(60) #time

quit()
