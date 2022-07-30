import pandas as pd
from statistics import *
import numpy as np
from ftplib import parse150
from getpass import getpass
import os
from matplotlib import pyplot as plt
run = True
menu = True
play = False
ok = False
do = False
def clear():
    os.system("clear")
def draw():
    print("Xx------------------xX")
while True:
    count=0
    Iws = "Welcome to our spreadsheet database!"
    draw()
    username = input("Enter Username ")
    password = getpass("Enter Password ")
    draw()
    if username == "GIIS":
        ok = True
    if password == "punggol":
        do = True
        play = True
    if play == True:
        pass
    if do == True:
        if ok == True:
                while True:
                    if count!=0:
                        q = input("Do you want to continue(y/n)? ")
                    else:
                        q='y'
                    if q .strip() .lower() == "y":
                        print("")
                        print(Iws)
                        hello=[]
                        meany=0
                        myean=0
                        bruh=pd.read_csv('Hihi.csv')
                        bruh1=bruh.to_string()
                        print("Do you want to see the pie chart for a particular field (f), or do you want to see all the data of a patient (p)?")
                        choice=input()
                        if choice=='f':
                            field=input("What field of the data would you like to see? ")
                            age=bruh.loc[:,field]
                            age=age.tolist()
                            age1=list(dict.fromkeys(age))
                            for i in range(0, len(age1)):
                                count=age.count(age1[i])
                                hello.append(count) #hello contains the count of one number in the entire database
                            y=np.array(hello)
                            title1="Intensity of "+str(field)+ " for the patients"
                            if field=="Gender":
                                if hello[0]>hello[1]:
                                    print("There are more number of males than females in this data-set")
                                else:
                                    print("There are more number of females than males in this data-set")
                            else:
                                for i in range(0, len(hello)):
                                    maen=hello[i]*age1[i]
                                    meany=meany+maen
                                    myean=myean+hello[i]
                                themean=meany/myean
                                themean=round(themean,2)
                                srievatsan=age1[hello.index(max(hello))]
                                print("The modal number for how extreme the disease is is", srievatsan)
                                if field=="Age":
                                    print("The mean", field, "of the patients is", themean)
                                else:
                                    print("On average", themean, "is how extreme",field,"is for the patients")
                                if themean>=5:
                                    print("Most of the patients are in high-risk to", field, "since the average condition is", themean)
                                if themean<=2:
                                    print(field,"is at a relatively low-risk for the patients since the average condition is just", themean)
                                else:
                                    print(field, "is at a moderate-risk on average for the patients since the average is neither too high nor too low")
                            plt.title(title1)
                            plt.pie(y,labels=age1,autopct='%1.1f%%')
                            plt.show()
                        if choice=='p':
                            patient=int(input("Whose patients data do you want to see? "))
                            data=bruh.loc[patient]
                            data1=data.drop(labels=['Level'])
                            print(data1)
                            print("This patient has a", data["Level"], "chance of being vulnerable to cancer")
                            anchoice=input("Do you wish to see more details of the patient (y for yes and n for no)? ")
                            if anchoice=='y':
                                data2=data1.tolist()
                                bahru=bruh.columns.values.tolist()
                                for i in range(1, 4):
                                    data2.remove(data2[0])
                                    bahru.remove(bahru[0])
                                print("The most chronic disease for this patient is", bahru[data2.index(max(data2))], "with a value of", max(data2))
                                print("The least chronic disease for this patient is", bahru[data2.index(min(data2))], "with a value of", min(data2))
                        count=count+1
                    else:
                        print("Ok")
                        quit()
    else:   
        print("Error: Incorrect Password and/or Username")
        break           