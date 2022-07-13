from colorama import *
import os
from time import *
from os import system
from msvcrt import *
from random import *
Map=raw_input("ENTER YOUR MAP NAME")
system("cls")
init()
f=open(Map,"r")
g=f.readlines()
NumberOfWalls=int(g[1][:-1])
ConsuleSize=[int((g[0])[:2]),int((g[0])[3:5])]
walls=[]
for i in range(2,NumberOfWalls+2):
    length=len(g[i])
    for n in range (length):
        if g[i][n]==" ":
            xofcoordinate=int(g[i][:n])
            yofcoordinate=int(g[i][n+1: ])

    walls+=[[int(yofcoordinate),int(xofcoordinate)]]

NumberOfEnemies=int(g[len(g)-1])
#--------------------------------------------------------------------------------
def Randomize():
    return(randint(0,3))

def Random_X() :
    return randint(2,ConsuleSize[0]-1)
def Random_Y() :
    return randint(2,ConsuleSize[1]-1)


def blocks():
    w=1
    v=1
    while w<ConsuleSize[1] :  #vertical(y's)
        v=1
        while v<ConsuleSize[0] :  #horizental(x's)
            if [w,v] in walls :
                print Back.MAGENTA+Fore.MAGENTA+position(w,v)+"I"+Back.RESET+Fore.RESET
            v+=1
        w+=1

def IsThereBlock(l,k) :
    if [l,k] in walls :
        return "NO"

def position(y,x):
    return "\033["+str(y)+";"+str(x)+"H"
#--------------------------------------------------------------------------------------------------
i=2
j=2

def Moving(i,j,M,Difficulty,NumberOfEnemies):
    EnemyPos=[]
    t=0
    if Difficulty==2 :
        NumberOfEnemies=NumberOfEnemies+10
    while t < NumberOfEnemies :
        X=Random_X()
        Y=Random_Y()
        EnemyPos+=[[X,Y]]
        t+=1

    N=0
    pressedKey=" "
    Privious=[]
    Score=0
    while True:
        print Fore.YELLOW + Style.BRIGHT+"\033["+str(i)+";"+str(j)+"H"+"O"
        
        for a in EnemyPos :
            R=Randomize()
            o=a[0]
            p=a[1]
            
            if R==0: #go Down
                if o<ConsuleSize[0]-1 :
                    if IsThereBlock(p,o+1)!="NO":
                        if [o,p] not in Privious:
                            print Fore.RESET+Back.RESET+"\033["+str(p)+";"+str(o)+"H"+"*"
                        else:
                            print Fore.RESET+Back.RESET+"\033["+str(p)+";"+str(o)+"H"+" "
                        a[0]+=1

            if R==1: #go Up
                if o>2 :
                    if IsThereBlock(p,o-1)!="NO":
                        if [o,p] not in Privious:
                            print Fore.RESET+Back.RESET+"\033["+str(p)+";"+str(o)+"H"+"*"
                        else:
                            print Fore.RESET+Back.RESET+"\033["+str(p)+";"+str(o)+"H"+" "
                        a[0]-=1

            if R==2: #go Left
                if p>2 :
                    if IsThereBlock(p-1,o)!="NO":
                        if [o,p] not in Privious:
                            print Fore.RESET+Back.RESET+"\033["+str(p)+";"+str(o)+"H"+"*"
                        else:
                            print Fore.RESET+Back.RESET+"\033["+str(p)+";"+str(o)+"H"+" "
                        a[1]-=1

            if R==3: #go Right
                if p<ConsuleSize[1]-1 :
                    if IsThereBlock(p+1,o)!="NO":
                        if [o,p] not in Privious:
                            print Fore.RESET+Back.RESET+"\033["+str(p)+";"+str(o)+"H"+"*"
                        else:
                            print Fore.RESET+Back.RESET+"\033["+str(p)+";"+str(o)+"H"+" "
                        a[1]+=1


            print Fore.CYAN +Back.GREEN+"\033["+str(a[1])+";"+str(a[0])+"H"+"@"

        if kbhit():
            pressedKey = getch()

        if ord(pressedKey) == 80: #go Down
            if i<ConsuleSize[1]-1 :
                if IsThereBlock(i+1,j)!="NO":
                    print "\033["+str(i)+";"+str(j)+Back.RESET+"H"+" "

                    i+=1
                    if [j,i] not in Privious :
                        Privious+=[[j,i]]

                    print Fore.YELLOW + Style.BRIGHT+"\033["+str(i)+";"+str(j)+"H"+"O"


        if ord(pressedKey) == 77: #go Right
            if j<ConsuleSize[0]-1 :
                if IsThereBlock(i,j+1)!="NO" :
                    print "\033["+str(i)+";"+str(j)+Back.RESET+"H"+" "

                    j+=1
                    if [j,i] not in Privious :
                        Privious+=[[j,i]]

                    print Fore.YELLOW + Style.BRIGHT+"\033["+str(i)+";"+str(j)+"H"+"O"

        if ord(pressedKey) == 75 : #go Left
            if j>2:
                if IsThereBlock(i,j-1)!="NO" :
                    print "\033["+str(i)+";"+str(j)+Back.RESET+"H"+" "

                    j-=1
                    if [j,i] not in Privious :
                        Privious+=[[j,i]]

                    print Fore.YELLOW + Style.BRIGHT+"\033["+str(i)+";"+str(j)+"H"+"O"

        if ord(pressedKey) == 72 : #go Up
            if i>2 :
                if IsThereBlock(i-1,j)!="NO" :
                    print "\033["+str(i)+";"+str(j)+Back.RESET+"H"+" "

                    i-=1
                    if [j,i] not in Privious :
                        Privious+=[[j,i]]
                    print Fore.YELLOW + Style.BRIGHT+"\033["+str(i)+";"+str(j)+"H"+"O"
        Score = len(Privious)
        print Fore.GREEN+"\033["+str(1)+";"+str(1)+"H"+"SCORE : "+str(Score)
        print Fore.GREEN+"\033["+str(ConsuleSize[1]+5)+";"+str(ConsuleSize[0]/2)+"H"+"LIVES REMAINING : "+str(M)
        if ((ConsuleSize[0]-2)*(ConsuleSize[1]-2))-len(walls) == Score :

            system("cls")
            print "YOU WIN"
            sleep(2)
            High_Score(Score)
            GameMenu()
            break
        if [j, i] in EnemyPos :
            M-=1
            sleep(0.6)
            if M==0 :
                system("cls")
                print "GAME OVER"
                print "SCORE :",Score
                High_Score(Score)
                GameMenu()
                sleep(5)
                break
        if Difficulty==1 :

            sleep(0.15)    
        else :
            sleep(0.06)

        #print Privious
