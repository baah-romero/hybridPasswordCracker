'''
Fichero en el que se recogen todas las acciones que realiza el algoritmo.
'''
import os
import time
import modules.files
import modules.convert
import modules.guihpc
import modules.permutations

def adNum():
    a=input(str('|----- [+] Numeros añadir: '))
    return a

def adWord():
    a=input(str('|----- [+] Introduce palabra: '))
    return a

def adFile():
    a=input(str('|----- [+] Nombre del filesero a generar: '))
    print('|-------------------------------------------------------------------------------------------------------|')
    return a

def clearTerm():#Limpia la terminal
    if os.name=="posix":
        os.system("clear")
    elif os.name==("ce","nt","dos"):
        os.system("cls")

def adSimWord():#Añadir 1 palabra y permutar
    liPer=[]
    word=adWord()
    cnt,liPer=modules.permutations.palPerms(word)
    for i in range(len(liPer)):
        j=liPer[i]
        modules.files.wrFil(j)
    return cnt,liPer

def perSimWord(a,b):#Añadir 1 palabra y permutar
    liPer=[]
    t1=time.process_time()
    diFile=b
    cntia=0
    for i in range(len(a)):
        i=a[i]
        t2=time.process_time()
        cnt,liPer=modules.permutations.palPerms(i)
        for z in range(len(liPer)):
            w=liPer[z]
            modules.files.wrFil(w, diFile)
            cntia+=1
        t3=time.process_time()
        timing=t3-t2#Tiempo total en permutar 1 palabra
        modules.guihpc.prCntPerWor(i,cnt)
        modules.guihpc.prTimming(timing)
    t4=time.process_time()
    timing=t4-t1#Tiempo total en permutar todas las palabras
    return timing,cntia

def perPnch(a):#Añadir numeros ychars
    lipnch=[]
    for i in range(len(a)):
        word=a[i]
        lipnch=modules.permutations.perPnch(word,10)
        #insertar en filesero si se desea

def adLiWord():#Generar una lista de palabras para el diccionario
    liWoPer=[]
    ac=True
    while ac!=False:
        nwrd=adWord()
        b=modules.convert.enList(nwrd)
        if b!=True:
            liWoPer.append(nwrd)
            ac==True
        elif b==True:
            ac==b
            return ac,liWoPer

def nDiList():
    dicF=modules.files.creDict()
    a,b=adLiWord()
    i=modules.convert.countList(b)
    modules.guihpc.prCnt(i)
    t,c=perSimWord(b,dicF)
    modules.guihpc.resum()
    modules.guihpc.prEndLis(dicF)
    modules.guihpc.prEndCou(c)
    modules.guihpc.prEndTim(t)