#-----------------------------------------------------------------------------------------
def High_Score(Score):
    file1=open("highscore.txt","r")
    old=file1.readline()
    old=int(old)
    file1.close()
    if old<Score:
        file2=open("highscore.txt","w")
        file2.write(str(Score))
#----------------------------------------------------------------------------------------
def GameMenu():
    a=input("1.NEW GAME\n2.HIGH SCORE\n3.EXIT")
    if a==3 :
        exit()
    if a==2 :
        system("cls")
        file1=open("highscore.txt","r")
        old=file1.readline()
        print int(old)
        GameMenu()
    if a==1 :
        system("cls")
        M=input("NUMBER OF LIVES")
        system("cls")
        Difficulty=input("1.NORMALL\n2.LEGENDARY")

        m=1
        n=1 #stars location

        blocks()

        while m<ConsuleSize[1] :
            n=1
            while n<ConsuleSize[0]:
                if [m,n] not in walls:
                    print position(m,n)+"*"
                n+=1
            m+=1


        n=1
        for m in range (1,ConsuleSize[0]+1):                    #FRAME
            print Back.CYAN+position(n,m)+" "
        n=ConsuleSize[1]
        for m in range (1,ConsuleSize[0]+1):
            print Back.CYAN+position(n,m)+" "      #FRAME
        m=1
        for n in range (1,ConsuleSize[1]):
            print Back.CYAN+position(n,m)+" "      #FRAME
        m=ConsuleSize[0]
        for n in range (1,ConsuleSize[1]+1):
            print Back.CYAN+position(n,m)+" "      #FRAME


        Moving(i,j,M,Difficulty,NumberOfEnemies)
#----------------------------------------------------------------------------------------------------------------
GameMenu()
